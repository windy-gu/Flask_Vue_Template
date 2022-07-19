# -*- coding: utf-8 -*-
# @Author  : Windy.Gu
# @Software: PyCharm
# @Time    : 2022/7/19 11:21
# @File    : snowflake.py

import logging
import time

"""
Twitter 于 2010 年开源了内部团队在用的一款全局唯一 ID 生成算法 Snowflake
• 最高位占1 bit，值固定为 0，以保证生成的 ID 为正数
• 中位占 41 bit，值为毫秒级时间戳
• 中下位占 10 bit，值为工作机器的 ID，值的上限为 1024
• 末位占 12 bit，值为当前毫秒内生成的不同 ID，值的上限为 4096
"""

"""
WORKER_BITS = 5         # 机器ID
DATACENTER_BITS = 5     # 机房ID
SEQUENCE_BITS = 12      # 序列号
中下位包含 5 位机房ID 和 5 位机器ID，它们一起组成 10 位的中下位。接着通过中下位的长度计算机房和机器的上限值；# 设定设备数量上限
"""

# 64位ID的位数划分
DATACENTER_ID_BITS = 5
WORKER_ID_BITS = 5
SEQUENCE_BITS = 12

# 最大取值
MAX_DATACENTER_ID = -1 ^ (-1 << DATACENTER_ID_BITS)
MAX_WORKER_ID = -1 ^ (-1 << WORKER_ID_BITS)  # 2**5-1 0b11111

# 移位偏移值
DATACENTER_ID_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS
WOKER_ID_SHIFT = SEQUENCE_BITS
TIMESTAMP_LEFT_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS + DATACENTER_ID_BITS

# 序号循环掩码
SEQUENCE_MASK = -1 ^ (-1 << SEQUENCE_BITS)

# Twitter元年时间戳
TWEPOCH = 1288834974657


class InvalidSystemClock(Exception):
    """时钟回拨异常"""
    ...


class IdWorker:
    def __init__(self, datacenter_id, worker_id, sequence=0):
        """

        Args:
            datacenter_id:  数据中心ID
            worker_id:      机器ID
            sequence:       序号号
        """
        # sanity check
        if worker_id > MAX_WORKER_ID or worker_id < 0:
            raise ValueError('worker_id值越界')

        if datacenter_id > MAX_DATACENTER_ID or datacenter_id < 0:
            raise ValueError('datacenter_id值越界')

        self.worker_id = worker_id
        self.datacenter_id = datacenter_id
        self.sequence = sequence

        self.last_timestamp = -1  # 上次计算的时间戳

    def new_id(self):
        """获取新ID"""
        timestamp = int(time.time() * 1000)

        # 时钟回拨
        # 雪花算法需要是强依赖时间，如果时间发生回拨，有可能会生成重复的ID
        # 用当前时间和上一次的时间进行判断，如果当前时间小于上一次的时间那么就发生了时间回拨，直接抛出异常
        if timestamp < self.last_timestamp:
            logging.error('clock is moving backwards. Rejecting requests until {}'.format(self.last_timestamp))
            raise InvalidSystemClock

        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & SEQUENCE_MASK
            if self.sequence == 0:
                timestamp = self.__wait_until_next_millis()
        else:
            self.sequence = 0

        self.last_timestamp = timestamp

        new_id = (
            ((timestamp - TWEPOCH) << TIMESTAMP_LEFT_SHIFT) |
            (self.datacenter_id << DATACENTER_ID_SHIFT) |
            (self.worker_id << WOKER_ID_SHIFT) |
            self.sequence
        )
        return new_id

    def __wait_until_next_millis(self):
        """等待到下一毫秒
        """
        timestamp = int(time.time() * 1000)
        while timestamp <= self.last_timestamp:
            timestamp = int(time.time() * 1000)
        return timestamp


if __name__ == '__main__':
    worker = IdWorker(1, 2, 0)
    print(worker.new_id())