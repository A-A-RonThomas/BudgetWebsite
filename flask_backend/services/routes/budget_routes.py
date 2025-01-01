from flask import Blueprint, request
from services.models import *
from services.controllers import BudgetController



budget_bp = Blueprint('budget', __name__)
budgetController = BudgetController()



@budget_bp.route('/save-budget', methods=['POST'])
def save_budget():
    data = request.json
    return budgetController.save_budget(data)

@budget_bp.route('/get-budget-<date>', methods=['GET'])
def get_budget(date):
    return budgetController.get_budget(date)