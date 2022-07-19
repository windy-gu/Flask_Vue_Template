# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/7/19 14:34
# @File    : validator.py
from app.common.exceptions import ServiceError


def check_is_blank(obj: any, error_msg: str = 'Validation failed'):
    """
    检查obj对象是否为空，不为空则抛异常
    :param obj:
    :param error_msg:
    :return:
    """
    if obj:
        raise ServiceError(msg=error_msg)


def check_is_not_blank(obj: any, error_msg: str = 'Validation failed'):
    """
    检查obj对象是否为空，为空则抛异常
    :param obj:
    :param error_msg:
    :return:
    """
    if not obj:
        raise ServiceError(msg=error_msg)
