from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from firebase_admin import db

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
async def set_admin_message(message: Message, state: FSMContext):
    """
    Send to admin info message, and waiting for mailing message
    :param message: Message
    :param state: FSMContext
    """
    await state.set_state(Mailing.message)
    await message.answer("✨ Напиши сообщение, которое придёт всем\n"
                         "подписанным пользователям\n\n"
                         "ℹ Чтобы отменить нажми: отмена", reply_markup=build_kb("Отмена"))


@router.message(Mailing.message)
async def copy_and_send_message_to_users(message: Message, bot: Bot, state: FSMContext):
    """
    Copy admin message and send to all subscribes, if the cancel button was pressed, returns to menu

    Send to admin info with count of subscription users
    :param message: Message
    :param bot: Bot
    :param state: FSMContext
    """
    await state.update_data(message=message.text)
    data = await state.get_data()
    await state.clear()
    if str(data["message"]).lower() != 'отменить' and str(data["message"]).lower() != 'отмена':
        users = db.reference('users').get()
        count = 0
        for user, value in users.items():
            if value['subscription']:
                count += 1
                await bot.copy_message(chat_id=user, from_chat_id=message.chat.id, message_id=message.message_id)
        await message.answer(f"ℹ Ваше сообщение было отправлено {count} пользователям")
        print(f"Рассылка от {message.from_user.full_name} @{message.from_user.username}\n"
              f"Текст: {message.text if message.text is not None else message.caption}")
    await basic.menu(message)
