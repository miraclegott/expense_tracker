from flask.views import MethodView
from flask_smorest import Blueprint
from models import db, Expense
from schemas import ExpenseSchema

expense_bp = Blueprint('expenses', __name__, description='Operations on expenses')

@expense_bp.route('/expenses')
class ExpenseListResource(MethodView):  # Успадковуємо MethodView
    @expense_bp.response(200, ExpenseSchema(many=True))
    def get(self):
        return Expense.query.all()

    @expense_bp.arguments(ExpenseSchema)
    @expense_bp.response(201, ExpenseSchema)
    def post(self, new_data):
        expense = Expense(**new_data)
        db.session.add(expense)
        db.session.commit()
        return expense
