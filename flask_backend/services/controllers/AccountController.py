from flask import jsonify
from services.models import *
from services.config import db
from datetime import datetime

class AccountController:
    @staticmethod
    def populate_accounts():
        accounts = Account.query.all()

        if not accounts:
            db.session.add(Account(name='joint'))

            db.session.add(Account(name='grocery'))

            db.session.add(Account(name='sinking fund'))

            db.session.commit()


    
    @staticmethod
    def get_account_dict():
        account_dict = {a.name: a.id for a in Account.query.all()}

        if account_dict:
            return jsonify(account_dict), 200
        else:
            return jsonify({'Error': 'Error in retrieving account dictionary'}), 500
        
