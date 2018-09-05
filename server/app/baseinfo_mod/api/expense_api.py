from app.baseinfo_mod.model.expense import Expense

def create_expense_blueprint(api_manager):    
    expense_api = api_manager.create_api_blueprint(Expense, methods = ['GET', 'POST'])
    api_manager.app.register_blueprint(expense_api, url_prefix = '/api')