import logging
from threading import Thread

from firebase_admin import db
from flask import Flask, render_template, send_from_directory, request

from admin.toggle_event_mode import get_state_of_event_mode
from admin.toggle_order_songs_mode import get_state_of_order_songs_mode

# Only errors logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask('')

@app.route('/')
def home():
    return render_template('home.html', state_event_mode=get_state_of_event_mode(),
                           state_songs_order_mode=get_state_of_order_songs_mode(),
                           dj_name=str(
                               db.reference('dj-name').get()))


@app.route('/robots.txt')
def no_robots():
    return send_from_directory(app.static_folder, request.path[1:])


def run():
    app.run(host='0.0.0.0', port=80)


def keep_alive():
    t = Thread(target=run)
    t.start()
