# author:windy
# datetime:2022/3/3 11:22 AM
# software: PyCharm
# 定义的用户名和密码两个内容。还增加了按用户名查找用户的方法、生成密码和验证密码的方法

from app.utils.database import db
from app.utils.database import DBModel
from app.utils.time_util import datetime_now_by_utc8


class Menu(DBModel):
    __tablename__ = 'MENU_INFO'

    ID = db.Column(db.Integer, primary_key=True)
    USER_NO = db.Column(db.String(32), index=True, unique=True, nullable=False, comment='用户编号')
    REDIRECT = db.Column(db.String(128), comment='重定向')
    ALWAYSSHOW = db.Column(db.String(128), comment='动态菜单只有一个子菜单时父级菜单显示不显示这个字段来控制')
    SORT = db.Column(db.String(2), default='0', comment='排序')
    TITLE = db.Column(db.String(128), nullable=False, comment='标题')
    COMPONENT = db.Column(db.String(128), comment='路由路径')
    NAME = db.Column(db.String(256), comment='组件名称')
    PID = db.Column(db.String(32), default='0', comment='上级类目id')
    CREATED_TIME = db.Column(db.DateTime, default=datetime_now_by_utc8, comment='创建时间')
    UPDATED_TIME = db.Column(db.DateTime, default=datetime_now_by_utc8, onupdate=datetime_now_by_utc8, comment='更新时间')
    DELETED = db.Column(db.String(2), nullable=False, default='0', comment='是否为已删除的数据(0:正常, 1:已删除)')
    REMARK = db.Column(db.String(64), comment='备注')



