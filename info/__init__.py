import logging
from logging.handlers import RotatingFileHandler

import redis
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_session import Session
from config import config_dict

db = SQLAlchemy()
redis_store = None

def create_app(env):
    app = Flask(__name__)

    config_classname = config_dict[env]

    log_level = config_classname.LOG_LV
    log_file(log_level)

    app.config.from_object(config_classname)


    # 创建SQLAlchemy对象

    db.init_app(app)

    # 创建redis仓库
    global redis_store
    redis_store = redis.StrictRedis(host=config_classname.REDIS_HOST, port=config_classname.REDIS_PORT, db=0)

    # 创建Session对象
    Session(app)

    # 注册首页蓝图到app中  #因首页蓝图最后执行渲染到网页,故须其他代码执行完毕才开始,防止代码报错.
    from info.modules.index import index_blu
    app.register_blueprint(index_blu)

    return app


def log_file(lv):
    """记录日志信息"""
    # 设置哪些日志信息等级要被记录
    logging.basicConfig(level=lv)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100,
                                           backupCount=10)  # 若出现FileNotFoundError: [Errno 2] No such file or directory: '/home/python/logs/log'报错,需在Working directory中设置当前文件路径
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)
