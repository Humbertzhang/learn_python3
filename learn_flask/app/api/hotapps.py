import redis
import json
from . import api
from flask import request
from flask import jsonify
from ..models import User

@api.route("/hotapps/", methods = ['GET'])
def hotapps():
    if request.method == 'GET':
        conn = redis.StrictRedis(host='localhost',decode_responses=True, port=6379, db=0)
        ret = conn.hgetall("hotapps")
        ret = json.dumps(ret, ensure_ascii=False)
        return ret, 200
