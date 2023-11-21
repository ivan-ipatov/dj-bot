import requests
from firebase_admin import db


async def post_data_to_virualdj(name: str, message: str):
    """
    Post data to https://virtualdj.com/ask for order songs
    :param name: str
    :param message: str
    """
    data = {
        'name': name,
        'message': message
    }
    headers = {
        "Access-Control-Allow-Origin": "*",
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    requests.post(url=str(db.reference('dj-url').get()), headers=headers, data=data)
