from services.config import db

class BudgetItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    expected = db.Column(db.Float)
    actual = db.Column(db.Float)
    budget_table_id = db.Column(db.Integer)
    



    def __repr__(self):
        return f'<Budget Item - Id: {self.id} - Name: {self.name}>'
