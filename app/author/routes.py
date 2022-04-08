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
    print(data)
    pageNum = int(data['pageNum'])
    pageSize = int(data['pageSize'])
    paginate = Author.query.paginate(page=pageNum, per_page=pageSize)
    paginate_data = paginate.items
    author_schema = AuthorSchema(many=True, only=['first_name', 'last_name', 'id'])
    authors = author_schema.dump(paginate_data)
    pagination = {}
    print(authors)
    print(type(authors))
    return response_with(resp.SUCCESS_200,
                         value={"list": authors,
                                "pages": paginate.pages,
                                "hasNextPage": paginate.has_next,
                                "hasLastPage": paginate.has_prev,
                                "lastPage": paginate.prev_num,
                                "nextPage": paginate.next_num,
                                "total": paginate.total,
                                "pageNum": paginate.page,
                                "pageSize": paginate.per_page})


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


@author_bp.route('/update/<int:id>', methods=['PUT'])
def update_author_detail(id):
    data = request.get_json()
    get_author = Author.query.get_or_404(id)
    get_author.first_name = data['first_name']
    get_author.last_name = data['last_name']
    db.session.add(get_author)
    db.session.commit()
    author_schema = AuthorSchema()
    author = author_schema.dump(get_author)
    return response_with(resp.SUCCESS_200, value={"responseData": author})


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
