# -*- coding: utf-8 -*-

from datetime import datetime

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


@app.route('/signup', methods=['POST'])
def signup():
    mobile = request.form['MobileNumber1']
    birth_date = request.form['BirthDate1']
    birth_date = datetime.strptime(birth_date)
    pin_code = request.form['PinCode1']
    try:
        user = User.get(User.mobile==mobile)
    except:
        user = User(mobile=mobile,
            birth_date=birth_date,
            pin_code=pin_code)
        user.save()
    if user.pin_code == pin_code:
        session['uid'] = user.id
        return redirect('/docs')
    return redirect('/')


@app.route('/docs')
def docs(template_name="docs.html"):
    user_id = session.get('uid')
    if not user_id:
        return redirect('/')
    user = User.get(User.id == user_id)
    travels = Travel.select(Travel.user == user)
    documents = Document.select(Document.user == user)
    return render_template(template_name,
        user=user, travels=travels, documents=documents)


