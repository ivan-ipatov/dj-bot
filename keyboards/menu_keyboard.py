from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def builder_menu_kb(get_like):
    menu = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Заказать песню 🎶"), KeyboardButton(text="Оставить отзыв ✨")],
        [KeyboardButton(text=f"Поставить лайк за мероприятие: {get_like} 💙")]
    ], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Можешь выбрать ниже:')
    return menu


