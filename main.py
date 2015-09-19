#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from app import app
from admin import *
from views import *

if not path.exists(app.config['DATABASE']['name']):
    print " * Creating tables"
    from models import create_tables
    with app.app_context():
        create_tables(True)

if __name__ == '__main__':
    app.run()
