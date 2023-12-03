import os

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from firebase_admin import db

from filters.is_admin import IsAdmin
from handlers import basic

"""
Only admin command
Change global DJ name and URL for Virtual DJ
"""

router = Router()


@router.message(lambda msg: IsAdmin(msg).__call__(), Command("ChangeDJ"))
@router.message(lambda msg: IsAdmin(msg).__call__(), F.text.lower().in_(["🔄 смена", "смена", "сменить dj"]))
async def change_dj(message: Message):
    """
    Change DJ name and URL
    :param message: Message
    """
    if str(db.reference('dj-name').get()) == os.environ['DJ_NAME']:
        db.reference('dj-name').set(os.environ['DJ_NAME_2'])
        db.reference('dj-url').set(os.environ['DJ_URL_2'])
        await message.answer(f"✅ Вы успешно сменили DJ\n\n"
                             f"▶ Сейчас DJ является: {os.environ['DJ_NAME_2']}")
    else:
        db.reference('dj-name').set(os.environ['DJ_NAME'])
        db.reference('dj-url').set(os.environ['DJ_URL'])
        await message.answer(f"✅ Вы успешно сменили DJ\n\n"
                             f"▶ Сейчас DJ является: {os.environ['DJ_NAME']}")
    await basic.menu(message)
