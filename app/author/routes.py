# author:windy
# datetime:2022/3/3 9:28 AM
# software: PyCharm


from flask import request
from app import db
from app.author import author_bp
from app.author.models import Author
from app.author.schema import AuthorSchema
from app.utils.responses import response_with
from app.utils import responses as resp
from app.author.author_service import get_authors_info
from app.author.author_service import update_author_info


@author_bp.route('/add', methods=['POST'])
def create_author():
    try:
        data = request.get_json()
        print(data)
        result = Author.add_author(**data)
        # author_schema = AuthorSchema()
        # author = author_schema.load(data)
        # result = author_schema.dump(author.create())
        return response_with(resp.SUCCESS_201)
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@author_bp.route('/list', methods=['GET'])
def get_authors_all_list():
    fetched = Author.query.all()
    author_schema = AuthorSchema(many=True, only=['first_name', 'last_name', 'id'])
    authors = author_schema.dump(fetched)
    print(authors)
    print(type(authors))
    return response_with(resp.SUCCESS_200, value={"responseData": authors})


@author_bp.route('/list', methods=['POST'])
def get_authors_list_by_paginate():
    data = request.get_json()
    return get_authors_info(data)


@author_bp.route('/list/<int:author_id>', methods=['GET'])
def get_author_list_by_id(author_id):
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
def get_author_detail(author_id):
    fetched = Author.query.get_or_404(author_id)
    author_schema = AuthorSchema()
    author = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"responseData": author})


# @author_bp.route('/update/<int:id>', methods=['PUT'])
# def update_author_info(id):
#     data = request.get_json()
#     get_author = Author.query.get_or_404(id)
#     get_author.first_name = data['first_name']
#     get_author.last_name = data['last_name']
#     db.session.add(get_author)
#     db.session.commit()
#     author_schema = AuthorSchema()
#     author = author_schema.dump(get_author)
#     return response_with(resp.SUCCESS_200, value={"responseData": author})


@author_bp.route('/update/<int:id>', methods=['POST'])
def update_author_info_by_id(id):
    """
    通过id修改author信息
    :param id:
    :return:
    """
    data = request.get_json()
    return update_author_info(id=id, request_body=data)


@author_bp.route('/modify/<int:id>', methods=['PATCH'])
def modify_author_detail(id):
    data = request.get_json()
    get_author = Author.query.get(id)
    if data.get('first_name'):
        get_author.first_name = data['first_name']
    if data.get('last_name'):
        get_author.last_name = data['last_name']

    db.session.add(get_author)
    db.session.commit()
    author_schema = AuthorSchema()
    author = author_schema.dump(get_author)
    return response_with(resp.SUCCESS_200, value={"responseData": author})


@author_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_author(id):
    get_author = Author.query.get_or_404(id)
    db.session.delete(get_author)
    db.session.commit()
    return response_with(resp.SUCCESS_200)
