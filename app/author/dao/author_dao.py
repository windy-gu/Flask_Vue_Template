# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/4/11 11:31
# @File    : author_dao.py
from app.author.models import Author
from app.author.schema import AuthorSchema
from app.utils.responses import response_with
from app.utils import responses as resp
from app.utils.camel_case import list_key_to_lower_camel_case
from app.utils.camel_case import dict_key_to_upper


def select_authors_by_pagination(**kwargs):
    """
    通过pageNum，pageSize查询authors list数据
    :param pageNum:
    :param pageSize:
    :return:
    """
    try:
        if 'pageNum' in kwargs.keys():
            pageNum = kwargs['pageNum']
            del kwargs['pageNum']
        else:
            pageNum = 1
        if 'pageSize' in kwargs.keys():
            pageSize = kwargs['pageSize']
            del kwargs['pageSize']
        else:
            pageSize = 10
        pagination = Author.filter_by(DELETED=0, **dict_key_to_upper(kwargs)).paginate(page=pageNum, per_page=pageSize)
    except Exception as e:
        return response_with(resp.SQL_Execute_Error_10004,
                             value={"responseData": "".format(e)})
    else:
        author_schema = AuthorSchema(many=True, only=['ID', 'NAME', 'PSEUDONYM'])
        authors_list = author_schema.dump(pagination.items)
        return response_with(resp.SUCCESS_200,
                             value={"responseData": list_key_to_lower_camel_case(authors_list)},
                             pagination=pagination)


def select_authors_filter(**kwargs):
    """
    模糊查询
    :param args:
    :return:
    """
    try:
        if 'pageNum' in kwargs.keys():
            pageNum = kwargs['pageNum']
            del kwargs['pageNum']
        else:
            pageNum = 1
        if 'pageSize' in kwargs.keys():
            pageSize = kwargs['pageSize']
            del kwargs['pageSize']
        else:
            pageSize = 10
        temp_dict = dict_key_to_upper(kwargs)
        if 'NAME' not in temp_dict.keys():
            temp_dict['NAME'] = ''
        if 'PSEUDONYM' not in temp_dict.keys():
            temp_dict['PSEUDONYM'] = ''
        select_data = Author.filter(Author.NAME.like('%' + temp_dict['NAME'] + '%'),
                                    Author.PSEUDONYM.like('%' + temp_dict['PSEUDONYM'] + '%'),
                                    Author.DELETED == 0).paginate(page=pageNum, per_page=pageSize)
    except Exception as e:
        return response_with(resp.SQL_Execute_Error_10004,
                             value={"responseData": "".format(e)})
    else:
        author_schema = AuthorSchema(many=True, only=['ID', 'NAME', 'PSEUDONYM'])
        authors_list = author_schema.dump(select_data.items)
        return response_with(resp.SUCCESS_200,
                             value={"responseData": list_key_to_lower_camel_case(authors_list)})

