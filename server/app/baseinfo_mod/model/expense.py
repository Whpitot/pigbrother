# -*-coding:utf8-*-

from db import db
from app.baseinfo_mod.model.base_entity import BaseEntity

class Expense(BaseEntity, db.Model):
    __tablename__ = 'expense'

    family_id = db.Column(db.Integer)
    family_code = db.Column(db.String(50))
    family_name = db.Column(db.String(50))

    item = db.Column(db.String(50))
    customer = db.Column(db.String(30))
    money = db.Column(db.String(50))
    type = db.Column(db.String(50))
