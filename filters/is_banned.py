from aiogram.types import Message
from firebase_admin import db


class IsBanned:
    def __call__(self, message: Message) -> bool:
        """
        If user is banned and hasn't role "admin"
        :param message: Message
        :return: bool
        """
        return db.reference(f'users/{message.from_user.id}/ban/banned').get() and not db.reference(
            f'users/{message.from_user.id}/role/admin').get() is True
