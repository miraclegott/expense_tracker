from flask.views import MethodView
from flask_smorest import Blueprint
from flask import request
from models import db, Currency
from schemas import CurrencySchema

currency_bp = Blueprint('currencies', __name__, description='Operations on currencies')

@currency_bp.route('/currencies')
class CurrencyListResource(MethodView):  # Важливо, щоб клас успадковував MethodView
    @currency_bp.response(200, CurrencySchema(many=True))
    def get(self):
        return Currency.query.all()
    
    @currency_bp.arguments(CurrencySchema)
    @currency_bp.response(201, CurrencySchema)
    def post(self, new_data):
        currency = Currency(**new_data)
        db.session.add(currency)
        db.session.commit()
        return currency
