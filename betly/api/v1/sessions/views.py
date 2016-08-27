# -*- coding: utf-8 -*-
"""Session views."""
from flask import Blueprint, jsonify
from flask_login import login_required, logout_user, login_user
from webargs import fields
from webargs.flaskparser import use_args
from werkzeug.exceptions import BadRequest, NotFound

from betly.err_constants import Errors
from betly.api.v1.users.models import User, Account
from betly.api.v1.users.schema import UserSchema

blueprint = Blueprint('sessions', __name__, url_prefix='/api/v1/sessions')
USER_SCHEMA = UserSchema()


SESSION_ARGS = {
    'email': fields.Str(required=True),
    'password': fields.Str(required=True)
}


@blueprint.route('/', methods=['POST'], strict_slashes=False)
@use_args(SESSION_ARGS)
def sign_in(args):
    acct = Account.query.filter(Account.email == args['email']).first()
    if acct is None:
        raise NotFound(Errors.USER_NOT_FOUND)
    if not acct.check_password(args['password']):
        raise BadRequest(Errors.INCORRECT_PW)
    login_user(acct.user)
    return USER_SCHEMA.dumps(acct.user).data


@blueprint.route('/', methods=['DELETE'], strict_slashes=False)
@login_required
def sign_out():
    logout_user()
    res = jsonify(message='Logout successful')
    res.status_code = 204
    return res
