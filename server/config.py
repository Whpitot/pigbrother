# -*-coding:utf8-*-

class DevelopmentMysqlConfig():
    SQLALCHEMY_DATABASE_URI  = 'mysql://root:123456@localhost/pigbrother'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

class DevelopmentSqliteConfig_momery():   #在内存中创建一个sqlite
    SQLALCHEMY_DATABASE_URI  = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentSqliteConfig_disk():   
    SQLALCHEMY_DATABASE_URI  = 'sqlite:////tmp/testapp.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

config = {
    'development_mysql':DevelopmentMysqlConfig,
    'development_sqlite_momery':DevelopmentSqliteConfig_momery,
    'development_sqlite_disk':DevelopmentSqliteConfig_disk,
    'default':DevelopmentMysqlConfig
}