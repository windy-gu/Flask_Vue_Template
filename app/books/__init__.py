# author:windy
# datetime:2022/3/3 9:27 AM
# software: PyCharm

from flask import Blueprint

books_bp = Blueprint('books_bp', __name__)

from app.books import routes