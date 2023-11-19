from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from firebase_admin import db

from filters.is_admin import IsAdmin
from handlers import basic
from keyboards.builder_keyboard import rmk, builder_kb
from utils.states import BanUser

router = Router()


@router.message(IsAdmin(), Command("ban"))
@router.message(IsAdmin(), F.text.lower().in_(['⛔ забанить/разбанить пользователя', 'забанить', 'разбанить']))
async def ban_user_set(message: Message, state: FSMContext):
    await state.set_state(BanUser.ban)
    await message.answer("‼ Напиши ID кого надо забанить/разбанить")


@router.message(BanUser.ban)
async def ban_user_set(message: Message, state: FSMContext):
    await state.update_data(ban=message.text)
    await state.set_state(BanUser.reason)
    await message.answer("❗ Напиши причину блокировки/разблокировки (либо выбери на клавитуре)",
                         reply_markup=builder_kb(["Спам", "Флуд", "Маты"]))


@router.message(BanUser.reason)
async def ban_user(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(reason=message.text)
    data = await state.get_data()
    ban = data["ban"]
    reason = data["reason"]
    ban_username = str(db.reference(f'/users/{ban}/username').get())
    await state.clear()
    if db.reference(f'/users/{ban}').get() is not None:
        if bool(db.reference(f'/users/{ban}/banned').get()) is True:
            db.reference(f'/users/{ban}/banned').set(False)
            db.reference(f'/users/{data["ban"]}/ban_reason').set(reason)
            await bot.send_message(int(ban), "Поздравляю, тебя разбанили 🎉\n\n"
                                             "Советую тебе больше не нарушать правила 😉")
            await message.answer(f"✅ {ban_username} успешно разбанен")
        else:
            db.reference(f'/users/{data["ban"]}/banned').set(True)
            db.reference(f'/users/{data["ban"]}/ban_reason').set(reason)
            await bot.send_message(int(ban), f"О нет, кажется, тебя забанил администратор 😨\n\n"
                                             f"▶ Причина блокировки: {reason}\n"
                                             f"✳ Для разбана обращаться: {db.reference('main-admin-username').get()}",
                                   reply_markup=rmk)
            await message.answer(f"⛔ {db.reference(f'/users/{ban}/username').get()} успешно забанен")
    else:
        await message.answer("❌ Пользователя с таким ID не существует")
    await basic.menu(message)
