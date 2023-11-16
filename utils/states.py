from aiogram.fsm.state import State, StatesGroup

class OrderSongList(StatesGroup):
    song = State()

class Reviews(StatesGroup):
    review = State()