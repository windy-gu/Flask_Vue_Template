# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/7/25 20:56
# @File    : camel_case.py

import re


def to_camel_case(x):
    """转驼峰法命名"""
    return re.sub('_([a-zA-Z])', lambda m: (m.group(1).upper()), x)


def to_upper_camel_case(x):
    """转大驼峰法命名"""
    s = re.sub('_([a-zA-Z])', lambda m: (m.group(1).upper()), x)
    return s[0].upper() + s[1:]


def to_lower_camel_case(x):
    """转小驼峰法命名"""
    s = re.sub('_([a-zA-Z])', lambda m: (m.group(1).upper()), x)
    return s[0].lower() + s[1:]


def key_to_lower_camel_case(parameter_list: list):
    """
    将返回的参数key进行小驼峰法转换
    :param parameter_list:
    :return:
    """
    target_list = []
    for i in range(len(parameter_list)):
        temp_dict = {}
        for k, v in parameter_list[i].items():
            # print(k, v)
            k_result = to_lower_camel_case(k.lower())
            temp_dict[k_result] = v
        target_list.append(temp_dict)
    return target_list