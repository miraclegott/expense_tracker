from flask.views import MethodView
from flask_smorest import Blueprint
from models import db, Expense
from schemas import ExpenseSchema

expense_bp = Blueprint('expenses', __name__, description='Operations on expenses')

@expense_bp.route('/expenses')
class ExpenseListResource(MethodView):
    @expense_bp.response(200, ExpenseSchema(many=True))
    def get(self):
        """Отримати всі витрати"""
        return Expense.query.all()

    @expense_bp.arguments(ExpenseSchema)
    @expense_bp.response(201, ExpenseSchema)
    def post(self, new_data):
        """Додати нову витрату"""
        expense = Expense(**new_data)
        db.session.add(expense)
        db.session.commit()
        return expense

@expense_bp.route('/expenses/<int:expense_id>')
class ExpenseResource(MethodView):
    @expense_bp.response(200, ExpenseSchema)
    def get(self, expense_id):
        """Отримати витрату за ID"""
        expense = Expense.query.get_or_404(expense_id)
        return expense

    @expense_bp.arguments(ExpenseSchema)
    @expense_bp.response(200, ExpenseSchema)
    def put(self, updated_data, expense_id):
        """Оновити витрату за ID"""
        expense = Expense.query.get_or_404(expense_id)
        for key, value in updated_data.items():
            setattr(expense, key, value)
        db.session.commit()
        return expense

    @expense_bp.response(204)
    def delete(self, expense_id):
        """Видалити витрату за ID"""
        expense = Expense.query.get_or_404(expense_id)
        db.session.delete(expense)
        db.session.commit()
        return '', 204
