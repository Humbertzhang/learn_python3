from . import api
from .. import db
from flask import request
from flask import jsonify
from ..models import User

import redis

@api.route('/raiseit/', methods = ['POST'])
def raiseit():
    if request.method == 'POST':
        raiser_id = request.get_json().get("raiser_id")
        time = request.get_json().get("time")
        dic = {}
        dic["raiser_id"] = raiser_id
        dic["acceptter_id"] = 0
        dic["time"] = time
        try:
            conn = redis.StrictRedis(host='localhost',decode_responses=True, port=6379, db=0)
            content = conn.hgetall(str(raiser_id))
            
            #if content is not {}:
            #    return jsonify({
            #        "status":0
            #    })
            
            conn.hmset(str(raiser_id), dic)
            return jsonify({
                "status":1
            })
        except:
            return jsonify({
                "status":0
            })
