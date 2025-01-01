from services.config import db

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date,nullable=False)
    budget_json = db.Column(db.String,nullable=False)


    def __repr__(self):
        return f'<Budget - Id: {self.id} - Date: {self.date} - Budget JSON: {self.budget_json}>'
