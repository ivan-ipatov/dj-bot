from aiogram.types import Message
from firebase_admin import db


class IsBanned:
    def __call__(self, message: Message) -> bool:
        return db.reference(f'users/{message.from_user.id}/banned').get() is True
