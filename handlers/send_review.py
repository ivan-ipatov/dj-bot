import os
import random

from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from firebase_admin import db

from handlers import basic
from utils.states import Reviews

router = Router()


# Waiting for review
@router.message(F.text.lower().in_(["оставить отзыв ✨", "оставить отзыв", "отзыв", "админ"]))
async def set_review(message: Message, state: FSMContext):
    await state.set_state(Reviews.review)
    await message.answer("Здесь ты можешь оставить отзыв\n"
                         "о моей работе или о работе Вани\n\n"
                         "Спасибо, что делаешь нас лучше 💙")


# Sending review to admin
@router.message(Reviews.review)
async def send_review(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(review=message.text)
    data = await state.get_data()
    if data["review"] is not None:
        await bot.send_message(int(db.reference('main-admin-id').get()),
                               f"👉 Отзыв от {message.from_user.first_name} {message.from_user.last_name}\n\n"
                               f"{data['review']}\n\n"
                               f"▶ @{message.from_user.username}\n"
                               f"🆔 {message.from_user.id}")
    else:
        await bot.send_message(int(db.reference('main-admin-id').get()),
                               f"Отзыв от {message.from_user.first_name} {message.from_user.last_name}\n"
                               f"▶ @{message.from_user.username}\n"
                               f"🆔 {message.from_user.id}")
        await message.send_copy(int(db.reference('main-admin-id').get()))
    await state.clear()
    await message.answer("Отзыв отправлен, спасибо ✨")
    await message.answer_sticker(
        random.choice(["CAACAgIAAxkBAAEKw_hlViktKngSUGArtQcv4UAsLQhmbQAC4yMAAp2cKUlqWl4-UhqRezME",
                       "CAACAgIAAxkBAAEKw_ZlVikqyXqFbYz3fYbjg-kooS7w9gACNB8AAut7IUmkLqq_-xLBjDME"]))
    await basic.menu(message)
