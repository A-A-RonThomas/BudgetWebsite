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
        
        print("Data:", data)
        message = 'test'
        # # Parse the date from the supplied data
        # budget_date = datetime.strptime(data['date'], '%Y-%m')

        # # Check if a budget already exists for the given year and month
        # budget = Budget.query.filter(func.strftime('%Y-%m', Budget.date) == data['date']).first()

        # if budget:
        #     message = 'Budget data updated successfully'

        #     for budget_table_type in data['budget_tables']:
        #         for budget_table in data['budget_tables'][budget_table_type]:
        #             db_budget_table = BudgetTable.query.filter(BudgetTable.name == budget_table and BudgetTable.budget_id == budget.id).first()

        #             for budget_item in data['budget_tables'][budget_table_type][budget_table]:
        #                 # if the budget_table is a fund
        #                 if db_budget_table.isFund:
        #                     if 'id' not in budget_item.keys():
        #                         new_budget_item = FundItem(
        #                             name = budget_item['name'],
        #                             plus = budget_item['plus'],
        #                             minus = budget_item['minus'],
        #                             ending_value = budget_item['ending_value'],
        #                             starting_value = budget_item['starting_value'],
        #                             budget_category = budget_item['category'],
        #                             budget_table_id = db_budget_table.id
        #                         )
        #                         db.session.add(new_budget_item)
                            
        #                     # Handles existing budget_items
        #                     else:
        #                         db_budget_item = FundItem.query.filter(FundItem.id == budget_item['id']).first()
        #                         budget_item_keys = budget_item.keys()
        #                         for key in budget_item_keys:
        #                             setattr(db_budget_item, key, budget_item[key])

        #                 # if the budget_table is not a fund
        #                 else:
        #                     # Handles newly entered budget_items 
        #                     if 'id' not in budget_item.keys():
        #                         new_budget_item = BudgetItem(
        #                             name = budget_item['name'],
        #                             expected = budget_item['expected'],
        #                             actual = budget_item['actual'],
        #                             budget_table_id = db_budget_table.id,
        #                             budget_category = budget_item['category']
        #                         )
        #                         db.session.add(new_budget_item)
                            
        #                     # Handles existing budget_items
        #                     else:
        #                         db_budget_item = BudgetItem.query.filter(BudgetItem.id == budget_item['id']).first()
        #                         budget_item_keys = budget_item.keys()
        #                         for key in budget_item_keys:
        #                             setattr(db_budget_item, key, budget_item[key])

                            
                            
            
        #     db.session.commit()

        #     # print("data:", data)




        # # else:
        # #     # Create a new budget object
        # #     budget = Budget(
        # #         date=budget_date,
        # #         # budget_json=json.dumps(data['budgets'])  # Corrected here
        # #     )
        # #     db.session.add(budget)
        # #     message = 'Budget data saved successfully'

        # # # Commit the changes to the database
        # # db.session.commit()

        return jsonify({'message': message}), 200


    # Need significant work here to build the dictionary following the new schema.
    @staticmethod
    def get_budget(date):
        # Match only the year and month of the date

        budget = Budget.query.filter(
            func.strftime('%Y-%m', Budget.date) == date
        ).first()


        if budget:
            budget_id = budget.id
            budget_tables = [(b.id, b.name, b.isFund) for b in BudgetTable.query.filter(BudgetTable.budget_id == budget_id).all()]

            # non_fund_tables = {
            #     name[1]: {
            #         'items': [
            #             {'id': bi.id, 'name': bi.name, 'expected': bi.expected, 'actual': bi.actual}
            #             for bi in BudgetItem.query.filter(BudgetItem.budget_table_id == name[0])
            #         ],
            #         'budget_table_id': name[0]
            #     }
            #     for name in budget_tables if not name[2]
            # }

            non_fund_tables = {
                name[0]: {
                    'name': name[1],
                    'items': [
                        {'id': bi.id, 'name': bi.name, 'expected': bi.expected, 'actual': bi.actual}
                        for bi in BudgetItem.query.filter(BudgetItem.budget_table_id == name[0])
                    ],
                    'budget_table_id': name[0]
                }
                for name in budget_tables if not name[2]
            }

            
            fund_tables = {
                name[0]: {
                    'name': name[1],
                    'items': [
                        {'id': fi.id, 'name': fi.name, 'plus': fi.plus, 'minus': fi.minus, 'ending_value': fi.ending_value, 
                        'starting_value': fi.starting_value, 'budget_category': fi.budget_category}
                        for fi in FundItem.query.filter(FundItem.budget_table_id == name[0])
                    ],
                    'budget_table_id': name[0]
                } 
                for name in budget_tables if name[2]
            }

            return jsonify({'message': {'Budget Id': str(budget_id), 'budget': {'non_fund': non_fund_tables, 'fund': fund_tables}}})

        else:
            # return jsonify({'message': {"fixed": [], "variable": [], "sinkingFunds": []}}), 200
            return jsonify({'message': {'Budget Id': None, 'budget': {'non-fund': {}, 'fund': {}}}}), 200
        
    

    @staticmethod
    def delete_budget_item(data):
        try:

            if not data['type']:
                BudgetItem.query.filter(BudgetItem.id == data['item']['id']).delete()

            else:
                FundItem.query.filter(FundItem.id == data['item']['id']).delete()

            db.session.commit()

            return jsonify({'message': 'Success'}), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500
        