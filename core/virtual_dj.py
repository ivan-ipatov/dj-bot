import os
import requests
from firebase_admin import db


async def send_song(name: str, message: str):
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
