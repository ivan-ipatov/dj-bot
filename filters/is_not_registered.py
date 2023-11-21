from aiogram.types import Message
from firebase_admin import db


class IsNotRegistered:
    def __call__(self, message: Message) -> bool:
        """
        :param message: Message
        :return: bool
        """
        return db.reference(f'users/{message.from_user.id}').get() is None
