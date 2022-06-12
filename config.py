# -*- coding:utf-8 -*-
_author_ = 'weijian'



# 数据库的配置信息
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'flask'
USERNAME = 'root'
PASSWORD = ''
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

#将链接数据库的配置传递给APP
SQLALCHEMY_DATABASE_URI = DB_URI
#是否每次跟踪修改设置为是
SQLALCHEMY_TRACK_MODIFICATIONS = True

#session的配置key
SECRET_KEY = '12dffdf'

#邮箱配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAM = '649514913@qq.com'
MAIL_PASSWORD = 'ossdqfqfphwebbad'
MAIL_DEFAULT_SENDE = '649514913@qq.com'
