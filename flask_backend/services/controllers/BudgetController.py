from flask import jsonify
from sqlalchemy.sql import func
from services.models import *
from services.config import db
from datetime import datetime
import json

class BudgetController:


    @staticmethod
    def save_budget(data):
        if not data:
            return jsonify({'Error': 'No data supplied'}), 400

        # Parse the date from the supplied data
        budget_date = datetime.strptime(data['date'], '%Y-%m')

        # Check if a budget already exists for the given year and month
        budget = Budget.query.filter(func.strftime('%Y-%m', Budget.date) == data['date']).first()

        if budget:
            # Update the existing budget's budget_json
            budget.budget_json = json.dumps(data['budgets'])
            message = 'Budget data updated successfully'
        else:
            # Create a new budget object
            budget = Budget(
                date=budget_date,
                budget_json=json.dumps(data['budgets'])  # Corrected here
            )
            db.session.add(budget)
            message = 'Budget data saved successfully'

        # Commit the changes to the database
        db.session.commit()

        return jsonify({'message': message}), 200


    
    @staticmethod
    def get_budget(date):
        # Match only the year and month of the date

        budget = Budget.query.filter(
            func.strftime('%Y-%m', Budget.date) == date
        ).first()

        if budget:
            budget_json = json.loads(budget.budget_json)
            return jsonify({'message': budget_json})

        else:
            return jsonify({'message': {"fixed": [], "variable": [], "sinkingFunds": []}}), 200
        