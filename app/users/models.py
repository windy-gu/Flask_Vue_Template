# author:windy
# datetime:2022/3/3 11:22 AM
# software: PyCharm
# 定义的用户名和密码两个内容。还增加了按用户名查找用户的方法、生成密码和验证密码的方法

from app.utils.database import db
from app.utils.database import DBModel
from app.utils.time_util import datetime_now_by_utc8


class User(DBModel):
    __tablename__ = 'USERS_BASE_INFO'

    ID = db.Column(db.Integer, primary_key=True)
    USER_NO = db.Column(db.String(32), index=True, unique=True, nullable=False, comment='用户编号')
    USER_NAME = db.Column(db.String(128), unique=True, nullable=False, comment='用户名称')
    PASSWORD = db.Column(db.String(256), nullable=False, comment='用户密码')
    MOBILE = db.Column(db.String(16), comment='手机号')
    EMAIL = db.Column(db.String(128), comment='邮箱')
    STATE = db.Column(db.String(16), nullable=False, default='ENABLE', comment='用户状态(ENABLE:启用, CLOSE:禁用)')
    AVATAR = db.Column(db.String(256), comment='头像URL')
    LOGGED_IN = db.Column(db.Boolean, nullable=False, default=False, comment='是否已登录')
    CREATED_TIME = db.Column(db.DateTime, default=datetime_now_by_utc8, comment='创建时间')
    UPDATED_TIME = db.Column(db.DateTime, default=datetime_now_by_utc8, onupdate=datetime_now_by_utc8, comment='更新时间')
    DELETED = db.Column(db.Integer, nullable=False, default=0, comment='是否为已删除的数据')
    REMARK = db.Column(db.String(64), comment='备注')


class UserVerifyCode(DBModel):
    __tablename__ = 'USER_OPERATOR_VERIFY_CODE'
    ID = db.Column(db.Integer, primary_key=True)
    MOBILE = db.Column(db.String(64), comment='登录手机号', nullable=False,)
    VERIFY_CODE = db.Column(db.String(64), comment='验证码', nullable=False,)
    BIZ_ID = db.Column(db.String(64), comment='业务ID')
    EXPIRES_TIME = db.Column(db.DateTime,  comment='过期时间', nullable=False,)
    IS_USED = db.Column(db.Integer, default=0, comment='是否使用(0：未使用；1：已使用)')
    MAX_TIMES = db.Column(db.Integer, default=5, comment='最多重试次数')
    VERSION = db.Column(db.Integer, nullable=False, default=0, comment='版本号')
    CREATED_TIME = db.Column(db.DateTime, default=datetime_now_by_utc8, comment='创建时间')
    UPDATED_TIME = db.Column(db.DateTime, default=datetime_now_by_utc8, onupdate=datetime_now_by_utc8, comment='更新时间')
    REMARK = db.Column(db.String(64), comment='备注')


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
