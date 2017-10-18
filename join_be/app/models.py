# coding:utf-8

"""
sql models
use: Flask-SQLAlchemy
-- http://flask-sqlalchemy.pocoo.org/2.1/
"""

from flask import current_app,request
from . import db, login_manager
from itsdangerous import JSONWebSignatureSerializer as Serializer

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	idcode = db.Column(db.String(164), unique = True, index = True)

