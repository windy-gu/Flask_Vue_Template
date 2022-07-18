# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/5/27 18:06
# @File    : user_public_util.py

import random
import time
import datetime


def send_verify_code():

    ...


def get_verify_code(code_len: int = 6):
    code_list = []
    for i in range(code_len):
        code_list.append(str(random.randint(0, 9)))

    return ''.join(code_list)


def get_expire_time():
    """
    获取验证码过期时间
    :return:
    """
    return str(datetime.datetime.now()+datetime.timedelta(minutes=5))


if __name__ == '__main__':
    print(get_verify_code())
    print(str(datetime.datetime.now()+datetime.timedelta(minutes=5)))

