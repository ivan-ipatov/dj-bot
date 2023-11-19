from firebase_admin import db


def do_toggle_order():
    if get_toggle_true_order():
        db.reference('order-songs-mode').set(False)
    else:
        db.reference('order-songs-mode').set(True)


def get_toggle_true_order(self=None) -> bool:
    return bool(db.reference('order-songs-mode').get())


def get_toggle_false_order(self=None) -> bool:
    return not bool(db.reference('order-songs-mode').get())
