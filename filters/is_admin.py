from aiogram.types import Message
from firebase_admin import db


class IsAdmin:
    def __call__(self, message: Message) -> bool:
        return db.reference(f'users/{message.from_user.id}/admin').get() is True
