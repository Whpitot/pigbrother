# -*-coding:utf8-*-

import os 
from logbook import Logger, TimedRotatingFileHandler

current_root_path = os.getcwd()
print 

handler = TimedRotatingFileHandler(current_root_path + '\\log\\app.log',backup_count =30,date_format='%Y-%m-%d',bubble=True)     #先要自己创建一个log目录             
handler.push_application()
logger = Logger('app')