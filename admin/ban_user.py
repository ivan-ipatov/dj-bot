import logging

from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from firebase_admin import db

from filters.is_admin import IsAdmin
from handlers import basic
from keyboards.builder_keyboard import rmk, build_kb
from utils.states import BanUser

"""
Only admin command
Ban/unban a user by his ID 
"""

router = Router()


# /ban or Ban user command
@router.message(IsAdmin(), Command("ban"))
@router.message(IsAdmin(), F.text.lower().in_(['⛔ забанить/разбанить пользователя', 'забанить', 'разбанить']))
async def ban_user_set_id(message: Message, state: FSMContext):
    """
    Requests Telegram user ID for blocking
    :param message: Message
    :param state: FSMContext
    """
    await state.set_state(BanUser.ban_id)
    await message.answer("‼ Напиши ID кого надо забанить/разбанить")


@router.message(BanUser.ban_id)
async def ban_user_set_reason(message: Message, state: FSMContext):
    """
    Requests reason for blocking and set state of user's ID
    :param message: Message
    :param state: FSMContext
    """
    await state.update_data(ban_id=message.text)
    await state.set_state(BanUser.reason)
    await message.answer("❗ Напиши причину блокировки/разблокировки (либо выбери на клавиатуре)",
                         reply_markup=build_kb(["Спам", "Флуд", "Маты"]))


@router.message(BanUser.reason)
async def ban_user(message: Message, state: FSMContext, bot: Bot):
    """
    Ban/unban the user and returns the administrator to the menu
    :param message: Message
    :param state: FSMContext
    :param bot: Bot
    """
    await state.update_data(reason=message.text)
    data = await state.get_data()
    ban_id = data["ban_id"]
    reason = data["reason"]
    ban_username = str(db.reference(f'/users/{ban_id}/username').get())
    await state.clear()
    # If user with this ID is exist
    if db.reference(f'/users/{ban_id}').get() is not None:
        # If user with this ID already banned
        if bool(db.reference(f'/users/{ban_id}/ban/banned').get()) is True:
            db.reference(f'/users/{ban_id}/ban/banned').set(False)
            db.reference(f'/users/{ban_id}/ban/ban_reason').set(reason)
            logging.info(f"Админ: @{message.from_user_username} разбанил @{ban_username}, причина: {reason}")
            await bot.send_message(int(ban_id), "Поздравляю, тебя разбанили 🎉\n\n"
                                                "Советую тебе больше не нарушать правила 😉")
            await message.answer(f"✅ {ban_username} успешно разбанен")
        # If user isn't banned
        else:
            db.reference(f'/users/{ban_id}/ban/banned').set(True)
            db.reference(f'/users/{ban_id}/ban/ban_reason').set(reason)
            logging.info(f"Админ: @{message.from_user_username} забанил @{ban_username}, причина: {reason}")
            await bot.send_message(int(ban_id), f"О нет, кажется, тебя забанил администратор 😨\n\n"
                                                f"▶ Причина блокировки: {reason}\n"
                                                f"✳ Для разбана обращаться: {db.reference('main-admin-username').get()}",
                                   reply_markup=rmk)
            await message.answer(f"⛔ {db.reference(f'/users/{ban_id}/username').get()} успешно забанен")
    else:
        await message.answer("❌ Пользователя с таким ID не существует")
    await basic.menu(message)
