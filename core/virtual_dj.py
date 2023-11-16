import os
import requests

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
    requests.post(url=os.environ['DJ_URL'], headers=headers, data=data)
