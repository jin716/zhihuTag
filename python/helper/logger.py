#coding:utf-8
import logging.handlers

import config
from python import constant

LOG_FILE = constant.project_path + '/log/debug.log'

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
formatter = logging.Formatter(fmt)  # 实例化formatter
handler.setFormatter(formatter)  # 为handler添加formatter

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
# 设置日志打印格式
consoleHandler.setFormatter(formatter)
# 将定义好的console日志handler添加到root logger


logger = logging.getLogger('tagRank')  # 获取名为tst的logger
logger.addHandler(handler)  # 为logger添加handler
logger.addHandler(consoleHandler)

level = config.getConfig('log', 'level')
logger.setLevel(logging.DEBUG)
if(level == 'ERROR'):
    logger.setLevel(logging.ERROR)
if (level == 'INFO'):
        logger.setLevel(logging.INFO)


def debug(msg):
    logger.debug(msg)

def info(msg):
    logger.info(msg)

def error(msg):
    logger.error(msg)

debug('123')