from aiogram import Router
from aiogram.types import Message
from firebase_admin import db

from filters.is_banned import IsBanned
from keyboards.builder_keyboard import rmk

router = Router()


@router.message(IsBanned())
async def banned(message: Message):
    await message.answer(f"⛔ Тебя забанил администратор\n\n"
                         f"▶ Причина блокировки: {db.reference(f'users/{message.from_user.id}/ban_reason').get()}\n"
                         f"✳ Для разбана обращаться: {db.reference('main-admin-username').get()}",
                         reply_markup=rmk)
