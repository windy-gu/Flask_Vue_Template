# author:windy
# datetime:2022/3/3 9:30 AM
# software: PyCharm
# 配置了数据库连接 URI，日志的级别和目录
import os
import logging
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# load env
load_dotenv(os.path.join(basedir, '.flaskenv'))

# log dir
log_dir = os.path.join(basedir, os.getenv('LOG_DIR', 'logs'))


class Config(object):
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///books.db'  # 原本设置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:gxf4843860@localhost:3306/Test_CMS_SYSTEM'   # 自己的本地账号
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    LOG_LEVEL = logging.INFO
    SECRET_KEY = 'HS256'
