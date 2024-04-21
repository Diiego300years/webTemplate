from marshmallow import Schema, fields


class AboutMeSchema(Schema):
    name = fields.Str(required=True)
    profession = fields.Str(required=True)
    description = fields.Str(required=True)
    code = fields.Str(required=True)


class CustomerSchema(Schema):
    customer_email = fields.Email()
    customer_phone = fields.Str()