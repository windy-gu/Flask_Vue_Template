# author:windy
# datetime:2022/3/3 9:27 AM
# software: PyCharm

from flask import Blueprint
author_bp = Blueprint('author_bp', __name__)

from app.author import routes