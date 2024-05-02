from marshmallow import Schema, fields


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
