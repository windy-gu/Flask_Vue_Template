# author:windy
# datetime:2022/3/3 11:31 AM
# software: PyCharm

from flask import request
from app.users import user_bp
from app.users.models import User
from app.users.service.user_service import send_mobile_verify_code
from app.users.service.user_service import user_register
from app.users.service.user_service import user_login
from app.utils.responses import response_with
from app.utils import responses as resp


# 注册
@user_bp.route('/register', methods=['POST'])
def create_user():
    return user_register(request.get_json())


# 登录
@user_bp.route('/login', methods=['POST'])
def authenticate_user():
    return user_login(request.get_json())


# 查询用户信息
@user_bp.route('/userinfo', methods=['POST'])
def get_user_info():
    try:
        data = request.get_json()
        # current_user = User.find_by_username(data['username'])
        current_user = User.find_by_username(data['username'])
        if not current_user:
            return response_with(resp.SERVER_ERROR_404)

        else:
            return response_with(resp.SUCCESS_201, value={'avatar': current_user.AVATAR,
                                                          'name': current_user.USER_NAME})

    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


# 发送验证码
@user_bp.route('/sendSms', methods=['POST'])
def send_verify_code():
    return send_mobile_verify_code(request.get_json())


# 查询验证码
@user_bp.route('/checkSmsCode', methods=['POST'])
def check_verify_code():
    try:
        data = request.get_json()
        # current_user = User.find_by_username(data['username'])
        current_user = User.find_by_username(data['username'])
        if not current_user:
            return response_with(resp.SERVER_ERROR_404)

        else:
            return response_with(resp.SUCCESS_201, value={'avatar': current_user.AVATAR,
                                                          'name': current_user.USER_NAME})

    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)
