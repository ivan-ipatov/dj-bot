from aiogram.types import Message
from firebase_admin import db


class IsMaintenance:
    def __call__(self, message: Message) -> bool:
        """
        If bot in maintenance
        :param message: Message
        :return: bool
        """
        return db.reference('maintenance-mode').get() is True
