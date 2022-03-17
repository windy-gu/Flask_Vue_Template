# author:windy
# datetime:2022/3/4 11:44 AM
# software: PyCharm

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.users.models import User
from app.users.schema import UserSchema
import os, sys


class Sqlalchemy_MySQL:
    def __init__(self, user: str = 'root', password: str = 'gxf4843860',
                 host: str = 'localhost', port: int = 3306, database: str = 'Test_CMS_SYSTEM'):
        """

                :param user:
                :param password:
                :param host:
                :param port:
                :param database:
                """
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def engine(self, database=None):
        # 初始化数据库连接
        if database is None:
            database = self.database
        engine = create_engine("mysql+pymysql://{root}:{password}@{localhost}:{port}/{database}".
                               format(root=self.user,
                                      password=self.password,
                                      localhost=self.host,
                                      port=self.port,
                                      database=database),
                               encoding="utf-8",
                               echo=True
                               )
        return engine

    def _connect(self, database=None):
        # 初始化数据库连接
        if database is None:
            database = self.database
        engine = create_engine("mysql+pymysql://{root}:{password}@{localhost}:{port}/{database}".
                               format(root=self.user,
                                      password=self.password,
                                      localhost=self.host,
                                      port=self.port,
                                      database=database
                                      ), encoding="utf-8")
        # 创建DBSession类型
        DBSession = sessionmaker(bind=engine)

        # 创建session对象
        session = DBSession()
        return session

    def query_data(self):
        return self._connect()

    def update_data(self):
        return self._connect()


if __name__ == '__main__':
    # mysql_operator = Sqlalchemy_MySQL()
    # user_schema = UserSchema()
    # data = {'username': 'gxf_root', 'password': '123456'}
    # data['password'] = User.generate_hash(data['password'])
    # users = user_schema.load(data)
    # update_session = mysql_operator.update_data()
    # # update_data = User(us)
    # update_session.add(users)
    # update_session.commit()
    print(os.path.dirname(__file__))
    print(os.path.abspath('../dist'))
    print(os.path.abspath('../../dist'))
    print(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    print(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


