from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from firebase_admin import db



def builder_menu_kb(get_like, get_toggle_true, get_toggle_true_order, userid):
    if db.reference(f'users/{userid}/admin').get() is False:
        if get_toggle_true and get_toggle_true_order:
            menu = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton(text="Заказать песню 🎶"), KeyboardButton(text="Оставить отзыв ✨")],
                [KeyboardButton(text=f"Поставить лайк за мероприятие: {get_like} 💙")]
            ], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Можешь выбрать ниже:')
            return menu
        elif get_toggle_true and not get_toggle_true_order:
            menu = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton(text="🔒 Заказать песню"), KeyboardButton(text="Оставить отзыв ✨")],
                [KeyboardButton(text=f"Поставить лайк за мероприятие: {get_like} 💙")]
            ], resize_keyboard=True, one_time_keyboard=True,
                input_field_placeholder='Можешь поставить лайк или написать отзыв')
            return menu
        else:
            menu = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton(text="🔒 Заказать песню"), KeyboardButton(text="Оставить отзыв ✨")],
                [KeyboardButton(text=f"Лайков за прошлое мероприятие: {get_like} 💙")]
            ], resize_keyboard=True, one_time_keyboard=True,
                input_field_placeholder='Пока что ты можешь оставить только отзыв:')
            return menu
    else:
        if get_toggle_true and get_toggle_true_order:
            menu = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton(text="Заказать песню 🎶"), KeyboardButton(text="Оставить отзыв ✨")],
                [KeyboardButton(text=f"Поставить лайк за мероприятие: {get_like} 💙")],
                [KeyboardButton(text="⛔ Выключить меро"), KeyboardButton(text="⛔ Выключить песни")],
                [KeyboardButton(text="⛔ Забанить/разбанить пользователя")],
                [KeyboardButton(text="📣 Рассылка"), KeyboardButton(text="🔄 Смена")]
            ], resize_keyboard=True, one_time_keyboard=True)
            return menu
        elif get_toggle_true and not get_toggle_true_order:
            menu = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton(text="🔒 Заказать песню"), KeyboardButton(text="Оставить отзыв ✨")],
                [KeyboardButton(text=f"Поставить лайк за мероприятие: {get_like} 💙")],
                [KeyboardButton(text="⛔ Выключить меро"), KeyboardButton(text="✅ Включить песни")],
                [KeyboardButton(text="⛔ Забанить/разбанить пользователя")],
                [KeyboardButton(text="📣 Рассылка"), KeyboardButton(text="🔄 Смена")]
            ], resize_keyboard=True, one_time_keyboard=True)
            return menu
        else:
            menu = ReplyKeyboardMarkup(keyboard=[
                [KeyboardButton(text="🔒 Заказать песню"), KeyboardButton(text="Оставить отзыв ✨")],
                [KeyboardButton(text=f"Лайков за прошлое мероприятие: {get_like} 💙")],
                [KeyboardButton(text="✅ Включить мероприятие")],
                [KeyboardButton(text="⛔ Забанить/разбанить пользователя")],
                [KeyboardButton(text="📣 Рассылка"), KeyboardButton(text="🔄 Смена")]
            ], resize_keyboard=True, one_time_keyboard=True)
            return menu
