# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/7/18 20:00
# @File    : user_dao.py

from app.users.models import User
from app.users.models import UserVerifyCode


def select_user_info_by_username(user_name: str) -> User:
    return User.filter_by(USER_NAME=user_name).first()


def select_verify_code_by_mobile(mobile: str) -> UserVerifyCode:
    """通过id倒序查询出最近的一条数据"""
    return UserVerifyCode.filter_by(MOBILE=mobile).order_by(UserVerifyCode.ID.desc()).first()
