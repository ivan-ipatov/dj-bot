from aiogram import Router
from aiogram.types import Message
from firebase_admin import db

from filters.is_admin import IsAdmin
from filters.is_banned import IsBanned
from filters.is_prof_bureau import IsProfBureau
from keyboards.builder_keyboard import rmk

"""
Used for send information to user, if banned 
"""

router = Router()


@router.message(IsBanned(), IsProfBureau or IsAdmin)
async def banned(message: Message):
    """
    Send message to prof bureau user with ban information
    :param message: Message
    """
    await message.answer(
        f"⛔ {db.reference(f'users/{message.from_user.id}/first_name').get()}, блин, как так? Тебя забанил "
        f"администратор\n\n"
        f"▶ Причина блокировки: {db.reference(f'users/{message.from_user.id}/ban/ban_reason').get()}\n"
        f"✳ Для разбана обращаться: {db.reference('main-admin-username').get()} (100₽)",
        reply_markup=rmk)


@router.message(IsBanned())
async def banned(message: Message):
    """
    Send message to user with ban information
    :param message: Message
    """
    await message.answer(f"⛔ Тебя забанил администратор\n\n"
                         f"▶ Причина блокировки: {db.reference(f'users/{message.from_user.id}/ban/ban_reason').get()}\n"
                         f"✳ Для разбана обращаться: {db.reference('main-admin-username').get()}",
                         reply_markup=rmk)
