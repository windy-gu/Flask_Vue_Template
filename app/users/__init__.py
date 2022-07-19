# author:windy
# datetime:2022/3/3 11:22 AM
# software: PyCharm

from flask import Blueprint
user_bp = Blueprint('user_bp', __name__)

from app.users import routes