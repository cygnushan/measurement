# -*- coding: utf-8 -*-
'''
Created on 2015-12-21

@author: Administrator
'''
import os
import sys
import logging
import traceback

script_path = os.getcwd()
root_path = os.path.dirname(script_path)
sys.path.insert(0,root_path)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler(script_path + '/debug.log')
fh.setLevel(logging.INFO)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s')
datefmt = logging.Formatter
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)

def my_exception_handler(exc_type, exc_value, exc_tb):
    # logger.error(exc_type)
    # logger.error(''.join(traceback.format_tb(exc_tb)))
    logger.error(''.join(traceback.format_exception(exc_type, exc_value, exc_tb)))
                
sys.excepthook = my_exception_handler


if __name__== "__main__":
    logger.debug('This is debug message')
    logger.info('This is info message')
    logger.warning('This is warning message')
