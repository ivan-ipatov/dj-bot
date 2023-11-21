import random

from aiogram import Router, F
from aiogram.types import Message

from admin.toggle_event_mode import get_reverted_state_of_event_mode, get_state_of_event_mode
from core.increase_likes import increase_likes_in_db
from handlers.basic import menu

"""
Global like to event
"""

router = Router()


@router.message(F.text, lambda msg: any(x in msg.text.lower() for x in ['поставить лайк', 'лайков за прошлое']),
                get_reverted_state_of_event_mode)
async def put_like_is_unavailable(message: Message):
    """
    Go to menu
    :param message: Message
    """
    await menu(message)


@router.message(F.text, lambda msg: any(x in msg.text.lower() for x in ['поставить лайк', 'лайков за прошлое']),
                get_state_of_event_mode)
async def put_like(message: Message):
    """
    Increasing likes in DB
    :param message:
    :return:
    """
    increase_likes_in_db()
    await message.answer_sticker(
        random.choice(["CAACAgIAAxkBAAEKw_hlViktKngSUGArtQcv4UAsLQhmbQAC4yMAAp2cKUlqWl4-UhqRezME",
                       "CAACAgIAAxkBAAEKw_ZlVikqyXqFbYz3fYbjg-kooS7w9gACNB8AAut7IUmkLqq_-xLBjDME"]))
    await menu(message)
