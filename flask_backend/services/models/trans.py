from services.config import db

class Trans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date,nullable=False)
    description = db.Column(db.String,nullable=False)
    orig_description = db.Column(db.String,nullable=False)
    amount = db.Column(db.Float, nullable=False)
    hash = db.Column(db.String, nullable=False)
     # Foreign key linking to the Account table
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    # Define relationship to Account
    account = db.relationship('Account', back_populates='trans')

    # Foreign key linking to the budget_category_table
    budget_category_id = db.Column(db.Integer)

    budget_item_id = db.Column(db.Integer)



    def __repr__(self):
        return f'<Trans - Id: {self.id} - Date: {self.date} - Description: {self.description} - Original Description: {self.orig_description} - Amount: {self.amount} - Account ID: {self.account_id}>'
