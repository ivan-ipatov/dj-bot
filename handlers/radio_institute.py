import random
import time

from aiogram import Router, F
from aiogram.types import Message, URLInputFile

router = Router()


async def start_chant(message):
    await message.answer("🔵 Всё радисты твёрдо знают тройку самых важных слов:")
    await chant(message)

async def chant(message):
    time.sleep(0.15)
    await message.answer("РТФ!")
    time.sleep(0.25)
    await message.answer("УрФУ!")
    time.sleep(0.25)
    await message.answer("Попов!")

async def another_chant(message):
    await message.answer("Родился радистом...")
    time.sleep(0.25)
    await message.answer("Умру программистом!")

async def pictures_chant(message):
    for photo in ["https://rtf.urfu.ru/fileadmin/user_upload/site_19652/main_page/photo_slides_img/cXeo3iPj1hk.jpg", "https://static.ucheba.ru/thumbs/809/-/pix/uz_photo//1504.full.webp", "https://etu.ru/assets/cache/images/ru/universitet/novosti/1280x854-popovchteniya.a71.jpg"]:
        await message.answer_photo(URLInputFile(photo))


# Radik
@router.message(F.text, lambda msg: any(x in msg.text.lower() for x in ["радик", "ртф", "ирит-ртф", "hna", "bhbn-hna"]))
async def menu(message: Message):
    r = random.randint(0, 5)
    if r == 0:
        await start_chant(message)
    elif r == 1:
        await chant(message)
    elif r == 2:
        await another_chant(message)
    elif r == 3:
        await start_chant(message)
        time.sleep(0.75)
        await another_chant(message)
    elif r == 4:
        await pictures_chant(message)
    else:
        await message.answer_sticker("CAACAgIAAxkBAAEKxIllVoHtnbDHMr7zlqEEVSF1huPxWgACwx4AAhoMKEmHNGe_wAl3MDME")