# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound

from .models import User
from .schema import UserSchema
from betly.err_constants import Errors

blueprint = Blueprint('users', __name__, url_prefix='/api/v1/users')
USER_SCHEMA = UserSchema()


# TODO: make this admin-only in the future
@blueprint.route('/', methods=['GET'], strict_slashes=False)
@login_required
def list_users(args=None):
    """List the users."""
    users = User.query.all()
    return USER_SCHEMA.dumps(users, many=True).data


@blueprint.route('/me', methods=['GET'], strict_slashes=False)
@login_required
def show_me(args=None):
    """Return the current user."""
    return USER_SCHEMA.dumps(current_user).data


@blueprint.route('/<string:email>', methods=['GET'], strict_slashes=False)
@login_required
def show_user_by_email(email):
    """Show a user profile by the email."""
    user = User.query.filter(User.email == email).first()
    if user is None:
        raise NotFound(Errors.USER_NOT_FOUND)
    return USER_SCHEMA.dumps(user).data
