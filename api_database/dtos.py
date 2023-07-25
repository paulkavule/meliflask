from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields
from models import AppProduct

class AppProductDto(SQLAlchemyAutoSchema):
    class Meta:
        model = AppProduct
        load_instance = True

    name = auto_field()
    price = auto_field()
    description = auto_field()

