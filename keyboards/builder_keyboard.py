from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def build_kb(text: str | list):
    """
    Help to build simple keyboard
    :param text: str | list
    :return: ReplyKeyboardBuilder
    """
    builder = ReplyKeyboardBuilder()

    if isinstance(text, str):
        text = [text]

    [builder.button(text=txt) for txt in text]
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


rmk = ReplyKeyboardRemove()
