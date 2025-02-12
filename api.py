from flask import Blueprint, jsonify, request, make_response
from utils import check_ans, GET_COOKIE, GET_SITEMAP_FLAG

api_bp = Blueprint('api', __name__)

@api_bp.route("/check_answer/1",methods=['POST'])
def check_answer_1():
     data = request.get_json()
     correct_answer = check_ans("./onsite/answer.txt")
     correct_answer = correct_answer.replace('\n', '')
     value = data.get("key")
     response = "correct" if value == correct_answer else "incorrect"
     return jsonify({'message': 'Received', 'value': response})

@api_bp.route("/check_answer/2",methods=['POST'])
def check_answer_2():
     data = request.get_json()
     correct_answer = check_ans("./onsite/answer.txt",opt=2)
     correct_answer = correct_answer.replace('\n', '')
     value = data.get("key")
     response = "correct" if value == correct_answer else "incorrect"
     return jsonify({'message': 'Received', 'value': response})

@api_bp.route("/check_answer/3",methods=['POST'])
def check_answer_3():
     data = request.get_json()
     correct_answer = check_ans("./onsite/answer.txt",opt=3)
     correct_answer = correct_answer.replace('\n', '')
     value = data.get("key")
     response = "correct" if value == correct_answer else "incorrect"
     return jsonify({'message': 'Received', 'value': response})

@api_bp.route("/check_answer/4",methods=['POST'])
def check_answer_4():
     data = request.get_json()
     correct_answer = check_ans("./onsite/answer.txt",opt=4)
     correct_answer = correct_answer.replace('\n', '')
     value = data.get("key")
     response = "correct" if value == correct_answer else "incorrect"
     return jsonify({'message': 'Received', 'value': response})

@api_bp.route('/set-cookie')
def set_cookie():
    response = make_response('CTF Flag cookie has been set!')
    FLAG = GET_COOKIE()
    response.set_cookie('flag',FLAG, max_age=60*60*24)
    return response

@api_bp.route("/flag")
def sitemap_flag():
     data = GET_SITEMAP_FLAG()
     return {"flag":data}