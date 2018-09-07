from app.baseinfo_mod.model.user import User

def create_user_blueprint(api_manager):    
    user_api = api_manager.create_api_blueprint(User, methods = ['GET','POST'])
    api_manager.app.register_blueprint(user_api, url_prefix = '/api')