import redis
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,session
from flask_session import Session
from config import Config

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # 创建SQLAlchemy对象
    db = SQLAlchemy(app)

    # 创建redis仓库
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT,db=0)


    # 创建Session对象
    Session(app)
    return app