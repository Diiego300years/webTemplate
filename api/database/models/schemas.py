from marshmallow import Schema, fields
from marshmallow.validate import Range


class AboutMeSchema(Schema):
    name = fields.Str(required=True)
    profession = fields.Str(required=True)
    description = fields.Str(required=True)
    code = fields.Integer(required=True)


class CustomerSchema(Schema):
    customer_email = fields.Email()
    customer_phone = fields.Str()


class DefaultErrorSchema(Schema):
    code = fields.Integer()
    status = fields.String()
    message = fields.String()
    errors = fields.Dict(keys=fields.Str(), values=fields.Str())

# make scgema for customer data with concact email and phone number

class IntegerInputSchema(Schema):
    value = fields.Integer(required=True, validate=Range(min=0))  # przykład z minimalną wartością 0
