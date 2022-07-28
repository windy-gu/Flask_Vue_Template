# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/4/11 11:31
# @File    : author_service.py
from app.author.dao import author_dao
from app.author.models import Author
from app.utils.responses import response_with
from app.utils import responses as resp


def author_list(req):
    try:
        return author_dao.select_authors_by_pagination(**req)
    except Exception as e:
        return response_with(resp.SQL_Execute_Error_10004, value={'Exception': 'SQL执行出现异常，{}'.format(e)})


def author_list_like(req):
    try:
        # print(type(req))
        return author_dao.select_authors_filter(**req)
    except Exception as e:
        return response_with(resp.SQL_Execute_Error_10004, value={'Exception': 'SQL执行出现异常，{}'.format(e)})


def update_author(req):
    try:
        id = req['id']
        name = req['name']
        pseudonym = req['pseudonym']
        author = Author.filter_by(ID=id).first()
        author.update(NAME=name, PSEUDONYM=pseudonym)
        return response_with(resp.SUCCESS_200, value={'code': '00000'})
    except Exception as e:
        return response_with(resp.SQL_Execute_Error_10004, value={'Exception': 'SQL执行出现异常，{}'.format(e)})


def delete_author(req):
    try:
        id = req['id']
        author = Author.filter_by(ID=id).first()
        author.delete()
        return response_with(resp.SUCCESS_200, value={'code': '00000'})
    except Exception as e:
        return response_with(resp.SQL_Execute_Error_10004, value={'Exception': 'SQL执行出现异常，{}'.format(e)})


def add_author(req):
    try:
        name = req['name']
        pseudonym = req['pseudonym']
        Author.insert(NAME=name, PSEUDONYM=pseudonym)
        return response_with(resp.SUCCESS_200, value={'code': '00000'})
    except Exception as e:
        return response_with(resp.SQL_Execute_Error_10004, value={'Exception': 'SQL执行出现异常，{}'.format(e)})

