from flask.views import MethodView
from flask_smorest import Blueprint
from flask import request
from models import db, Currency
from schemas import CurrencySchema

currency_bp = Blueprint('currencies', __name__, description='Operations on currencies')

@currency_bp.route('/currencies')
class CurrencyListResource(MethodView):
    @currency_bp.response(200, CurrencySchema(many=True))
    def get(self):
        """Отримати всі валюти"""
        return Currency.query.all()
    
    @currency_bp.arguments(CurrencySchema)
    @currency_bp.response(201, CurrencySchema)
    def post(self, new_data):
        """Додати нову валюту"""
        currency = Currency(**new_data)
        db.session.add(currency)
        db.session.commit()
        return currency

@currency_bp.route('/currencies/<int:currency_id>')
class CurrencyResource(MethodView):
    @currency_bp.response(200, CurrencySchema)
    def get(self, currency_id):
        """Отримати валюту за ID"""
        currency = Currency.query.get_or_404(currency_id)
        return currency

    @currency_bp.arguments(CurrencySchema)
    @currency_bp.response(200, CurrencySchema)
    def put(self, updated_data, currency_id):
        """Оновити валюту за ID"""
        currency = Currency.query.get_or_404(currency_id)
        for key, value in updated_data.items():
            setattr(currency, key, value)
        db.session.commit()
        return currency

    @currency_bp.response(204)
    def delete(self, currency_id):
        """Видалити валюту за ID"""
        currency = Currency.query.get_or_404(currency_id)
        db.session.delete(currency)
        db.session.commit()
        return '', 204
