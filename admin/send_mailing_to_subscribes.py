from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from firebase_admin import db

from background import logging
from filters.is_admin import IsAdmin
from filters.is_prof_bureau import IsProfBureau
from handlers import basic
from keyboards.builder_keyboard import build_kb
from utils.states import Mailing

"""
Only admin and prof bureau command
Copy message from admin and send to all subscription users 
"""
router = Router()


# /send or Mailing
@router.message(IsAdmin(), Command("send"))
@router.message(IsAdmin(), F.text.lower().in_(['рассылка', '📣 рассылка']))
@router.message(lambda msg: IsProfBureau(msg).__call__(), Command("send"))
@router.message(lambda msg: IsProfBureau(msg).__call__(), F.text.lower().in_(['рассылка', '📣 рассылка']))
async def which_role(message: Message, state: FSMContext):
    """
    Ask for which role is message
    :param message: Message
    :param state: FSMContext
    """
    await state.set_state(Mailing.for_which_role)
    await message.answer("✨ Для кого будет рассылка?", reply_markup=build_kb(["Для всех", "Для профбюро"]))


@router.message(Mailing.for_which_role)
async def set_message(message: Message, state: FSMContext):
    """
    Send to admin info message, and waiting for mailing message
    :param message: Message
    :param state: FSMContext
    """
    await state.update_data(for_which_role=message.text)
    await state.set_state(Mailing.message)
    await message.answer(f"Напиши сообщение, которое я скопирую и отправлю пользователям\n\n"
                         f"ℹ Можно использовать картинку с текстом\n"
                         f"✳ Если уже не нужно, нажмите отмена", reply_markup=build_kb("Отмена"))


@router.message(Mailing.message)
async def copy_and_send_message_to_users(message: Message, bot: Bot, state: FSMContext):
    """
    Copy admin message and send to all subscribes or prof bureau only, if the cancel button was pressed, returns to menu

    Send to admin info with count of subscription users
    :param message: Message
    :param bot: Bot
    :param state: FSMContext
    """
    await state.update_data(message=message.text)
    data = await state.get_data()
    await state.clear()
    if data["message"].lower() != 'отменить' and data["message"].lower() != 'отмена':
        users = db.reference('users').get()
        count = 0
        for user, value in users.items():
            if data["for_which_role"].lower() == 'для профбюро' or data["for_which_role"].lower() == 'для проф бюро':
                if value['role']['prof_bureau']:
                    count += 1
                    await bot.copy_message(chat_id=user, from_chat_id=message.chat.id, message_id=message.message_id)
            else:
                if value['subscription']:
                    count += 1
                    await bot.copy_message(chat_id=user, from_chat_id=message.chat.id, message_id=message.message_id)
        if data["for_which_role"].lower() == 'для профбюро' or data["for_which_role"].lower() == 'для проф бюро':
            await message.answer(f"ℹ Ваше сообщение было отправлено {count} членам профбюро")
            logging(
                f"Рассылка от {message.from_user.full_name} @{message.from_user.username} для профбюро\n"
                f"Текст: {message.text if message.text is not None else message.caption}")
        else:
            await message.answer(f"ℹ Ваше сообщение было отправлено {count} пользователям")
            logging(f"Рассылка от {message.from_user.full_name} @{message.from_user.username} для всех\n"
                  f"Текст: {message.text if message.text is not None else message.caption}")

    await basic.menu(message)
