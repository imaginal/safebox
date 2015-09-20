# -*- coding: utf-8 -*-


from flask import *
from flask_peewee.utils import get_object_or_404

from app import app
from models import *


@app.route('/favicon.ico')
def favicon():
    return send_file("static/img/favicon.png", cache_timeout=86400)


@app.route('/')
def main(template_name="main.html"):
    return render_template(template_name)


@app.route('/frame')
def frame(template_name="frame.html"):
    return render_template(template_name)

