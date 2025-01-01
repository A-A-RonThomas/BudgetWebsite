from services.config import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    trans = db.relationship('Trans', back_populates='account', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Account id={self.id} name={self.name}>"
