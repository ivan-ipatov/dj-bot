import random

from aiogram.types import Message
from aiogram import Router, F

from handlers.basic import increase_like, menu

router = Router()


@router.message(F.text.lower().contains('поставить лайк'))
async def click(message: Message):
    increase_like()
    await message.answer_sticker(random.choice(["CAACAgIAAxkBAAEKw_hlViktKngSUGArtQcv4UAsLQhmbQAC4yMAAp2cKUlqWl4-UhqRezME",
                                          "CAACAgIAAxkBAAEKw_ZlVikqyXqFbYz3fYbjg-kooS7w9gACNB8AAut7IUmkLqq_-xLBjDME"]))
    await menu(message)

