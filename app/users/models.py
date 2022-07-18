# author:windy
# datetime:2022/3/3 11:22 AM
# software: PyCharm
# 定义的用户名和密码两个内容。还增加了按用户名查找用户的方法、生成密码和验证密码的方法

from app.utils.database import BaseColumn
from app.utils.database import DBModel
from app.utils.database import db
from passlib.hash import pbkdf2_sha256 as sha256
from app.utils.time_util import datetime_now_by_utc8
from app.users.user_public_util import *
from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields


class User(DBModel, BaseColumn):
    __tablename__ = 'users'

    USER_NO = db.Column(db.Integer, primary_key=True, index=True, unique=True, nullable=False, comment='用户编号')
    USER_NAME = db.Column(db.String(128), unique=True, nullable=False, comment='用户名称')
    PASSWORD = db.Column(db.String(256), nullable=False, comment='用户密码')
    MOBILE_NO = db.Column(db.String(16), comment='手机号')
    EMAIL = db.Column(db.String(128), comment='邮箱')
    AVATAR = db.Column(db.String(256), comment='头像URL')
    STATE = db.Column(db.String(16), nullable=False, default='ENABLE', comment='用户状态(ENABLE:启用, CLOSE:禁用)')
    LOGGED_IN = db.Column(db.Boolean, nullable=False, default=False, comment='是否已登录')

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def add_username(cls, username, password):
        """
        add by myself
        :param username:
        :param password:
        :return:
        """
        add_user_data = User(USER_NAME=username, PASSWORD=password)
        return cls.create(add_user_data)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(USER_NAME=username).first()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        print(password)
        print(hash)
        return sha256.verify(password, hash)


class UserVerifyCode(DBModel):
    __tablename__ = 'USER_OPERATOR_VERIFY_CODE'
    ID = db.Column(db.Integer, primary_key=True)
    MOBILE = db.Column(db.String(64), comment='登录手机号')
    VERIFY_CODE = db.Column(db.String(64), comment='验证码')
    BIZ_ID = db.Column(db.String(64), comment='业务ID')
    EXPIRES_TIME = db.Column(db.DateTime,  comment='过期时间')
    IS_USED = db.Column(db.Integer, default=0, comment='是否使用(0：未使用；1：已使用)')
    MAX_TIMES = db.Column(db.Integer, default=5, comment='最多重试次数')
    VERSION = db.Column(db.Integer, nullable=False, default=0, comment='版本号')
    CREATED_TIME = db.Column(db.DateTime, default=datetime_now_by_utc8, comment='创建时间')
    UPDATED_TIME = db.Column(db.DateTime, default=datetime_now_by_utc8, onupdate=datetime_now_by_utc8, comment='更新时间')
    REMARK = db.Column(db.String(64), comment='备注')

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def create_verify_code(cls, phone: str):
        phone_no = phone
        code = get_verify_code()
        expire_time = get_expire_time()
        add_verify_code = UserVerifyCode(MOBILE=phone_no, VERIFY_CODE=code, EXPIRES_TIME=expire_time)
        return cls.submit(add_verify_code)


class T_USERS(db.Model):
    __tablename__ = 't_users'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True, nullable=False, comment='用户id')
    name = db.Column(db.String(128), unique=True, nullable=False, comment='用户名称')
    department_id = db.Column(db.String(256), nullable=False, comment='部门id')
    owner = db.Column(db.String(256), comment='技能')


class T_Department(db.Model):
    __tablename__ = 't_department'
    id = db.Column(db.Integer, primary_key=True, comment='部门编号id')
    department = db.Column(db.String(64), comment='部门名称')




