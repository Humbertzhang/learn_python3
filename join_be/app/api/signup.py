from . import api
from .. import db
from flask import request
from flask import jsonify
from ..models import User

@api.route('/signup/', methods = ['POST'])
def signup():
    if request.method == 'POST':
        idc = request.get_json().get("idcode")
        
        if idc == None:
            return jsonify({}), 400

        user = User.query.filter_by(idcode = idc).first()
        if user:
            return jsonify({}), 400
        else:
            new_user = User(idcode = idc)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({
                    "idcode":new_user.idcode
                }), 200
