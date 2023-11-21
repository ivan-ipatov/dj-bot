import operator

from aiogram.types import Message
from firebase_admin import db


class IsProfBureau:
    def __init__(self, msg):
        """
        :param msg: Message
        """
        self.message = msg

    def __call__(self) -> bool:
        """
        :return: bool
        """
        return db.reference(f'users/{self.message.from_user.id}/role/prof_bureau').get() is True

    def __invert__(self) -> bool:
        """
        :return: bool
        """
        return db.reference(f'users/{self.message.from_user.id}/role/prof_bureau').get() is False
