from flask import current_app
from flask import session

from info import redis_store
from . import index_blu
from flask import render_template

@index_blu.route("/")
def index():
    redis_store.set("name", "python")

    session["age"] = 28
    return render_template("news/index.html")

@index_blu.route("/favicon.ico")
def get_web_icon():
    """处理窗口小图标的请求"""
    return current_app.send_static_file("news/favicon.ico")