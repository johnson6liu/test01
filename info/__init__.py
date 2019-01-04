import redis
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,session
from flask_session import Session
from config import Config, config_dict


def create_app(env):
    app = Flask(__name__)

    config_classname = config_dict[env]
    app.config.from_object(config_classname)

    # 创建SQLAlchemy对象
    db = SQLAlchemy(app)

    # 创建redis仓库
    redis_store = redis.StrictRedis(host=config_classname.REDIS_HOST, port=config_classname.REDIS_PORT,db=0)


    # 创建Session对象
    Session(app)
    return app