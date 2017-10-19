from . import api
from .. import db
from flask import request
from flask import jsonify
from ..models import User

import redis

@api.route('/finishit/', methods = ['POST'])
def finishit():
    if request.method == 'POST':
        dic = {}
        idcode = request.get_json().get("my_id")
        dic["record"] = request.get_json().get("record")
        dic["score"] = request.get_json().get("score")

        key = str(idcode) + "fin"
        conn = redis.StrictRedis(host='localhost',decode_responses=True, port=6379, db=0)
        conn.hmset(key, dic)
        return jsonify({"status":1})
