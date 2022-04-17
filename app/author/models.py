# author:windy
# datetime:2022/3/3 9:28 AM
# software: PyCharm


from app import db
from app.utils.database import DBModel
from datetime import datetime


class Author(DBModel):
    __tablename__ = 'authors'
    __tabel_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    createTime = db.Column(db.DateTime, server_default=db.func.now())
    updateTime = db.Column(db.DateTime, server_default=db.func.now())
    books = db.relationship('Book', backref='Author', cascade="all, delete-orphan")

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
