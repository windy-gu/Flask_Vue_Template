# author:windy
# datetime:2022/3/3 9:27 AM
# software: PyCharm
# 这部分程序集成了日志、数据库迁移、跨域、blueprint，还有我们编写的 author、books 接口都注册在这里。后续如果有新用到的 Flask 扩展，新开发的接口，都需要来这里进行注册操作

import os
import logging
from logging.handlers import RotatingFileHandler
import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from config import Config, log_dir
from app.utils.log import DayRotatingHandler
from app.utils import responses as resp
from app.utils.responses import response_with

db = SQLAlchemy()
jwt = JWTManager()
cors = CORS()
migrate = Migrate()
marshmallow = Marshmallow()


def create_app(config_class=Config):
    app = Flask(__name__,
                static_folder='/Users/gxf/Documents/code/myself/test/vue-admin-template/dist/static',
                template_folder='/Users/gxf/Documents/code/myself/test/vue-admin-template/dist'
                )
    app.config.from_object(config_class)

    # 注册插件
    register_plugins(app)

    # 注册蓝图
    register_blueprints(app)

    # 注册日志处理器
    register_logging(app)

    # 注册错误处理函数
    register_errors(app)

    app.logger.info('Flask Rest Api startup')
    return app


def register_logging(app):
    app.logger.name = 'flask_api'
    log_level = app.config.get("LOG_LEVEL", logging.INFO)
    cls_handler = logging.StreamHandler()
    log_file = os.path.join(log_dir, datetime.date.today().strftime("%Y-%m-%d.log"))
    file_handler = DayRotatingHandler(log_file, mode="a", encoding="utf-8")

    logging.basicConfig(level=log_level,
                        format="%(asctime)s %(name)s "
                               "%(filename)s[%(lineno)d] %(funcName)s() %(levelname)s: %(message)s",
                        datefmt="%Y/%m/%d %H:%M:%S",
                        handlers=[cls_handler, file_handler])

    if not app.debug and not app.testing:
        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler(os.path.join(log_dir, 'flask_api.log'), maxBytes=1024 * 1024 * 50, backupCount=5, encoding='utf-8')
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(name)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))

            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)


def register_plugins(app):
    cors.init_app(app, supports_credentials=True)
    db.init_app(app)
    jwt.init_app(app)
    marshmallow.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):

    from app.author import author_bp
    app.register_blueprint(author_bp, url_prefix='/api/author')

    from app.books import books_bp
    app.register_blueprint(books_bp, url_prefix='/api/books')

    from app.users import user_bp
    app.register_blueprint(user_bp, url_prefix='/api/user')


def register_errors(app):

    @app.after_request
    def add_header(response):
        return response

    @app.errorhandler(404)
    def not_found(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_404)

    @app.errorhandler(500)
    def server_error(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_500)

    @app.errorhandler(400)
    def bad_request(e):
        logging.error(e)
        return response_with(resp.BAD_REQUEST_400)
