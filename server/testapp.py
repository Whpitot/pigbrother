# -*-coding:utf8-*-

from flask import Flask,Blueprint,jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError, validate, pre_load, post_dump, post_load


app = Flask(__name__)   # 第一个参数是模块或者包的名字，参数是必须的
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:123456@localhost/windy'
db = SQLAlchemy(app)

customerUri = Blueprint('customer',__name__)


# 基础信息字段
class Entity():
    FInterID = db.Column(db.Integer, primary_key = True)
    FCreator = db.Column(db.String(50))
    FCreateTime = db.Column(db.DateTime)
    FModifier = db.Column(db.String(50))
    FModifyTime = db.Column(db.DateTime)

# 客户资料    
class Customer(Entity, db.Model):   
    __tablename__ = 't_customer'

    Name = db.Column(db.String(50))
    FullName = db.Column(db.String(100))
    Fax = db.Column(db.Integer)
    Tel = db.Column(db.String(50))
    Address = db.Column(db.String(100))
    Note = db.Column(db.String(200))

class EntitySchema(Schema):
    FInterID = fields.Int() #dump_only 只能被serialization，而不能被deserialization
    FCreator = fields.Str()
    FCreateTime = fields.DateTime()
    FModifier = fields.Str()
    FModifyTime = fields.Str()    

class CustomerSchema(EntitySchema):
    Name = fields.Str(required=True)
    FullName = fields.Str()
    Fax = fields.Str()
    Tel = fields.Str()
    Address = fields.Str()
    Note = fields.Str()

    @post_load
    def trans_customer(self, data):
        return Customer(**data)    

customer_singel_schema = CustomerSchema()
customer_all_schema = CustomerSchema(many = True)        

@customerUri.route('customers/<int:pk>',methods=['DELETE'])
def delete_customer(pk):
    customer = Customer.query.get(pk)
    if customer is None:
        return jsonify({'message':'Customer\'s FInter {0} not exists'.format(pk)})
    try:
        db.session.delete(customer)
        db.session.commit()
        return jsonify({'message':'delete successful'})
    except Exception as ex:
        return jsonify({'message':ex.message})     

@customerUri.route('/customers',methods=['GET'])
def get_allcustomer():
    customers = Customer.query.all()
    result, err = customer_all_schema.dump(customers)
    if err:
        return jsonify(err)
    return jsonify({"customer":result})        

if __name__ == "__main__": # 当当前模块为启动模块，执行命令
    app.register_blueprint(customerUri, url_prefix="/api") 
    app.run(debug=True,port=5000) #jkfjk         