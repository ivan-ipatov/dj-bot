import random

from aiogram import Router, F
from aiogram.enums import content_type
from aiogram.filters import Command
from aiogram.types import Message
from keyboards import menu_keyboard
from keyboards.builder_keyboard import builder_kb


router = Router()
like = 0

def increase_like():
    global like
    like += 1

def get_like():
    return like


# Swears
@router.message(F.text.func(lambda text: any(
    x in text.lower() for x in
    ["блять", "сука", "пизда", "пидр", "пидарас", "мразь", "мудак", "blyat", "pizda", "нахуй", "еблан", "шлюха",
     "тварь"])))
async def censure(message: Message):
    await message.delete()
    await message.answer("Без мата, пожалуйста ⛔")
    await message.answer_sticker("CAACAgIAAxkBAAEKw_BlViXvxYsB3YiXH22plGK6eifXRQACOxoAAsr-KEm4ngABDdTYwQMzBA")


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
@router.message(F.text.func(lambda text: any(x in text.lower() for x in ["menu", "меню", "менб", "vty."])))
async def menu(message: Message):
    await message.answer("🌐 Выбери действие из меню:", reply_markup=menu_keyboard.builder_menu_kb(get_like()))


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
    stickers = ["CAACAgIAAxkBAAEKuXJlTgJB5IH-C9R4ds1auxUhSrT7swAC8g8AAiPMeEnhoUI9nHuCtTME",
                "CAACAgIAAxkBAAEKwEtlU9KPMOe-8I-Zjf4qEMZ2a8YzqwACkUsAAulVBRi55GuHH19IrjME",
                "CAACAgIAAxkBAAEKuXZlTgK51S3ibNKn-w_xbsKAcj4IwQACfwUAAj-VzAqgnsuFcST4RTME",
                "CAACAgEAAxkBAAEKwE1lU9LX2u_Qee2qKSzqtPiWIl6R4gACggkAAr-MkASrQ88OYNnBpjME",
                "CAACAgIAAxkBAAEKwFNlU9NbeDpBIXUUJzYBo5t8QliCXQACGAADwDZPE9b6J7-cahj4MwQ"]
    await message.answer_sticker(random.choice(stickers))
