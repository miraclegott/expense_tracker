from flask.views import MethodView
from flask_smorest import Blueprint
from models import db, User
from schemas import UserSchema

user_bp = Blueprint('users', __name__, description='Operations on users')

@user_bp.route('/users')
class UserListResource(MethodView):  # Клас має успадковувати MethodView
    @user_bp.response(200, UserSchema(many=True))
    def get(self):
        return User.query.all()

    @user_bp.arguments(UserSchema)
    @user_bp.response(201, UserSchema)
    def post(self, new_data):
        user = User(**new_data)
        db.session.add(user)
        db.session.commit()
        return user
