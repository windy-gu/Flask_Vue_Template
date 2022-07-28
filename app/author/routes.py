# author:windy
# datetime:2022/3/3 9:28 AM
# software: PyCharm


from flask import request
from app.author import author_bp
from app.author.models import Author
from app.author.schema import AuthorSchema
from app.utils.responses import response_with
from app.utils import responses as resp
from app.author.service import author_service


@author_bp.route('/add', methods=['POST'])
def create_author():
    """
    添加作者信息
    :return:
    """
    return author_service.add_author(request.get_json())


@author_bp.route('/detail/<int:author_id>', methods=['GET'])
def author_detail(author_id):
    fetched = Author.query.get_or_404(author_id)
    author_schema = AuthorSchema()
    author = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"responseData": author})


@author_bp.route('/update', methods=['POST'])
def update_author():
    """
    通过id修改author信息
    :return:
    """
    return author_service.update_author(request.get_json())


@author_bp.route('/delete', methods=['POST'])
def delete_author():
    """
    通过id删除author信息
    :return:
    """
    return author_service.delete_author(request.get_json())


@author_bp.route('/list', methods=['POST'])
def author_list():
    """
    查询author list数据
    :return:
    """
    return author_service.author_list(request.get_json())


@author_bp.route('/list/like', methods=['POST'])
def author_list_like():
    """
    查询author list数据
    :return:
    """
    return author_service.author_list_like(request.get_json())
