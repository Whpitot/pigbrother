# coding:utf-8
from marshmallow import Schema, fields
from marshmallow import fields

class FamilySchema(Schema):
    
    class Meta:
        additional=(
            'id', 'create_at', 'creator', 'modify_at', 'modifier', 
            'code', 'name_cn', 'member_qty', 'signation'
            )
      
