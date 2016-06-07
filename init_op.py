# -*- coding: utf-8 -*-
'''
Created on 2015-12-9

@author: Administrator
'''
#!/usr/bin/python
# -*- coding:utf-8 -*-
#author: lingyue.wkl
#desc: use to read ini
#---------------------
#2012-02-18 created

#---------------------
import sys
import ConfigParser


class Config:
    def __init__(self, path):
        self.path = path
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.path)

    def get(self, field, key):
        result = ""
        try:
            result = self.cf.get(field, key)
        except:
            result = ""
        return result

    def set(self, filed, key, value):
        try:
            self.cf.set(field, key, value)
            self.cf.write(open(self.path, 'w'))
        except:
            return False
        return True


def read_config(config_file_path, field, key):
    cf = ConfigParser.ConfigParser()
    try:
        cf.read(config_file_path)
        result = cf.get(field, key)
    except Exception,e:
        print "error:",e,config_file_path
        result = 0
    return result


def write_config(config_file_path, field, key, value):
    if value == "":
        value = '0'
    cf = ConfigParser.ConfigParser()
    try:
        cf.read(config_file_path)
        cf.set(field, key, value)
        cf.write(open(config_file_path, 'w'))
    except Exception, e:
        print e
        # sys.exit(1)
    return True

if __name__ == "__main__":
#     if len(sys.argv) < 4:
#         sys.exit(1)
# 
#     config_file_path = sys.argv[1]
#     field = sys.argv[2]
#     key = sys.argv[3]
#     if len(sys.argv) == 4:
#         print read_config(config_file_path, field, key)
#     else:
#         value = sys.argv[4]
#         write_config(config_file_path, field, key, value)
    config_file_path = "conf/ST_CONF.ini"
    SYS_CONF_PATH = "conf/SYS_CONF.ini"
    write_config(SYS_CONF_PATH, "AI518P", "meas_times", 10)
    # print read_config(config_file_path, 'INST', 'meas_mode')
    