from services.config import db

class BudgetCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


    def __repr__(self):
        return f'<Budget Category - Id: {self.id} - Name: {self.name}>'
