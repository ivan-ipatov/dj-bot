from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def prof_bureau_menu(get_likes, get_state_of_event_mode):
    """
    Prof bureau menu keyboard
    :param get_likes: int
    :param get_state_of_event_mode: bool
    :return: ReplyKeyboardMarkup
    """
    if not get_state_of_event_mode:
        menu = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="Заказать песню 🎶"), KeyboardButton(text="Оставить отзыв ✨")],
            [KeyboardButton(text=f"Лайков за прошлое мероприятие: {get_likes} 💙")],
            [KeyboardButton(text="📣 Рассылка")]
        ], resize_keyboard=True, one_time_keyboard=True)
    else:
        menu = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="Заказать песню 🎶"), KeyboardButton(text="Оставить отзыв ✨")],
            [KeyboardButton(text=f"Поставить лайк за мероприятие: {get_likes} 💙")],
            [KeyboardButton(text="📣 Рассылка")]
        ], resize_keyboard=True, one_time_keyboard=True)
    return menu
