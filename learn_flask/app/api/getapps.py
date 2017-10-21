from . import api
from .. import db
from flask import request, abort
from flask import jsonify
from ..models import User

import redis

@api.route('/getapps/', methods = ['POST'])
def getapps():
    if request.method == 'POST':
        idcode = request.get_json().get("id")
        conn = redis.StrictRedis(host='localhost',decode_responses=True, port=6379, db=0)
        content = conn.hgetall(str(idcode)+"app")
        if content == {}:
            abort(404)
        else:
            conn.delete(idcode+"app")
            return jsonify(content)
