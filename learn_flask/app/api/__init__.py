from flask import Blueprint

api = Blueprint('api', __name__)

from . import signup, hotapps, raiseit, acceptit, check, addapps, getapps, finishit, getrecord
