# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/4/11 11:31
# @File    : author_dao.py
from app.author.models import Author
from app.author.schema import AuthorSchema
from app.utils.responses import response_with
from app.utils import responses as resp


def select_authors_by_pagination(pageNum: int=1, pageSize: int=10):
    """
    通过pageNum，pageSize查询authors list数据
    :param pageNum:
    :param pageSize:
    :return:
    """
    try:
        pagination = Author.query.paginate(page=pageNum, per_page=pageSize)
        print(pagination.items)
    except Exception as e:
        return response_with(resp.SUCCESS_200,
                             value={"responseData": "".format(e)})
    else:
        author_schema = AuthorSchema(many=True, only=['ID', 'NAME', 'PSEUDONYM'])
        authors_list = author_schema.dump(pagination.items)
        return response_with(resp.SUCCESS_200,
                             value={"responseData": authors_list},
                             pagination=pagination)
