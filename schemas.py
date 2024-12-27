from marshmallow import Schema, fields

class CurrencySchema(Schema):
    id = fields.Int(dump_only=True)
    code = fields.Str(required=True)
    name = fields.Str(required=True)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    default_currency_id = fields.Int()

class ExpenseSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    amount = fields.Float(required=True)
    currency_id = fields.Int()
