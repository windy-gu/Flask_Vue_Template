# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/5/27 18:06
# @File    : user_public_util.py

import random
import datetime
from passlib.hash import pbkdf2_sha256 as sha256


def get_verify_code(code_len: int = 6):
    """
    获取验证码
    :param code_len: 默认值 长度 6位
    :return:
    """
    code_list = []
    for i in range(code_len):
        code_list.append(str(random.randint(0, 9)))

    return ''.join(code_list)


def get_expire_time(expired_time: int = 5):
    """
    获取验证码过期时间
    :param expired_time: 默认值 5分钟
    :return:
    """
    return str(datetime.datetime.now()+datetime.timedelta(minutes=expired_time))


def generate_hash(password: str):
    """
    通过明文密码生成密文密码
    :param password:    明文密码
    :return:            密文密码
    """
    return sha256.hash(password)


def verify_hash(password, hash):
    """
    通过明文密码和密文密码，验证是否一致
    :param password:
    :param hash:
    :return:
    """
    return sha256.verify(password, hash)


if __name__ == '__main__':
    print(get_verify_code())
    print(str(datetime.datetime.now()+datetime.timedelta(minutes=5)))
