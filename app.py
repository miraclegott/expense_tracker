from flask import Flask, request, jsonify
from flask_smorest import Api
from flask_migrate import Migrate
from models import db
from resources.currency import currency_bp
from resources.user import user_bp
from resources.expense import expense_bp

def create_app():
    app = Flask(__name__)

    # Додайте заголовок API
    app.config['API_TITLE'] = 'Lab 3: Expense Tracker API'  # Заголовок API

    # Додати версію OpenAPI
    app.config['OPENAPI_VERSION'] = '3.0.0'  # Версію OpenAPI

    # Додайте версію API
    app.config['API_VERSION'] = '2.0.1'  # Версія API

    # Конфігурація додатка
    app.config.from_object('config.Config')

    # Ініціалізація бібліотек
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    # Реєстрація Blueprint-ів
    api.register_blueprint(user_bp)
    api.register_blueprint(expense_bp)
    api.register_blueprint(currency_bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)