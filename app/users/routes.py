# author:windy
# datetime:2022/3/3 11:31 AM
# software: PyCharm

from flask import request
from app.users import user_bp
from app.users.service import user_service


# 注册
@user_bp.route('/register', methods=['POST'])
def create_user():
    return user_service.user_register(request.get_json())


# 登录
@user_bp.route('/login', methods=['POST'])
def login_user():
    return user_service.user_login(request.get_json())


# 查询用户信息
@user_bp.route('/userinfo', methods=['POST'])
def get_user_info():
    return user_service.get_user_info(request.get_json())


# 发送验证码
@user_bp.route('/sendSms', methods=['POST'])
def send_verify_code():
    return user_service.send_mobile_verify_code(request.get_json())


# 查询验证码
@user_bp.route('/checkSmsCode', methods=['POST'])
def check_verify_code():
    return user_service.check_mobile_verify_code(request.get_json())
