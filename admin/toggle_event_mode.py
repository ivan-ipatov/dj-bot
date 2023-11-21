from firebase_admin import db


def toggle_event_mode():
    """
    Turn on/off event mode

    Set key 'event-mode' in DB True/False
    """
    if get_state_of_event_mode():
        db.reference('event-mode').set(False)
    else:
        db.reference('event-mode').set(True)


def get_state_of_event_mode(self=None) -> bool:
    """
    Get state of 'event-mode' in DB
    :param self: Any
    :return: bool
    """
    return bool(db.reference('event-mode').get())


def get_reverted_state_of_event_mode(self=None) -> bool:
    """
    Get state inversion of 'event-mode' in DB

    Used for filtering message, if 'event-mode' is False
    :param self: Any
    :return: bool
    """
    return not bool(db.reference('event-mode').get())
