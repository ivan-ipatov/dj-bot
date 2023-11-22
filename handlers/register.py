from aiogram import Router
from aiogram.types import Message
from firebase_admin import db

from background import logging
from filters.is_not_registered import IsNotRegistered
from keyboards.builder_keyboard import build_kb

router = Router()


@router.message(IsNotRegistered())
async def register(message: Message):
    """
    Set default user's params in DB
    :param message: Message
    """
    db.reference('/users/').update({
        f'{message.chat.id}': {
            'username': f'@{message.from_user.username}',
            'first_name': f'{message.from_user.first_name}',
            'last_name': f'{message.from_user.last_name if message.from_user.last_name is not None else ""}',
            'full_name': f'{message.from_user.full_name}',
            'subscription': True,
            'role': {
                'admin': False,
                'prof_bureau': False
            },
            'ban': {
                'banned': False,
                'ban_reason': '',
            }
        }
    })
    logging(f'Пользователь {message.from_user.full_name} @{message.from_user.username} зарегистрировался')
    await message.answer(
        "Привет 👋\n"
        "Я бот-помощник Ипатова Ивана,\n"
        "помогаю ему с разными организационными вещами,\n"
        "буду рад и тебе помочь!", reply_markup=build_kb("Привееет, отправь меня в /menu 😊"))
