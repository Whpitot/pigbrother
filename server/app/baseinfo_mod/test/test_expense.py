# -*-coding:utf8-*-
import os
import json
import unittest
from db import db
from log import logger
from flask import Flask
from app import create_app
from datetime import datetime
from flask_fixtures import FixturesMixin

# ------------------------------------------------------
# If you try to perform database operations outside an application context, 
# you will see the following error:
# No application found. Either work inside a view function or push an application context.
# app.app_context().push()
# -------------------------------------------------------

class TestFamily(unittest.TestCase, FixturesMixin):    #自己可以封装一个访问的接口就好了
    os.environ['MODE'] ='TEST_SQLITE'
    db = db
    app = create_app()    
    # app.testing = True
    app.config['FIXTURES_DIRS'] = ['../app/baseinfo_mod/test/fixtures']
    client= app.test_client()
    fixtures = ['expense.json']                          

    # @unittest.skip('get测试')
    def test_expense_get(self):                             
        resp = self.client.get('/api/expense') #rv.data 返回的是一个字符串
        print 'resp.data------------>', resp.data
        data = json.loads(resp.data)
        self.assertEqual(data['objects'][0]['item'], 'apple')
        self.assertEqual(data['objects'][0]['money'], '300')     

    # @unittest.skip('post测试')
    def test_expense_post(self):
        data = {            
            "creator": "windy",
            "create_at": "2018-05-11 16:29:21",
            "modifier": "windy",
            "modify_at": "2018-05-11 16:29:21",
            "family_id":1,
            "family_code":"windy_family",
            "family_name":"windy的一家家",
            "item":"orange",
            "customer":"windy",
            "money":200,
            "type": "fruits"                              
        }
        resp = self.client.post('/api/expense', content_type='application/json', data= json.dumps(data))   
        print 'resp.data------------>', resp.data
        data = json.loads(resp.data)
        self.assertEqual(data['item'], 'orange')
        self.assertEqual(data['money'], '200') 
             
if __name__=='__main__':
    unittest.main()