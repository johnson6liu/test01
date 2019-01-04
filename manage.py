import redis
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,session
from flask_session import Session

app = Flask(__name__)

class Config(object):
    DEBUG = True
    SECRET_KEY = "$*&&$$#$%&&u*"

    # mysql数据库相关配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:Aa201810@127.0.0.1:3306/test01"  # mysql数据库链接地址
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 设置不跟踪数据库的修改

    # redis数据库配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # 配置session信息
    SESSION_TYPE = "redis" # 存储类型
    SESSION_KEY_PREFIX = "Session:" # 设置前缀
    SESSION_USE_SIGNER = True  # 签名存储
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT) # 制定存储位置
    PERMANENT_SESSION_LIFETIME = 3600 * 24 * 2  # 设置session两天有效

app.config.from_object(Config)

# 创建SQLAlchemy对象
db = SQLAlchemy(app)

# 创建redis仓库
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT,db=0)


# 创建Session对象
Session(app)


@app.route("/")
def index():
    redis_store.set("name", "python")

    session["age"] = 28
    return "666"


if __name__ == '__main__':
    app.run()