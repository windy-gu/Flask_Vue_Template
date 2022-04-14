# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/4/11 11:31
# @File    : author_service.py
from app.author.author_dao import select_authors_by_pagination


def get_authors_info(request_body: dict):
    pageNum = int(request_body['pageNum'])
    pageSize = int(request_body['pageSize'])
    return select_authors_by_pagination(pageNum, pageSize)


def update_author_info(id:int, request_body: dict):
    first_name = request_body['first_name']
    last_name = request_body['first_name']
    pass


