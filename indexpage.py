from createDB import get_db
from flask import(Blueprint,g,jsonify,request,make_response)

bp=Blueprint('index',__name__)

@bp.route('/haha',methods=('GET','POST'))
def anything():
    return jsonify('wowowwowowowo')