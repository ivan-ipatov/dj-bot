from firebase_admin import db
from background import fb_app


def increase_like_helper(current_value):
    return current_value + 1


def increase_like():
    db.reference('likes').transaction(increase_like_helper)


def get_like():
    return int(db.reference('likes').get())
