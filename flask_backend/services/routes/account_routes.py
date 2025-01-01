from flask import Blueprint
from services.models import *
from services.controllers import AccountController



account_bp = Blueprint('account', __name__)
accountController = AccountController()



@account_bp.route('/get_account_dict', methods=['GET'])
def get_account_dict():
    return accountController.get_account_dict()