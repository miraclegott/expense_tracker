from flask.views import MethodView
from flask_smorest import Blueprint
from models import db, User, Currency
from schemas import UserSchema

user_bp = Blueprint('users', __name__, description='Operations on users')

@user_bp.route('/users')
class UserListResource(MethodView):
    @user_bp.response(200, UserSchema(many=True))
    def get(self):
        """Отримати список усіх користувачів"""
        return User.query.all()

    @user_bp.arguments(UserSchema)
    @user_bp.response(201, UserSchema)
    def post(self, new_data):
        """Додати нового користувача"""
        user = User(**new_data)
        db.session.add(user)
        db.session.commit()
        return user

@user_bp.route('/users/<int:user_id>')
class UserResource(MethodView):
    @user_bp.response(200, UserSchema)
    def get(self, user_id):
        """Отримати користувача за ID"""
        user = User.query.get_or_404(user_id)
        return user

    @user_bp.arguments(UserSchema)
    @user_bp.response(200, UserSchema)
    def put(self, updated_data, user_id):
        """Оновити дані користувача за ID"""
        user = User.query.get_or_404(user_id)
        for key, value in updated_data.items():
            setattr(user, key, value)
        db.session.commit()
        return user

    @user_bp.response(204)
    def delete(self, user_id):
        """Видалити користувача за ID"""
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

@user_bp.route('/users/<int:user_id>/default_currency')
class UserDefaultCurrencyResource(MethodView):
    @user_bp.response(200, UserSchema)
    def get(self, user_id):
        """Отримати валюту за замовчуванням для користувача"""
        user = User.query.get_or_404(user_id)
        currency = Currency.query.get(user.default_currency_id)
        if currency:
            return {"default_currency": currency.name, "symbol": currency.symbol}
        else:
            return {"default_currency": None}, 404

    @user_bp.response(200)
    def post(self, user_id):
        """Встановити валюту за замовчуванням для користувача"""
        user = User.query.get_or_404(user_id)
        currency_id = request.json.get("currency_id")
        currency = Currency.query.get_or_404(currency_id)
        user.default_currency_id = currency.id
        db.session.commit()
        return {"message": f"Default currency set to {currency.name}"}, 200
