# -*- coding: utf-8 -*-

from datetime import datetime
from flask_peewee.auth import BaseUser
from peewee import *

from app import db


class AdminUser(db.Model, BaseUser):
    username = CharField(unique=True)
    password = CharField()
    join_date = DateTimeField(default=datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)
    email = property(lambda x: x.username)

    def __unicode__(self):
        return self.username


class User(db.Model):
    mobile = CharField(unique=True)
    full_name = CharField()
    birth_date = DateField()
    pin_code = CharField()
    join_date = DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.mobile


class Travel(db.Model):
    user = ForeignKeyField(User)
    country = CharField()
    address = CharField()
    arrival_date = DateTimeField()
    departure_date = DateTimeField()

    def __unicode__(self):
        return self.country


class Document(db.Model):
    user = ForeignKeyField(User)
    name = CharField()
    filename = CharField()
    password = CharField()
    create_date = DateTimeField(default=datetime.now)
    delete_date = DateTimeField(null=True)

    def __unicode__(self):
        return self.name


def create_tables(create_admin_user=False):
    models = [AdminUser, User, Travel, Document]
    for cls in models:
        cls.create_table()
    if create_admin_user:
        user = AdminUser(username='admin', admin=True)
        user.set_password('adminadmin')
        user.save()
