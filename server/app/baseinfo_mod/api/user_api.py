# -*-coding:utf8-*-
from app.baseinfo_mod.model.user import User

def create_user_blueprint(api_manager):    
    """
    post 多个用户提交
    根据family_id过滤用户
    """    
    user_api = api_manager.create_api_blueprint(
        User, exclude_columns=['password'], methods = ['GET','POST'])        
    api_manager.app.register_blueprint(user_api, url_prefix = '/api')