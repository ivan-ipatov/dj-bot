from aiogram import Router
from aiogram.types import Message
from firebase_admin import db
from filters.is_not_registered import IsNotRegistered
from keyboards.builder_keyboard import builder_kb

router = Router()


@router.message(IsNotRegistered())
async def register(message: Message):
    db.reference('/users/').update({
        f'{message.chat.id}': {
            'username': f'@{message.from_user.username}',
            'first_name': f'{message.from_user.first_name}',
            'last_name': f'{message.from_user.last_name}',
            'full_name': f'{message.from_user.full_name}',
            'admin': False,
            'subscription': True,
            'banned': False,
            'ban_reason': ''
        }
    })
    await message.answer(
        "Привет 👋\n"
        "Я бот-помощник Ипатова Ивана,\n"
        "помогаю ему с разными организационными вещами,\n"
        "буду рад и тебе помочь!", reply_markup=builder_kb("Привееет, отправь меня в /menu 😊"))

