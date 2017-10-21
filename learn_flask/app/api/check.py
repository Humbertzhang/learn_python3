from . import api
from .. import db
from flask import request
from flask import jsonify
from ..models import User

import redis

@api.route('/check/', methods = ['POST'])
def check():
    if request.method == 'POST':
        raiser_id = request.get_json().get("raiser_id")
        conn = redis.StrictRedis(host='localhost',decode_responses=True, port=6379, db=0)
         
        content = conn.hgetall(str(raiser_id))
        if content != {}:
            if str(content["acceptter_id"]) != "0":
                conn.delete(str(raiser_id))
                return jsonify({
                    "status":1,
                    "time":str(content["time"])
                })

        return jsonify({
            "status":0,
            "time":0
        }),404
