# -*- coding: utf-8 -*-
"""User schema."""
from marshmallow import Schema, fields


class UserSchema(Schema):
    created_at = fields.DateTime(dump_only=True)
    email = fields.Str()

    class Meta:
        type_ = 'users'
        strict = True
