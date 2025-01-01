from flask import Blueprint, jsonify
from services.models import *
import pandas as pd




fun_bp = Blueprint('fun', __name__)

@fun_bp.route('/monthly-summary', methods=['GET'])
def monthly_summary():
    # Query data from the database
    expenses_query = Trans.query.filter(Trans.amount < 0).all()
    income_query = Trans.query.filter(Trans.amount >= 0).all()

    # Convert to Pandas DataFrame
    expenses = pd.DataFrame([{
        "date": e.date,
        "amount": e.amount,
        "description": e.description,
        "account_id": e.account_id
    } for e in expenses_query])

    income = pd.DataFrame([{
        "date": i.date,
        "amount": i.amount,
        "description": i.description,
        "account_id": i.account_id
    } for i in income_query])

    # Data manipulation
    expenses["month"] = pd.to_datetime(expenses["date"]).dt.to_period("M")
    income["month"] = pd.to_datetime(income["date"]).dt.to_period("M")

    monthly_expenses = expenses.groupby("month")["amount"].sum()
    monthly_income = income.groupby("month")["amount"].sum()

    summary = pd.DataFrame({
        "month": monthly_expenses.index.astype(str),
        "expenses": monthly_expenses.values,
        "income": monthly_income.reindex(monthly_expenses.index, fill_value=0).values
    })

    # Convert to JSON
    return jsonify(summary.to_dict(orient="records"))
