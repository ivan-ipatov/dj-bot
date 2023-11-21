from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def no_role_menu(get_likes, get_state_of_event_mode, get_state_of_order_songs_mode):
    """
    Default user menu with no role
    :param get_likes: int
    :param get_state_of_event_mode: bool
    :param get_state_of_order_songs_mode: bool
    :return: ReplyKeyboardMarkup
    """
    if get_state_of_event_mode and get_state_of_order_songs_mode:
        menu = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="Заказать песню 🎶"), KeyboardButton(text="Оставить отзыв ✨")],
            [KeyboardButton(text=f"Поставить лайк за мероприятие: {get_likes} 💙")]
        ], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Можешь выбрать ниже:')
    elif get_state_of_event_mode and not get_state_of_order_songs_mode:
        menu = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="🔒 Заказать песню"), KeyboardButton(text="Оставить отзыв ✨")],
            [KeyboardButton(text=f"Поставить лайк за мероприятие: {get_likes} 💙")]
        ], resize_keyboard=True, one_time_keyboard=True,
            input_field_placeholder='Можешь поставить лайк или написать отзыв')
    else:
        menu = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="🔒 Заказать песню"), KeyboardButton(text="Оставить отзыв ✨")],
            [KeyboardButton(text=f"Лайков за прошлое мероприятие: {get_likes} 💙")]
        ], resize_keyboard=True, one_time_keyboard=True,
            input_field_placeholder='Пока что ты можешь оставить только отзыв:')
    return menu
