# -*- coding: utf-8 -*-
"""User schema."""
from marshmallow import Schema, fields, validates
from werkzeug.exceptions import BadRequest

from .models import Bet
from betly.err_constants import Errors
from betly.api.v1.users.schema import UserSchema


class BetSchema(Schema):
    created_at = fields.DateTime(dump_only=True)
    organizer = fields.Nested(UserSchema, dump_only=True)
    name = fields.String(required=True)
    description = fields.String()

    class Meta:
        type_ = 'bet'
        strict = True

    @validates('name')
    def validate_name(self, value):
        if not value:
            raise BadRequest(Errors.BET_NAME_MISSING)
        candidate_url_name = Bet.create_url_name(value)
        bet = Bet.query.filter(Bet.url_name == candidate_url_name)
        if bet is not None:
            raise BadRequest(Errors.BET_NAME_TAKEN)
        bet = Bet.query.filter(Bet.name == value)
        if bet is not None:
            raise BadRequest(Errors.BET_NAME_TAKEN)
