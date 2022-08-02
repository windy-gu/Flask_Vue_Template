# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/8/1 09:50
# @File    : requests_server.py
import requests
import json
# from flask import request


def api_request_service():
    # request.method()
    # requests.request()
    ...


class Requests():

    def get(self, url, **kwargs):
        return self.request(method='GET', url=url, **kwargs)

    def post(self, url, body, **kwargs):
        return self.request(method='POST', url=url, json=body, **kwargs)

    def put(self, url, **kwargs):
        return self.request(method='PUT', url=url, **kwargs)

    def options(self, url, **kwargs):
        return self.request(method='OPTIONS', url=url, **kwargs)

    def patch(self, url, **kwargs):
        return self.request(method='PATCH', url=url, **kwargs)

    def head(self, url, **kwargs):
        return self.request(method='HEAD', url=url, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(method='DELETE', url=url, **kwargs)

    def request(self, method, url, **kwargs):
        """

        :param method: method for the new :`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``,
                                           ``PATCH``, or ``DELETE``
        :param url: request url
        :param kwargs:
        :return:
        """
        response_text = requests.request(method=method, url=url, **kwargs)
        response_headers = response_text.headers
        response_body = response_text.content.decode('unicode_escape')
        return response_headers, response_body


if __name__ == '__main__':
    # test_req = Requests()
    #
    # headers = {
    #     'Content-type': 'application/json',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;'
    #                   ' x64) AppleWebKit/537.36 (KHTML, like'
    #                   ' Gecko) Chrome/89.0.4389.90 Safari/537.36',
    # }
    # test_body = {"pageNum": 1, "pageSize": 5, "name": "杨振东"}
    # test_url = 'http://127.0.0.1:5001/api/author/list'
    # header, body = test_req.post(url=test_url, json=test_body, headers=headers)
    test_add = "{\n  \"responseData\": [\n    {\n      \"id\": 3.0, \n      \"name\": \"杨振东\", \n      \"pseudonym\": \"辰东\"\n    }\n  ], \n  \"rspInf\": \"success\"\n}\n"
    test_2 = test_add.replace('\n', '').replace(' ', '')
    print(test_2)

    # print(header, body)

