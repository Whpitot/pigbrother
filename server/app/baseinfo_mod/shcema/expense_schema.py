# coding:utf-8
from marshmallow import Schema, fields
from marshmallow import fields

class ExpenseSchema(Schema):
    
    class Meta:
        additional=(
            'id', 'create_at', 'creator', 'modify_at', 'modifier', 
            'family_id','family_code','family_name',
            'item', 'customer', 'type', 'money'
            )
      
