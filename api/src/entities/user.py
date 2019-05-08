from sqlalchemy import Column, String

from .entity import Entity, Base

from marshmallow import Schema, fields

class User(Entity, Base):
    __tablename__ = 'users'

    name = Column(String)
    lastname = Column(String)
    description = Column(String)

    def __init__(self, name, lastname, description, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        # self.lastname = lastname
        self.description = description


class UserSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    lastname = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
