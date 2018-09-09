from app.baseinfo_mod.model.family import Family

def create_family_blueprint(api_manager):    

    # 根据family_id过滤用户
    # post 多个用户提交

    family_api = api_manager.create_api_blueprint(Family, methods = ['GET','POST'])
    api_manager.app.register_blueprint(family_api, url_prefix = '/api')