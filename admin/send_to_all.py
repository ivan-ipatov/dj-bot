from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from firebase_admin import db
from aiogram.filters import Command
from filters.is_admin import IsAdmin
from handlers import basic
from utils.states import SendToAll

router = Router()


@router.message(IsAdmin(), Command("send"))
@router.message(IsAdmin(), F.text.lower().in_(['рассылка', '📣 рассылка']))
async def send_to_all_set(message: Message, state: FSMContext):
    await state.set_state(SendToAll.mes)
    await message.answer("✨ Напиши сообщение, которое придёт всем подписанным пользователям")


@router.message(SendToAll.mes)
async def send_to_all_func(message: Message, bot: Bot, state: FSMContext):
    await state.clear()
    users = db.reference('users').get()
    for user, value in users.items():
        if value['subscription']:
            await bot.copy_message(chat_id=user, from_chat_id=message.chat.id, message_id=message.message_id)
    await message.answer(f"ℹ Ваше сообщение было отправлено {len(users)} пользователям")
    await basic.menu(message)