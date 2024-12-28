from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    default_currency_id = db.Column(db.Integer, db.ForeignKey('currencies.id'), nullable=True)
    default_currency = db.relationship('Currency', back_populates='users')

class Currency(db.Model):
    __tablename__ = 'currencies'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    users = db.relationship('User', back_populates='default_currency')

class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    currency_id = db.Column(db.Integer, db.ForeignKey('currencies.id'), nullable=True)
    currency = db.relationship('Currency')

with app.app_context():
    db.create_all()
