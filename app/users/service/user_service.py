# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/7/18 19:59
# @File    : user_service.py

from app.users.user_public_util import get_verify_code
from app.users.user_public_util import get_expire_time
from app.users.user_public_util import generate_hash
from app.users.user_public_util import verify_hash
from app.users.dao import user_dao
from app.common.id_generator import new_id
from app.common.validator import check_is_blank
from app.common.validator import check_is_not_blank
from app.common.exceptions import ServiceError
from app.users.models import User
from app.users.models import UserVerifyCode
from app.utils.responses import response_with
from app.utils import responses as resp

from flask_jwt_extended import create_access_token


def send_mobile_verify_code(req):
    try:
        code = get_verify_code(code_len=6)
        mobile = req["mobile"]
        code_expire_time = get_expire_time()
        UserVerifyCode.insert(MOBILE=mobile,
                              VERIFY_CODE=code,
                              EXPIRES_TIME=code_expire_time)
        return response_with(resp.SUCCESS_200, value={'code': '00000'})
    except Exception as e:
        return response_with(resp.INVALID_FIELD_NAME_SENT_422, value={'Exception': 'SQL执行出现异常，{}'.format(e)})


def check_mobile_verify_code(req):
    try:
        mobile = req["mobile"]
        verify_list = user_dao.select_verify_code_by_mobile(mobile)
        return response_with(resp.SUCCESS_200, value={'code': '00000',
                                                      'verify_code': '{}'.format(verify_list.VERIFY_CODE)})
    except Exception as e:
        return response_with(resp.INVALID_FIELD_NAME_SENT_422, value={'Exception': 'SQL执行出现异常，{}'.format(e)})


def user_register(req):
    try:
        username = req["username"]
        password = generate_hash(req["password"])
        user = user_dao.select_user_info_by_username(username)
        check_is_blank(user, "当前用户已注册")
        user_no = new_id()
        User.insert(USER_NO=user_no,
                    USER_NAME=username,
                    PASSWORD=password)
        return response_with(resp.SUCCESS_200, value={'code': '00000'})
    except ServiceError as e:
        return response_with(resp.INVALID_FIELD_NAME_SENT_422, value={'Exception': '{}'.format(e)})


def user_login(req):
    try:
        username = req["username"]
        password = req["password"]
        user = user_dao.select_user_info_by_username(username)
        check_is_not_blank(user, "账号未注册")
        if verify_hash(password, user.PASSWORD):
            access_token = create_access_token(identity=username)
            user.update(LOGGED_IN=1)
            return response_with(resp.SUCCESS_200, value={'message': 'Logged in as {}'.format(user.USER_NAME),
                                                          'access_token': access_token,
                                                          'name': user.USER_NAME,
                                                          'avatar': user.AVATAR,
                                                          'code': '00000'})
        else:
            raise ServiceError("账号或密码错误")
    except ServiceError as e:
        return response_with(resp.INVALID_FIELD_NAME_SENT_422, value={'Exception': '{}'.format(e)})


def get_user_info(req):
    try:
        username = req["username"]
        user = user_dao.select_user_info_by_username(username)
        check_is_not_blank(user, "当前用户不存在")
        return response_with(resp.SUCCESS_200, value={'code': '00000',
                                                      'avatar': user.AVATAR,
                                                      'name': user.USER_NAME
                                                      })
    except ServiceError as e:
        return response_with(resp.INVALID_FIELD_NAME_SENT_422, value={'Exception': '{}'.format(e)})
