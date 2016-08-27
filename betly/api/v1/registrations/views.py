# -*- coding: utf-8 -*-
"""Registraion views."""
from flask import Blueprint
from flask_login import login_user
from webargs import fields
from webargs.flaskparser import use_args
from werkzeug.exceptions import BadRequest

from betly.err_constants import Errors
from betly.api.v1.users.models import User, Account
from betly.api.v1.users.schema import UserSchema

blueprint = Blueprint('registrations', __name__, url_prefix='/api/v1/registrations')
USER_SCHEMA = UserSchema()


REGISTRATION_ARGS = {
    'email': fields.Str(required=True, validate=lambda val: len(val) > 0 ),
    'password': fields.Str(required=True, validate=lambda val: len(val) >= 8 ),
    'confirmpw': fields.Str(required=True)
}


@blueprint.route('/', methods=['POST'], strict_slashes=False)
@use_args(REGISTRATION_ARGS)
def sign_up(args):
    acct = Account.query.filter(Account.email == args['email']).first()
    if acct is not None:
        raise BadRequest(Errors.EMAIL_TAKEN)
    if args['password'] != args['confirmpw']:
        raise BadRequest(Errors.PASSWORD_MATCH)
    acct = Account.create(email=args['email'], password=args['password'])
    user = acct.user
    login_user(user)
    return USER_SCHEMA.dumps(user).data
