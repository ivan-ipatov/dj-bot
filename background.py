import os
from threading import Thread

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask import Flask, render_template

from admin.toggle_event_mode import get_state_of_event_mode
from admin.toggle_order_songs_mode import get_state_of_order_songs_mode


# Fetch the service account key JSON file contents
cred = credentials.Certificate('botdb.json')

# Initialize the app with a service account, granting admin privileges
fb_app = firebase_admin.initialize_app(cred, {
    'databaseURL': os.environ['DB_URL']
})

app = Flask('')


@app.route('/')
def home():
    return render_template('home.html', state_event_mode=get_state_of_event_mode(),
                           state_songs_order_mode=get_state_of_order_songs_mode(),
                           dj_name=str(
                               db.reference('dj-name').get()))


# @app.route('/robots.txt')
# def no_robots():
#     return send_from_directory(app.static_folder, request.path[1:])


def run():
    app.run(host='0.0.0.0', port=80)


def keep_alive():
    t = Thread(target=run)
    t.start()
