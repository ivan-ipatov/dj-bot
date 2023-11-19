from aiogram import Router, F
from aiogram.types import Message
import core.swear_words_list

router = Router()


# Is message contains swears
@router.message(F.text, lambda msg: any(x in msg.text.lower().replace("ё", "е") for x in core.swear_words_list.swears))
async def censure(message: Message):
    await message.delete()
    await message.answer("Без мата, пожалуйста ⛔")
    await message.answer_sticker("CAACAgIAAxkBAAEKw_BlViXvxYsB3YiXH22plGK6eifXRQACOxoAAsr-KEm4ngABDdTYwQMzBA")