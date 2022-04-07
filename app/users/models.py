# author:windy
# datetime:2022/3/3 11:22 AM
# software: PyCharm
# 定义的用户名和密码两个内容。还增加了按用户名查找用户的方法、生成密码和验证密码的方法

from app import db
from passlib.hash import pbkdf2_sha256 as sha256
from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields


class User(db.Model):
    __tablename__ = 'users'

    USER_NO = db.Column(db.Integer, primary_key=True)
    USER_NAME = db.Column(db.String(120), unique=True, nullable=False)
    PASSWORD = db.Column(db.String(120), nullable=False)

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
