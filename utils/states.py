from aiogram.fsm.state import State, StatesGroup


class OrderSong(StatesGroup):
    song = State()


class Reviews(StatesGroup):
    review = State()


class RequestForToggleOrderSongsMode(StatesGroup):
    confirm = State()


class RequestForToggleEventMode(StatesGroup):
    confirm = State()


class BanUser(StatesGroup):
    ban_id = State()
    reason = State()


class Mailing(StatesGroup):
    message = State()
