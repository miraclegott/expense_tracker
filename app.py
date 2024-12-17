from flask import Flask, request, jsonify
from data import users, categories, records, get_next_id

app = Flask(__name__)

# Створення користувача
@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    new_user = {"id": get_next_id(users), "name": data.get("name")}
    users.append(new_user)
    return jsonify(new_user), 201

# Отримання списку користувачів
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

# Отримання користувача за ID
@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

# Видалення користувача
@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return jsonify({"message": "User deleted"}), 200

# Створення категорії
@app.route("/category", methods=["POST"])
def create_category():
    data = request.json
    new_category = {"id": get_next_id(categories), "name": data.get("name")}
    categories.append(new_category)
    return jsonify(new_category), 201

# Отримання списку категорій
@app.route("/category", methods=["GET"])
def get_categories():
    return jsonify(categories), 200

# Видалення категорії
@app.route("/category/<int:category_id>", methods=["DELETE"])
def delete_category(category_id):
    global categories
    categories = [c for c in categories if c['id'] != category_id]
    return jsonify({"message": "Category deleted"}), 200

# Створення запису про витрати
@app.route("/record", methods=["POST"])
def create_record():
    data = request.json
    new_record = {
        "id": get_next_id(records),
        "user_id": data.get("user_id"),
        "category_id": data.get("category_id"),
        "amount": data.get("amount"),
        "created_at": data.get("created_at"),
    }
    records.append(new_record)
    return jsonify(new_record), 201

# Отримання запису за ID
@app.route("/record/<int:record_id>", methods=["GET"])
def get_record(record_id):
    record = next((r for r in records if r['id'] == record_id), None)
    if record:
        return jsonify(record), 200
    return jsonify({"message": "Record not found"}), 404

# Отримання списку записів з фільтрацією
@app.route("/record", methods=["GET"])
def get_records():
    user_id = request.args.get("user_id")
    category_id = request.args.get("category_id")

    if not user_id and not category_id:
        return jsonify({"error": "Missing user_id or category_id"}), 400

    filtered_records = [
        r for r in records
        if (not user_id or r['user_id'] == int(user_id)) and
           (not category_id or r['category_id'] == int(category_id))
    ]
    return jsonify(filtered_records), 200

# Видалення запису
@app.route("/record/<int:record_id>", methods=["DELETE"])
def delete_record(record_id):
    global records
    records = [r for r in records if r['id'] != record_id]
    return jsonify({"message": "Record deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
