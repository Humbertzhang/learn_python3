from . import api
from .. import db
from flask import request
from flask import jsonify
from ..models import User

import redis


@api.route('/acceptit/', methods = ['POST'])
def acceptit():
    if request.method == 'POST':
        raiser_id = request.get_json().get("raiser_id")
        accept_id = request.get_json().get("acceptter_id")
        
        conn = redis.StrictRedis(host='localhost',decode_responses=True, port=6379, db=0)
        try:
            content = conn.hgetall(str(raiser_id))
            if content == {}:
                return jsonify({
                    "status":0,
                    "time":0
                })
            time = content["time"]
            content["acceptter_id"] = accept_id
            conn.hmset(str(raiser_id), content)
            return jsonify({
                "status":1,
                "time":time
            })
        except:
            return jsonify({
                "status":0,
                "time":0
            })
