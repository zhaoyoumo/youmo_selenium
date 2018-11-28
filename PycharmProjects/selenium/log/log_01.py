#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-05-17 11:19
# log/log.py

import logging
import logging.handlers


# 日志类
class Logger():
    LOG_FILE = 'tst.log'

    handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)  # 实例化handler
    fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

    formatter = logging.Formatter(fmt)  # 实例化formatter
    handler.setFormatter(formatter)  # 为handler添加formatter

    logger = logging.getLogger('tst')  # 获取名为tst的logger
    logger.addHandler(handler)  # 为logger添加handler
    logger.setLevel(logging.DEBUG)

    def loginfo(self, message):
        self.logger.info(message)

    def logdebug(self, message):
        self.logger.debug(message)
