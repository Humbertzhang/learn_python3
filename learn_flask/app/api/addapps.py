from . import api
from .. import db
from flask import request
from flask import jsonify
from ..models import User

import redis

@api.route('/addapps/', methods = ['POST'])
def addapps():
    if request.method == 'POST':
        dic = {}
        try: 
            dic["idcode"] = request.get_json().get("id")
            dic["ifmodify"] = request.get_json().get("ifmodify")
            dic["apps"] = request.get_json().get("apps")
            key = str(dic["idcode"]) + "app"

            conn = redis.StrictRedis(host='localhost',decode_responses=True, port=6379, db=0)
            conn.hmset(key, dic)
            return jsonify({
                "status":1
            })
        except:
            return jsonify({
                "status":0
            })
