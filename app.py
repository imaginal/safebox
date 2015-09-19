# -*- coding: utf-8 -*-

from flask import Flask
from flask_peewee.db import Database
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.config.from_object('config');
app.wsgi_app = ProxyFix(app.wsgi_app)

db = Database(app)
