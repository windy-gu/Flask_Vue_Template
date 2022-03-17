# author:windy
# datetime:2022/3/3 9:29 AM
# software: PyCharm
# 自定义了程序出现错误是的错误信息，统一的接口响应处理程序

from flask import make_response, jsonify

INVALID_FIELD_NAME_SENT_422 = {
    "http_code": 422,
    "rspInf": "invalidField",
    "message": "Invalid fields found"
}

INVALID_INPUT_422 = {
    "http_code": 422,
    "rspInf": "invalidInput",
    "message": "Invalid input"
}

MISSING_PARAMETERS_422 = {
    "http_code": 422,
    "rspInf": "missingParameter",
    "message": "Missing parameters."
}

BAD_REQUEST_400 = {
    "http_code": 400,
    "rspInf": "badRequest",
    "message": "Bad request"
}

SERVER_ERROR_500 = {
    "http_code": 500,
    "rspInf": "serverError",
    "message": "Server error"
}

SERVER_ERROR_404 = {
    "http_code": 404,
    "rspInf": "notFound",
    "message": "Resource not found"
}

FORBIDDEN_403 = {
    "http_code": 403,
    "rspInf": "notAuthorized",
    "message": "You are not authorised to execute this."
}
UNAUTHORIZED_401 = {
    "http_code": 401,
    "rspInf": "notAuthorized",
    "message": "Invalid authentication."
}

NOT_FOUND_HANDLER_404 = {
    "http_code": 404,
    "rspInf": "notFound",
    "message": "route not found"
}

SUCCESS_200 = {
    'http_code': 200,
    'rspInf': 'success'
}

SUCCESS_201 = {
    'http_code': 201,
    'rspInf': 'success'
}

SUCCESS_204 = {
    'http_code': 204,
    'rspInf': 'success'
}

# {
#     "rspInf": "success",
#     "data": null,
#     "v": "1",
#     "responseTm": "20220316202326",
#     "rspCd": "00000",
#     "rspType": 0
# }


def response_with(response, value=None, message=None, error=None, headers={}, pagination=None):
    result = {}
    if value is not None:
        result.update(value)

    if response.get('message', None) is not None:
        result.update({'message': response['message']})

    result.update({'rspInf': response['rspInf']})

    if error is not None:
        result.update({'errors': error})

    if pagination is not None:
        result.update({'pagination': pagination})

    headers.update({'Access-Control-Allow-Origin': '*'})
    headers.update({'server': 'Flask REST API'})

    return make_response(jsonify(result), response['http_code'], headers)
