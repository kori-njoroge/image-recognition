from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    barcode = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)
