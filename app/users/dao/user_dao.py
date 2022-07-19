# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/7/18 20:00
# @File    : user_dao.py

from app.users.models import User
from app.users.models import UserVerifyCode


def select_by_username(user_name) -> User:
    return User.filter_by(USER_NAME=user_name).first()
