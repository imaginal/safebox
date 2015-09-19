# -*- coding: utf-8 -*-

from datetime import datetime
from flask_peewee.auth import BaseUser
from peewee import *

from app import db


class User(db.Model, BaseUser):
    username = CharField(unique=True)
    password = CharField()
    join_date = DateTimeField(default=datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)
    email = property(lambda x: x.username)

    def __unicode__(self):
        return self.username


def create_tables(create_admin_user=False):
    models = [User]
    for cls in models:
        cls.create_table()
    if create_admin_user:
        user = User(username='admin', admin=True)
        user.set_password('admin')
        user.save()
