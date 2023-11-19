import random

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from admin.order_toggle_func import get_toggle_true_order
from core.put_like_func import get_like
from admin.toggle_func import get_toggle_true
from keyboards import menu_keyboard
from keyboards.builder_keyboard import builder_kb

router = Router()


# /start
@router.message(Command(commands=['start', 'старт']))
async def start(message: Message):
    await message.answer(
        "Привет 👋\n"
        "Я бот-помощник Ипатова Ивана,\n"
        "помогаю ему с разными организационными вещами,\n"
        "буду рад и тебе помочь!",
        reply_markup=builder_kb("Привееет, отправь меня в /menu 😊"))


# /menu
@router.message(Command(commands=["menu", "меню", "менб", "vty."]))
@router.message(F.text, lambda msg: any(x in msg.text.lower() for x in ["menu", "меню", "менб", "vty."]))
async def menu(message: Message):
    await message.answer("🌐 Выбери действие из меню:",
                         reply_markup=menu_keyboard.builder_menu_kb(get_like(), get_toggle_true(), get_toggle_true_order(), message.from_user.id))


# Greeting
@router.message(F.text.lower().in_(["привет", "здравствуй", "ghbdtn", "хай", "hi", "hello"]))
async def hello(message: Message):
    stickers = ["CAACAgIAAxkBAAEKuWRlTgAB3HBFvqokMIjii0GEh_G9cYAAAgEBAAJWnb0KIr6fDrjC5jQzBA",
                "CAACAgIAAxkBAAEKuWZlTgAB-jXfrtvJxwjuzQmNMHQZJgkAAgQvAALpVQUYHrUJUUv9X_8zBA",
                "CAACAgIAAxkBAAEKuWhlTgEONfy2qV__b75AJ4FyznfVBQACeCEAApwcgEqM13Cb64xqPzME",
                "CAACAgIAAxkBAAEKuW5lTgFGh7_wfFkGNKXT9HwuC51KrwACiksAAulVBRhpZWRcB7KVSjME",
                "CAACAgIAAxkBAAEKuXBlTgF8Etrs78kZCeKDQ5sb-XLurwACjg8AApb4gEkLv6MazlR-gTME"]
    await message.answer_sticker(random.choice(stickers))


# Goodbye
@router.message(F.text.lower().in_(["пока", "прощай", "gjrf", "до встречи", "bye", "goodbye"]))
async def bye(message: Message):
    stickers = ["CAACAgIAAxkBAAEKwCdlU87WE-WQdjm6cd4UcGWzuvvO0AACUgADQbVWDAIQ4mRpfw9yMwQ",
                "CAACAgIAAxkBAAEKwCllU87gxIkWQLvmyJ78X13RMj-_zQACJisAAulVBRi9PhxzIk00KTME",
                "CAACAgIAAxkBAAEKwCtlU88O1WOkV4Ah4lnYSmJd0R5FuQACIAADwZxgDGWWbaHi0krRMwQ",
                "CAACAgIAAxkBAAEKwC1lU89JBVivXrnxHuvdJUcHOtlV1AACYyYAApd2SUsZ-jlAZYzv0DME",
                "CAACAgIAAxkBAAEKwDllU897oLRDyIZ3IL2HNtf0Fznj-QACuUsAAulVBRgv7Eseu3AVmjME"]
    await message.answer_sticker(random.choice(stickers))


# Unexpected message
@router.message()
async def default(message: Message):
    stickers = ["CAACAgIAAxkBAAEKxINlVn4UgQT0RIB23CXrUsYghXDK2QAClh8AAmytIUkmN-0qNzZa3zME",
                "CAACAgIAAxkBAAEKxAVlVjA34eYxpdMAAVClLzRmSbmojVcAAmggAAJz1CFJF3760j-oka4zBA",
                "CAACAgIAAxkBAAEKxIVlVn5iGT4Uv-KgV4Bfqw-tVp1BUAACUB8AAhPkIElqepY7WevrkjME"]
    await message.answer_sticker(random.choice(stickers))
