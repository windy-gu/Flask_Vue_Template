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
    return author_service.add_author(request.get_json())


@author_bp.route('/list', methods=['GET'])
def authors_all_list():
    fetched = Author.query.all()
    author_schema = AuthorSchema(many=True, only=['first_name', 'last_name', 'id'])
    authors = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"responseData": authors})


@author_bp.route('/list', methods=['POST'])
def authors_list_by_paginate():
    data = request.get_json()
    return author_service.get_authors_info(data)


@author_bp.route('/list/<int:author_id>', methods=['GET'])
def author_list_by_id(author_id):
    fetched = Author.query.get(author_id)
    author_schema = AuthorSchema(only=['first_name', 'last_name', 'id'])
    temp_data = author_schema.dump(fetched)
    if len(temp_data) == 0:
        return response_with(resp.SUCCESS_200, value={"responseData": None})
    else:
        authors = []
        authors.append(temp_data)
        return response_with(resp.SUCCESS_200, value={"responseData": authors})


@author_bp.route('/detail/<int:author_id>', methods=['GET'])
def author_detail(author_id):
    fetched = Author.query.get_or_404(author_id)
    author_schema = AuthorSchema()
    author = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"responseData": author})


@author_bp.route('/update', methods=['POST'])
def update_author_info():
    """
    通过id修改author信息
    :param id:
    :return:
    """
    return author_service.update_author(request.get_json())


@author_bp.route('/modify/<int:id>', methods=['PATCH'])
def modify_author_detail(id):
    return author_service.update_author(id, request.get_json())


@author_bp.route('/delete', methods=['POST'])
def delete_author():
    return author_service.delete_author(request.get_json())
