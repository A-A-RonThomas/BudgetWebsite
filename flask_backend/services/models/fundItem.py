from services.config import db

class FundItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    starting_value = db.Column(db.Float)
    plus = db.Column(db.Float)
    minus = db.Column(db.Float)
    ending_value = db.Column(db.Float)
    budget_category = db.Column(db.String)
    budget_table_id = db.Column(db.Integer)