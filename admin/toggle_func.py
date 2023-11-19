from firebase_admin import db

def do_toggle():
    if get_toggle_true():
        db.reference('event-mode').set(False)
    else:
        db.reference('event-mode').set(True)


def get_toggle_true(self=None) -> bool:
    return bool(db.reference('event-mode').get())


def get_toggle_false(self=None) -> bool:
    return not bool(db.reference('event-mode').get())
