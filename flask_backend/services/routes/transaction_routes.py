from flask import Blueprint, request, jsonify
from services.models import *
from services.controllers import TransactionController



transaction_bp = Blueprint('transaction', __name__)

transactionContoller = TransactionController()

@transaction_bp.route('/insert', methods=['POST'])
def insert_transaction_data():
    data = request.get_json()['transactions']

    return transactionContoller.insert_transactions(data)



@transaction_bp.route('/get_all', methods=['GET'])
def get_all_transactions():
    return TransactionController.get_all()
    


@transaction_bp.route('/get_all_purchases', methods=['GET'])
def get_all_purchases():
    return TransactionController.get_all_purchases()



@transaction_bp.route('/get_all_purchases/<year>', methods=['GET'])
def get_all_purchases_year(year):
    return TransactionController.get_all_purchases(year)



@transaction_bp.route('/get_all_purchases/<year>-<month>', methods=['GET'])
def get_all_purchases_year_month(year, month):
    return TransactionController.get_all_purchases(year, month)



@transaction_bp.route('/get_all_incomes', methods=['GET'])
def get_all_incomes():
    return TransactionController.get_all_incomes()



@transaction_bp.route('/get_all_incomes/<year>', methods=['GET'])
def get_all_incomes_year(year):
    return TransactionController.get_all_incomes(year)



@transaction_bp.route('/get_all_incomes/<year>-<month>', methods=['GET'])
def get_all_incomes_year_month(year, month):
    return TransactionController.get_all_incomes(year, month)


@transaction_bp.route('/save_purchases', methods=['POST'])
def save_purchases():
    data = request.get_json()
    print("Hit Save Purchases Route")
    return TransactionController.save_purchases(data)
