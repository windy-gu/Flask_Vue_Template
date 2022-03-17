# author:windy
# datetime:2022/3/3 9:29 AM
# software: PyCharm

import os
import datetime
from logging.handlers import BaseRotatingHandler


class DayRotatingHandler(BaseRotatingHandler):
    """
    主要功能是实现日志按天分割的功能
    """
    def __init__(self, filename, mode, encoding=None, delay=False):
        self.date = datetime.date.today()
        self.suffix = "%Y-%m-%d.log"
        super(BaseRotatingHandler, self).__init__(filename, mode, encoding, delay)

    def shouldRollover(self, record):
        return self.date != datetime.date.today()

    def doRollover(self):
        if self.stream:
            self.stream.close()
            self.stream = None
        new_log_file = os.path.join(os.path.split(self.baseFilename)[0], datetime.date.today().strftime(self.suffix))
        self.baseFilename = "{}".format(new_log_file)
        self._open()
