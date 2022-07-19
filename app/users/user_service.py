# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/7/18 19:59
# @File    : user_service.py

from app.users.user_public_util import get_verify_code
from app.users.user_public_util import get_expire_time
from app.users.models import UserVerifyCode


def send_mobile_verify_code(req):
    code = get_verify_code(code_len=6)
    mobile = req["mobile"]
    code_expire_time = get_expire_time()
    UserVerifyCode.insert(MOBILE=mobile,
                          VERIFY_CODE=code,
                          EXPIRES_TIME=code_expire_time)
    # UserVerifyCode.update()
    return {'code': '00000'}


def check_mobile_verify_code(req):
    mobile = req["mobile"]


def register_user(req):
    pass
