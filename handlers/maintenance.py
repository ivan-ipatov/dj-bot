import random

from aiogram import Router
from aiogram.types import Message, URLInputFile

from filters.is_admin import IsAdmin
from filters.is_maintenance import IsMaintenance

router = Router()


@router.message(lambda msg: ~IsAdmin(msg), IsMaintenance())
async def maintenance_mode(message: Message):
    """
    Bot in maintenance message
    :param message: Message
    """
    photo = random.choice([
        "http://chem-teacher.ru/wp-content/uploads/2018/05/kot-iz-shreka_167506705_orig_-300x225.jpg",
        "https://espritgames.ru/wp-content/uploads/sites/2/2022/04/SAO2_maintenance.jpg",
        "https://dota2.ru/img/memes/2019/10/63351.jpg",
        "https://habrastorage.org/getpro/habr/upload_files/baf/b76/3a5/bafb763a54d1cd106a9493c2862ad757.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Bsodwindows10.png/1200px-Bsodwindows10.png"
    ])
    await message.answer_photo(URLInputFile(photo), "Ведутся технические работы 🔧")
