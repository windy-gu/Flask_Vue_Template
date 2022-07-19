# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/7/19 11:33
# @File    : id_generator.py

from app.utils.snowflake import IdWorker

__ID_WORKER__ = IdWorker(datacenter_id=1, worker_id=1, sequence=1)

# datacenter.id = 1
# worker.id = 1
# sequence = 1


def new_id():
    """
    生成编号
    :return:
    """
    return str(__ID_WORKER__.new_id())
