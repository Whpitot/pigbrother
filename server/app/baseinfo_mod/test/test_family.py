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
    fixtures = ['family.json']                          

    # @unittest.skip('get测试')
    def test_family_get(self):                             
        resp = self.client.get('/api/family') #rv.data 返回的是一个字符串
        print 'resp.data------------>', resp.data
        data = json.loads(resp.data)
        self.assertEqual(data['objects'][0]['code'], 'windy_family')
        self.assertEqual(data['objects'][0]['member_qty'], 3)     

    # @unittest.skip('post测试')
    def test_family_post(self):
        data = {
            "code": "windy_family",
            "create_at": "2018-09-05",
            "creator": "windy",        
            "member_qty": 2,
            "modifier": "windy",
            "modify_at": "2018-09-05",
            "name_cn": "小小妹",
            "signation": "小小妹"
            }
        resp = self.client.post('/api/family', content_type='application/json', data= json.dumps(data))   
        print 'resp.data------------>', resp.data
        data = json.loads(resp.data)
        self.assertEqual(data['code'], 'windy_family')
        self.assertEqual(data['member_qty'], 2) 
             
if __name__=='__main__':
    unittest.main()