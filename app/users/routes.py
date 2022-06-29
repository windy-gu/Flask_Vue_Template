# author:windy
# datetime:2022/3/3 11:31 AM
# software: PyCharm

from flask import request
from flask_jwt_extended import create_access_token
from app import db
from app.users import user_bp
from app.users.models import User
from app.users.schema import UserSchema
from app.utils.responses import response_with
from app.utils import responses as resp


# 注册
@user_bp.route('/register', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        data['password'] = User.generate_hash(data['password'])
        result = User.add_username(**data)
        return response_with(resp.SUCCESS_201)
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


# 登录
@user_bp.route('/login', methods=['POST'])
def authenticate_user():
    try:
        data = request.get_json()
        print(data)
        current_user = User.find_by_username(data['username'])

        if not current_user:
            return response_with(resp.SERVER_ERROR_404)
        if User.verify_hash(data['password'], current_user.PASSWORD):
            access_token = create_access_token(identity=data['username'])
            return response_with(resp.SUCCESS_201, value={'message': 'Logged in as {}'.format(current_user.USER_NAME),
                                                          "access_token": access_token,
                                                          'name': current_user.USER_NAME,
                                                          'avatar': current_user.AVATAR})
        else:
            return response_with(resp.UNAUTHORIZED_401)
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


# 查询用户信息
@user_bp.route('/user/info', methods=['POST'])
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
@user_bp.route('/user/sendSms', methods=['POST'])
def send_verify_code():
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
