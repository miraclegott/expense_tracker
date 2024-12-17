# data.py

users = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Smith"},
    {"id": 3, "name": "Alice Johnson"}
]

categories = [
    {"id": 1, "name": "Food"},
    {"id": 2, "name": "Transport"},
    {"id": 3, "name": "Entertainment"},
    {"id": 4, "name": "Utilities"}
]

records = [
    {"id": 1, "user_id": 1, "category_id": 1, "amount": 50.25, "created_at": "2024-06-10T10:00:00"},
    {"id": 2, "user_id": 1, "category_id": 2, "amount": 20.00, "created_at": "2024-06-10T14:30:00"},
    {"id": 3, "user_id": 2, "category_id": 3, "amount": 75.50, "created_at": "2024-06-11T09:15:00"},
    {"id": 4, "user_id": 3, "category_id": 4, "amount": 120.00, "created_at": "2024-06-11T20:45:00"},
    {"id": 5, "user_id": 2, "category_id": 1, "amount": 30.00, "created_at": "2024-06-12T12:00:00"},
    {"id": 6, "user_id": 3, "category_id": 3, "amount": 55.75, "created_at": "2024-06-12T18:20:00"},
    {"id": 7, "user_id": 1, "category_id": 4, "amount": 90.00, "created_at": "2024-06-13T08:10:00"},
    {"id": 8, "user_id": 3, "category_id": 2, "amount": 15.00, "created_at": "2024-06-13T16:00:00"}
]

# Функції для генерації ID
def get_next_id(data):
    return max([item['id'] for item in data], default=0) + 1
