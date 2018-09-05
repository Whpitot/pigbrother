
# -*- coding:utf8 -*-

from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from app import create_app
from db import db

app = create_app()
migrate = Migrate(app, db) #注册migrate到flask
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# 初始化数据库
if __name__ == '__main__':
    manager.run()
