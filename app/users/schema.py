# author:windy
# datetime:2022/3/3 11:23 AM
# software: PyCharm

from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields
from app.users.models import User
from app import db


class UserSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = User
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
