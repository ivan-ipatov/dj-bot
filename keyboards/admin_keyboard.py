from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def admin_menu(get_likes, get_state_of_event_mode, get_state_of_order_songs_mode):
    """
    Admin menu keyboard
    :param get_likes: int
    :param get_state_of_event_mode: bool
    :param get_state_of_order_songs_mode: bool
    :return: ReplyKeyboardMarkup
    """
    if get_state_of_event_mode and get_state_of_order_songs_mode:
        menu = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="Заказать песню 🎶"), KeyboardButton(text="Оставить отзыв ✨")],
            [KeyboardButton(text=f"Поставить лайк мероприятию: {get_likes} 💙")],
            [KeyboardButton(text="⛔ Выключить меро"), KeyboardButton(text="⛔ Выключить песни")],
            [KeyboardButton(text="⛔ Забанить/разбанить пользователя")],
            [KeyboardButton(text="📣 Рассылка"), KeyboardButton(text="🔄 Смена")]
        ], resize_keyboard=True, one_time_keyboard=True)
    elif get_state_of_event_mode and not get_state_of_order_songs_mode:
        menu = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="Заказать песню 🎶"), KeyboardButton(text="Оставить отзыв ✨")],
            [KeyboardButton(text=f"Поставить лайк мероприятию: {get_likes} 💙")],
            [KeyboardButton(text="⛔ Выключить меро"), KeyboardButton(text="✅ Включить песни")],
            [KeyboardButton(text="⛔ Забанить/разбанить пользователя")],
            [KeyboardButton(text="📣 Рассылка"), KeyboardButton(text="🔄 Смена")]
        ], resize_keyboard=True, one_time_keyboard=True)
    else:
        menu = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="Заказать песню 🎶"), KeyboardButton(text="Оставить отзыв ✨")],
            [KeyboardButton(text=f"Лайков за прошлое мероприятие: {get_likes} 💙")],
            [KeyboardButton(text="✅ Включить мероприятие")],
            [KeyboardButton(text="⛔ Забанить/разбанить пользователя")],
            [KeyboardButton(text="📣 Рассылка"), KeyboardButton(text="🔄 Смена")]
        ], resize_keyboard=True, one_time_keyboard=True)
    return menu
