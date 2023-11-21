from firebase_admin import db


def increase_like(current_value):
    """
    :param current_value: int
    :return: int
    """
    return current_value + 1


def increase_likes_in_db():
    db.reference('likes').transaction(increase_like)


def get_likes():
    """
    Return quantity of likes in DB
    :return: int
    """
    return int(db.reference('likes').get())
