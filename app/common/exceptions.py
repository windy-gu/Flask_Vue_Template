# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/7/19 14:44
# @File    : exceptions.py


class ServiceError(Exception):
    """
    业务异常类
    """

    def __init__(self, msg=None):
        # super().__init__(self)
        self.message = msg
        # self.code = code

    def __str__(self):
        return self.message


class ParseError(Exception):
    """请求参数解析异常类"""

    def __init__(self, msg=None):
        self.message = msg
