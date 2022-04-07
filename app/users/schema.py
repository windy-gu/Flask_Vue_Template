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

    USER_NO = fields.Number(dump_only=True)
    USER_NAME = fields.String(required=True)
    PASSWORD = fields.String(required=True)
