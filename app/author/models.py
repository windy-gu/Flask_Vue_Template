# author:windy
# datetime:2022/3/3 9:28 AM
# software: PyCharm


from app import db
from app.utils.database import DBModel
from datetime import datetime
from app.utils.time_util import datetime_now_by_utc8

class Author(DBModel):
    __tablename__ = 'AUTHORS_INFO'
    __tabel_args__ = {'extend_existing': True}
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    FIRST_NAME = db.Column(db.String(20))
    LAST_NAME = db.Column(db.String(20))
    CREATED_TIME = db.Column(db.DateTime, default=datetime_now_by_utc8, comment='创建时间')
    UPDATED_TIME = db.Column(db.DateTime, default=datetime_now_by_utc8, onupdate=datetime_now_by_utc8, comment='更新时间')
    BOOKS = db.relationship('Book', backref='Author', cascade="all, delete-orphan")

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # self.time = time

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def add_author(cls, first_name, last_name):
      """
      add by myself
      :param first_name:
      :param last_name:
      :return:
      """
      add_author_data = Author(first_name=first_name, last_name=last_name)
      return cls.create(add_author_data)
