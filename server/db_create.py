# -*-coding:utf8-*-

from db import db
from app import create_app
from log import logger
import time

app = create_app()

# 怎么去创建数据表
if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    