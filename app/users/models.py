# author:windy
# datetime:2022/3/3 11:22 AM
# software: PyCharm
# 定义的用户名和密码两个内容。还增加了按用户名查找用户的方法、生成密码和验证密码的方法

from app.utils.database import BaseColumn
from app.utils.database import DBModel
from app.utils.database import db
from passlib.hash import pbkdf2_sha256 as sha256
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
