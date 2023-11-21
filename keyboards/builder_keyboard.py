from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def build_kb(text: str | list):
    """
    Help to build simple keyboard
    :param text: str | list
    :return: ReplyKeyboardBuilder
    """

    if isinstance(text, str):
        text = [text]

    [ReplyKeyboardBuilder().button(text=txt) for txt in text]
    return ReplyKeyboardBuilder().as_markup(resize_keyboard=True, one_time_keyboard=True)


rmk = ReplyKeyboardRemove()
