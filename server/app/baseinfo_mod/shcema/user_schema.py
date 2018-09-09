# coding:utf-8
from marshmallow import Schema

class UserSchema(Schema):
    
    class Meta:
        additional=(
            'id', 'create_at', 'creator', 'modify_at', 'modifier', 
            'family_id','family_code','family_name',
            'code', 'name_cn', 'signation'
            )
      
