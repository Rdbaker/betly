# -*- coding: utf-8 -*-
"""User schema."""
from marshmallow import Schema, fields
from betly.api.v1.users.schema import UserSchema


class BetSchema(Schema):
    created_at = fields.DateTime(dump_only=True)
    organizer = fields.Nested(UserSchema)
    name = fields.String()
    description = fields.String()

    class Meta:
        type_ = 'bet'
        strict = True
