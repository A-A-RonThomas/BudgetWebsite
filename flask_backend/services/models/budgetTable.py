from services.config import db

class BudgetTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable=False)
    budget_id = db.Column(db.Integer, nullable=False)
    isFund = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Budget Table - Id: {self.id} - Name: {self.name} - Budget ID: {self.budget_id} - IsFund: {self.isFund}>'
