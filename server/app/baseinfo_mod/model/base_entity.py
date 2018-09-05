# -*-coding:utf8-*-

from app import db

# 基础信息字段
class BaseEntity():
    id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    creator = db.Column(db.String(50))
    create_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modifier = db.Column(db.String(50))
    modify_at = db.Column(db.DateTime, default=db.func.current_timestamp())

