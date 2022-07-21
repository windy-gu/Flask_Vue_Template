# author:windy
# datetime:2022/3/3 9:28 AM
# software: PyCharm


from marshmallow_sqlalchemy import SQLAlchemySchema

from marshmallow import fields
from app.author.models import Author
from app.books.schema import BookSchema
from app import db


class AuthorSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Author
        sqla_session = db.session

    ID = fields.Number(dump_only=True)
    NAME = fields.String(required=True)
    PSEUDONYM = fields.String(required=True)
    DELETED = fields.Number(dump_only=True)
    # books = fields.Nested(BookSchema, many=True, only=['title', 'year', 'id'])
