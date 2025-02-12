from flask import Blueprint, render_template, make_response
from utils import check_ans, GET_COOKIE

web_bp = Blueprint('web', __name__)

@web_bp.route("/")
def index():
     return render_template("1.htm")

@web_bp.route("/2")
def playground():
     resp = make_response('CTF Flag cookie has been set!')
     FLAG = GET_COOKIE()
     print(FLAG)
     resp.set_cookie('flag_challenge', FLAG, max_age=60*60*24)
     return render_template("2.htm")

@web_bp.route("/3")
def playground2():
     return render_template("3.htm")