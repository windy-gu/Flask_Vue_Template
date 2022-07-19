# author:windy
# datetime:2022/3/3 9:28 AM
# software: PyCharm


from app import db
from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields
from app.utils.time_util import datetime_now_by_utc8


class Book(db.Model):
    __tablename__ = 'BOOKS_INFO'

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    AUTHOR_ID = db.Column(db.Integer, db.ForeignKey('AUTHORS_INFO.ID'))
    BOOK_NAME = db.Column(db.String(50))
    PUBLICATION_TIME = db.Column(db.Integer)
    CREATED_TIME = db.Column(db.DateTime, default=datetime_now_by_utc8, comment='创建时间')
    UPDATED_TIME = db.Column(db.DateTime, default=datetime_now_by_utc8, onupdate=datetime_now_by_utc8, comment='更新时间')

    def __init__(self, book_name, publication_time, author_id=None):
        self.book_name = book_name
        self.publication_time = publication_time
        self.author_id = author_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
