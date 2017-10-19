from . import api
from .. import db
from flask import request
from flask import jsonify
from ..models import User

import redis

@api.route('/getrecord/', methods = ['POST'])
def getrecord():
    if request.method == 'POST':
        idcode = request.get_json().get("id")
        conn = redis.StrictRedis(host='localhost',decode_responses=True, port=6379, db=0)

        content = conn.hgetall(str(idcode) + "fin")
        conn.delete(str(idcode) + "fin")
        return jsonify(content)
