#encoding:utf-8
#name:config.py

import ConfigParser
import constant

path = constant.project_path+'/conf/config.ini'
config = ConfigParser.ConfigParser()
config.read(path)

print 'load config file:'+path
print 'config session loaded;', config.sections()

#获取config配置文件
def get(section, key):
    return config.get(section, key)

