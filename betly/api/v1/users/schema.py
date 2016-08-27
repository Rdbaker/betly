# -*- coding: utf-8 -*-
"""User schema."""
from marshmallow_jsonapi import Schema, fields


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    username = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()

    belonging_roles = fields.Relationship(
        related_url='/api/v1/users/{user_id}/roles',
        related_url_kwargs={'user_id': '<id>'},
        include_data=True,
        type_='roles'
    )

    class Meta:
        type_ = 'users'
        strict = True


class Role(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str()

    class Meta:
        type_ = 'roles'
        strict = True
