# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/4/11 11:31
# @File    : author_service.py
from app.author.dao import author_dao
from app.author.models import Author
from app.utils.responses import response_with
from app.utils import responses as resp


def get_author_info(req):
    id = req['id']
    author = Author.filter_by(ID=id)
    return response_with(resp.SUCCESS_200, value={'code': '00000'})


def update_author(id, req):
    name = req['name']
    pseudonym = req['pseudonym']
    author = Author.filter_by(ID=id)
    author.update(NAME=name, PSEUDONYM=pseudonym)
    return response_with(resp.SUCCESS_200, value={'code': '00000'})


def delete_author(id):
    Author.delete_filter_by(ID=id)
    return response_with(resp.SUCCESS_200, value={'code': '00000'})


def add_author(req):
    name = req['name']
    pseudonym = req['pseudonym']
    Author.insert(NAME=name, PSEUDONYM=pseudonym)
    return response_with(resp.SUCCESS_200, value={'code': '00000'})



