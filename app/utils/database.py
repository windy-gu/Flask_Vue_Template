# -*- coding: utf-8 -*-
# @File    : database.py
# @Time    : 2019/11/7 10:57
# @Author  : Windy.Gu

import decimal
from app import db
from typing import Type
from sqlalchemy import func
from .time_util import datetime_now_by_utc8


MODEL = Type[db.Model]


class CRUDMixin:
    """Mixin that adds convenience methods for CRUD (create, read, update, delete) operations"""

    @classmethod
    def insert(cls: MODEL, **kwargs):
        entity = cls(**kwargs)
        entity.submit()

    @classmethod
    def filter(cls: MODEL, *args):
        return cls.query.filter(*args)

    @classmethod
    def filter_by(cls: MODEL, **kwargs):
        return cls.query.filter_by(**kwargs)

    @classmethod
    def count_by(cls: MODEL, **kwargs) -> int:
        return cls.query.session.query(func.count(cls.ID)).filter_by(**kwargs).scalar() or 0

    @classmethod
    def avg_by(cls: MODEL, field, **kwargs) -> decimal.Decimal:
        return cls.query.session.query(func.avg(field)).filter_by(**kwargs).scalar() or 0

    @classmethod
    def delete_filter(cls: MODEL, *args):
        cls.filter(*args).update({cls.DELETED: 1})

    @classmethod
    def delete_filter_by(cls: MODEL, **kwargs):
        cls.filter_by(**kwargs).update({cls.DELETED: 1})

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        self.submit()

    def delete(self):
        """软删除"""
        return self.update(DELETED=1)

    def submit(self):
        """写入数据库但不提交"""
        try:
            db.session.add(self)
            # db.session.flush()
            db.session.commit()
        except Exception as e:
            print(e)


class DBModel(CRUDMixin, db.Model):
    """Base model class that includes CRUD convenience methods"""

    __abstract__ = True

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return str(self.__dict__)


class BaseColumn:

    ID = db.Column(db.Integer, primary_key=True)
    VERSION = db.Column(db.Integer, nullable=False, default=0, comment='版本号')
    # CREATED_BY = db.Column(db.String(64), default=get_userno, comment='创建人')
    CREATED_TIME = db.Column(db.DateTime, default=datetime_now_by_utc8, comment='创建时间')
    # UPDATED_BY = db.Column(db.String(64), default=get_userno, onupdate=get_userno, comment='更新人')
    UPDATED_TIME = db.Column(db.DateTime, default=datetime_now_by_utc8, onupdate=datetime_now_by_utc8, comment='更新时间')
    DELETED = db.Column(db.Integer, nullable=False, default=0, comment='是否为已删除的数据')
    REMARK = db.Column(db.String(64), comment='备注')
