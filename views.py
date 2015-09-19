# -*- coding: utf-8 -*-


from flask import *
from flask_peewee.utils import get_object_or_404

from app import app
from models import *


@app.route('/favicon.ico')
def favicon():
    return ""


@app.route('/')
def main(template_name="main.html"):
    return render_template(template_name)



