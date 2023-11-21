import random

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from firebase_admin import db

from admin.toggle_event_mode import get_state_of_event_mode
from admin.toggle_order_songs_mode import get_state_of_order_songs_mode
from core.increase_likes import get_likes
from filters.is_admin import IsAdmin
from filters.is_prof_bureau import IsProfBureau
from keyboards import menu_keyboard, admin_keyboard, prof_bureau_keyboard
from keyboards.builder_keyboard import build_kb

"""
Basic commands of bot
"""

router = Router()


# /start
@router.message(Command(commands=['start', 'старт']))
async def start(message: Message):
    """
    Greeting
    :param message: Message
    """
    await message.answer(
        "Привет 👋\n"
        "Я бот-помощник Ипатова Ивана,\n"
        "помогаю ему с разными организационными вещами,\n"
        "буду рад и тебе помочь!",
        reply_markup=build_kb("Привееет, отправь меня в /menu 😊"))


# # /menu for admin user
# @router.message(Command(commands=["menu", "меню", "менб", "vty."]), IsAdmin)
# @router.message(F.text, lambda msg: any(x in msg.text.lower() for x in ["menu", "меню", "менб", "vty."]), IsAdmin)
# async def admin_menu(message: Message):
#     """
#     Send admin menu keyboard
#     :param message: Message
#     """
#     await message.answer("🌐 Выбери действие из меню:",
#                          reply_markup=admin_menu.admin_menu(get_likes(), get_state_of_event_mode(),
#                                                             get_state_of_order_songs_mode()))
#
# # /menu for admin user
# @router.message(Command(commands=["menu", "меню", "менб", "vty."]), IsAdmin)
# @router.message(F.text, lambda msg: any(x in msg.text.lower() for x in ["menu", "меню", "менб", "vty."]), IsAdmin)
# async def prof_bureau_menu(message: Message):
#     """
#     Send admin menu keyboard
#     :param message: Message
#     """
#     await message.answer("🌐 Выбери действие из меню:",
#                          reply_markup=admin_menu.admin_menu(get_likes(), get_state_of_event_mode(),
#                                                             get_state_of_order_songs_mode()))

# /menu for no role user
@router.message(Command(commands=["menu", "меню", "менб", "vty."]))
@router.message(F.text, lambda msg: any(x in msg.text.lower() for x in ["menu", "меню", "менб", "vty."]))
async def menu(message: Message):
    """
    Send menu keyboard
    :param message: Message
    """
    if IsAdmin.__call__(IsAdmin(), message):
        await message.answer(f"⚙ Привет, {message.from_user.first_name}, сам знаешь, выбирай из меню.\n\n"
                             f"Состояния:\n"
                             f"✳ Режим мероприятия: {'✅' if get_state_of_event_mode() else '❌'}\n"
                             f"🎶 Режим заказа песен: {'✅' if get_state_of_order_songs_mode() and get_state_of_event_mode()  else '❌'}\n"
                             f"😎 Ответственный за меро DJ: {db.reference('dj-name').get()}",
                             reply_markup=admin_keyboard.admin_menu(get_likes(), get_state_of_event_mode(),
                                                                    get_state_of_order_songs_mode()))
    elif IsProfBureau(message).__call__():
        await message.answer(f"💙 Привет, {message.from_user.first_name}, выбери действие из меню:\n\n"
                             f"⭕ Не используй рассылку без надобности, иначе мне придётся её отключить\n"
                             f"{'☑ Тебе доступен заказ песен (привилегия профбюро)' if not get_state_of_order_songs_mode() or not get_state_of_event_mode() else ''}",
                             reply_markup=prof_bureau_keyboard.prof_bureau_menu(get_likes(), get_state_of_event_mode()))
    else:
        await message.answer(f"🌐 {message.from_user.first_name}, выбери действие из меню:",
                             reply_markup=menu_keyboard.no_role_menu(get_likes(), get_state_of_event_mode(),
                                                                     get_state_of_order_songs_mode()))


# Hello message
@router.message(F.text.lower().in_(["привет", "здравствуй", "ghbdtn", "хай", "hi", "hello"]))
async def hello(message: Message):
    """
    Send random hello sticker
    :param message: Message
    """
    stickers = ["CAACAgIAAxkBAAEKuWRlTgAB3HBFvqokMIjii0GEh_G9cYAAAgEBAAJWnb0KIr6fDrjC5jQzBA",
                "CAACAgIAAxkBAAEKuWZlTgAB-jXfrtvJxwjuzQmNMHQZJgkAAgQvAALpVQUYHrUJUUv9X_8zBA",
                "CAACAgIAAxkBAAEKuWhlTgEONfy2qV__b75AJ4FyznfVBQACeCEAApwcgEqM13Cb64xqPzME",
                "CAACAgIAAxkBAAEKuW5lTgFGh7_wfFkGNKXT9HwuC51KrwACiksAAulVBRhpZWRcB7KVSjME",
                "CAACAgIAAxkBAAEKuXBlTgF8Etrs78kZCeKDQ5sb-XLurwACjg8AApb4gEkLv6MazlR-gTME"]
    await message.answer_sticker(random.choice(stickers))


# Goodbye
@router.message(F.text.lower().in_(["пока", "прощай", "gjrf", "до встречи", "bye", "goodbye"]))
async def bye(message: Message):
    """
    Send random bye sticker
    :param message: Message
    """
    stickers = ["CAACAgIAAxkBAAEKwCdlU87WE-WQdjm6cd4UcGWzuvvO0AACUgADQbVWDAIQ4mRpfw9yMwQ",
                "CAACAgIAAxkBAAEKwCllU87gxIkWQLvmyJ78X13RMj-_zQACJisAAulVBRi9PhxzIk00KTME",
                "CAACAgIAAxkBAAEKwCtlU88O1WOkV4Ah4lnYSmJd0R5FuQACIAADwZxgDGWWbaHi0krRMwQ",
                "CAACAgIAAxkBAAEKwC1lU89JBVivXrnxHuvdJUcHOtlV1AACYyYAApd2SUsZ-jlAZYzv0DME",
                "CAACAgIAAxkBAAEKwDllU897oLRDyIZ3IL2HNtf0Fznj-QACuUsAAulVBRgv7Eseu3AVmjME"]
    await message.answer_sticker(random.choice(stickers))


# Unexpected message
@router.message()
async def unexpected_message(message: Message):
    """
    Send random uncomprehending sticker
    :param message: Message
    """
    stickers = ["CAACAgIAAxkBAAEKxINlVn4UgQT0RIB23CXrUsYghXDK2QAClh8AAmytIUkmN-0qNzZa3zME",
                "CAACAgIAAxkBAAEKxAVlVjA34eYxpdMAAVClLzRmSbmojVcAAmggAAJz1CFJF3760j-oka4zBA",
                "CAACAgIAAxkBAAEKxIVlVn5iGT4Uv-KgV4Bfqw-tVp1BUAACUB8AAhPkIElqepY7WevrkjME"]
    await message.answer_sticker(random.choice(stickers))
