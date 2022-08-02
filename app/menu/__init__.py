# author:windy
# datetime:2022/3/3 11:22 AM
# software: PyCharm

from flask import Blueprint
menu_bp = Blueprint('menu_bp', __name__)

from app.users import routes