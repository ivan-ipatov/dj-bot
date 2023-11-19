from aiogram.fsm.state import State, StatesGroup


class OrderSongList(StatesGroup):
    song = State()


class Reviews(StatesGroup):
    review = State()


class Permission(StatesGroup):
    perm = State()


class PermissionOrder(StatesGroup):
    perm = State()


class BanUser(StatesGroup):
    ban = State()
    reason = State()


class SendToAll(StatesGroup):
    mes = State()
