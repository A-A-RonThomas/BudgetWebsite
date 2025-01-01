from flask import jsonify
from services.models import *
from services.config import db
from datetime import datetime
import hashlib

class TransactionController:
    @staticmethod
    def generate_transaction_hash(el):
        hash_input = f"{el[0]}|{el[1]}|{el[2]}|{el[4]}|{el[6]}"

        return hashlib.sha256(hash_input.encode('utf-8')).hexdigest()


    @staticmethod
    def filter_new_purchases(data):
        filtered = []
        incoming = data
        for each in incoming:
            each.append(TransactionController.generate_transaction_hash(each))

        target_date = datetime.strptime(data[0][0], "%Y-%m-%d").date()
        logged_hashes = [t.hash for t in Trans.query.filter(Trans.date >= target_date).all()]

        filtered = [el for el in incoming if el[len(el) - 1] not in logged_hashes]

        return filtered
    

    @staticmethod
    def insert_transactions(data):
        if data:
            try:
                for el in TransactionController.filter_new_purchases(data):
                    new_trans = Trans(
                        date = datetime.strptime(el[0], "%Y-%m-%d"),
                        description = el[1],
                        orig_description = el[2],
                        amount = float(el[4]),
                        hash = el[7],
                        account_id = el[6]
                    )
                    db.session.add(new_trans)

                db.session.commit()
                return jsonify({'message': 'Data Inserted'}), 200
            
            except Exception as e:
                return jsonify({'Error': f'{str(e)}'}), 500
        
        else:
            return jsonify({'Error': "No data suplied"}), 400
        
    

    @staticmethod
    def get_all():
            transactions = Trans.query.order_by(Trans.date.desc()).all()
            account_dict = {a.id: a.name for a in Account.query.all()}

            to_send = [{
                'date': t.date.strftime('%Y-%m-%d'),
                'description': t.description,
                'amount': t.amount,
                'account': account_dict[t.account_id]
            } for t in transactions]

            return jsonify({"All transactions": to_send}), 200


    @staticmethod
    def get_all_purchases(year=None, month=None):
        try:
            query = Trans.query.filter(Trans.amount < 0)

            # Apply year filter if provided
            if year:
                query = query.filter(db.extract('year', Trans.date) == year)

            # Apply month filter if provided
            if month:
                query = query.filter(db.extract('month', Trans.date) == month)

            query = query.order_by(Trans.date.desc())

            purchases = query.all()
            account_dict = {a.id: a.name for a in Account.query.all()}

            to_send = [
                {
                    'id': t.id,
                    'date': t.date.strftime('%Y-%m-%d'),
                    'description': t.description,
                    'amount': t.amount,
                    'account': account_dict[t.account_id]
                }
                for t in purchases
            ]

            if purchases:
                return jsonify({"purchases": to_send}), 200
            else:
                return jsonify({"purchases": {}}), 200
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500

        

    @staticmethod
    def get_all_incomes(year=None, month=None):
        try:
            query = Trans.query.filter(Trans.amount >= 0)

            # Apply year filter if provided
            if year:
                query = query.filter(db.extract('year', Trans.date) == year)

            # Apply month filter if provided
            if month:
                query = query.filter(db.extract('month', Trans.date) == month)
            
            query = query.order_by(Trans.date.desc())

            incomes = query.all()
            account_dict = {a.id: a.name for a in Account.query.all()}

            to_send = [
                {
                    'id': t.id,
                    'date': t.date.strftime('%Y-%m-%d'),
                    'description': t.description,
                    'amount': t.amount,
                    'account': account_dict[t.account_id]
                }
                for t in incomes
            ]

            if incomes:
                return jsonify({"incomes": to_send}), 200
            else:
                return jsonify({"incomes": {}}), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
