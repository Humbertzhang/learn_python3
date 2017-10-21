from . import api
from .. import db
from flask import request, abort
from flask import jsonify
from ..models import User

import json
import redis

@api.route('/getrecord/', methods = ['POST'])
def getrecord():
    if request.method == 'POST':
        idcode = request.get_json().get("id")
        conn = redis.StrictRedis(host='localhost',decode_responses=True, port=6379, db=0)

        content = conn.hgetall(str(idcode) + "fin")
        if content == {} :
            abort(404)
        else:
            ret = json.dumps(content, ensure_ascii=False)
            conn.delete(str(idcode) + "fin")
            return ret
