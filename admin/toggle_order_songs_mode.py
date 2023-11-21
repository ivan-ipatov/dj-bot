from firebase_admin import db

def toggle_order_songs_mode():
    """
    Turn on/off order songs mode

    Set key 'order-songs-mode' in DB True/False
    """
    if get_state_of_order_songs_mode():
        db.reference('order-songs-mode').set(False)
    else:
        db.reference('order-songs-mode').set(True)


def get_state_of_order_songs_mode(self=None) -> bool:
    """
    Get state of 'order-songs-mode' in DB
    :param self: Any
    :return: bool
    """
    return bool(db.reference('order-songs-mode').get())


def get_reverted_state_of_order_songs_mode(self=None) -> bool:
    """
    Get state inversion of 'order-songs-mode' in DB

    Used for filtering message, if 'order-songs-mode' is False
    :param self: Any
    :return: bool
    """
    return not bool(db.reference('order-songs-mode').get())
