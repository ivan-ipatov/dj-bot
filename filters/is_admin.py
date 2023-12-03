from firebase_admin import db


class IsAdmin:
    def __init__(self, msg):
        """
        :param msg: Message
        """
        self.message = msg

    def __call__(self) -> bool:
        """
        :return: bool
        """
        return db.reference(f'users/{self.message.from_user.id}/role/admin').get() is True

    def __invert__(self) -> bool:
        """
        :return: bool
        """
        return db.reference(f'users/{self.message.from_user.id}/role/admin').get() is False
