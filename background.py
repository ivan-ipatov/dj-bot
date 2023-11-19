import os
from flask import Flask, render_template
from threading import Thread
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from admin.order_toggle_func import get_toggle_true_order
from admin.toggle_func import get_toggle_true

# Fetch the service account key JSON file contents
cred = credentials.Certificate('botdb.json')

# Initialize the app with a service account, granting admin privileges
fb_app = firebase_admin.initialize_app(cred, {
    'databaseURL': os.environ['DB_URL']
})

app = Flask('')


@app.route('/')
def home():
    return render_template('home.html', toggle=get_toggle_true(), toggle_order=get_toggle_true_order(), dj_name=str(db.reference('dj-name').get()))


def run():
    app.run(host='0.0.0.0', port=80)


def keep_alive():
    t = Thread(target=run)
    t.start()
