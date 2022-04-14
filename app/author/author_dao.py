# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/4/11 11:31
# @File    : author_dao.py
from app.author.models import Author
from app.author.schema import AuthorSchema
from app.utils.responses import response_with
from app.utils import responses as resp


def select_authors_by_pagination(pageNum:int=1, pageSize:int=10):
    """
    通过pageNum，pageSize查询authors list数据
    :param pageNum:
    :param pageSize:
    :return:
    """
    pagination = Author.query.paginate(page=pageNum, per_page=pageSize)
    author_schema = AuthorSchema(many=True, only=['first_name', 'last_name', 'id'])
    authors_list = author_schema.dump(pagination.items)
    return response_with(resp.SUCCESS_200,
                         value={"list": authors_list},
                         pagination=pagination)


def update_author_info_by_id():
    pass