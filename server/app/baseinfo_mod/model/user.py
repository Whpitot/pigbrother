# -*-coding:utf8-*-

from db import db
from app.baseinfo_mod.model.base_entity import BaseEntity

class User(BaseEntity, db.Model):
    __tablename__ = 'expense'

    family_id = db.Column(db.Integer)
    family_code = db.Column(db.String(50))
    family_name = db.Column(db.String(50))

    code = db.Column(db.String(50))
    name_cn = db.Column(db.String(30))
    password = db.Column(db.String(30))
    signation = db.Column(db.String(50))    
