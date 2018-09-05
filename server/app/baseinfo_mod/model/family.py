# -*-coding:utf8-*-

from db import db
from app.baseinfo_mod.model.base_entity import BaseEntity

class Family(BaseEntity, db.Model):
    __tablename__ = 'family'

    code = db.Column(db.String(50))
    name_cn = db.Column(db.String(30))
    member_qty = db.Column(db.Integer)
    signation = db.Column(db.String(50))    
