import random
from aiogram.types import Message
from aiogram import Router, F
from handlers.basic import menu
from core.put_like_func import increase_like
from admin.toggle_func import get_toggle_false, get_toggle_true

router = Router()


# if toggle is False
@router.message(F.text, lambda msg: any(x in msg.text.lower() for x in ['поставить лайк', 'лайков за прошлое']),
                get_toggle_false)
async def set_song_message(message: Message):
    await menu(message)


# if toggle is True
@router.message(F.text, lambda msg: any(x in msg.text.lower() for x in ['поставить лайк', 'лайков за прошлое']),
                get_toggle_true)
async def click(message: Message):
    increase_like()
    await message.answer_sticker(
        random.choice(["CAACAgIAAxkBAAEKw_hlViktKngSUGArtQcv4UAsLQhmbQAC4yMAAp2cKUlqWl4-UhqRezME",
                       "CAACAgIAAxkBAAEKw_ZlVikqyXqFbYz3fYbjg-kooS7w9gACNB8AAut7IUmkLqq_-xLBjDME"]))
    await menu(message)
