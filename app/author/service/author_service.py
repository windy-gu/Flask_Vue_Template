# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/4/11 11:31
# @File    : author_service.py
from app.author.dao import author_dao
from app.author.models import Author
from app.utils.responses import response_with
from app.utils import responses as resp


def author_list(req, pageNum: int=1, pageSize: int=10):
    try:
        if 'pageNum' in req:
            pageNum = req['pageNum']
        if 'pageSize' in req:
            pageSize = req['pageSize']
        return author_dao.select_authors_by_pagination(pageNum=pageNum, pageSize=pageSize)
    except Exception as e:
        return response_with(resp.INVALID_FIELD_NAME_SENT_422, value={'Exception': 'SQL执行出现异常，{}'.format(e)})


def update_author(req):
    try:
        id = req['id']
        name = req['name']
        pseudonym = req['pseudonym']
        author = Author.filter_by(ID=id).first()
        author.update(NAME=name, PSEUDONYM=pseudonym)
        return response_with(resp.SUCCESS_200, value={'code': '00000'})
    except Exception as e:
        return response_with(resp.INVALID_FIELD_NAME_SENT_422, value={'Exception': 'SQL执行出现异常，{}'.format(e)})


def delete_author(req):
    try:
        id = req['id']
        author = Author.filter_by(ID=id).first()
        author.delete()
        return response_with(resp.SUCCESS_200, value={'code': '00000'})
    except Exception as e:
        return response_with(resp.INVALID_FIELD_NAME_SENT_422, value={'Exception': 'SQL执行出现异常，{}'.format(e)})


def add_author(req):
    try:
        name = req['name']
        pseudonym = req['pseudonym']
        Author.insert(NAME=name, PSEUDONYM=pseudonym)
        return response_with(resp.SUCCESS_200, value={'code': '00000'})
    except Exception as e:
        return response_with(resp.INVALID_FIELD_NAME_SENT_422, value={'Exception': 'SQL执行出现异常，{}'.format(e)})

