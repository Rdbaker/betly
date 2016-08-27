# -*- coding: utf-8 -*-
"""Error codes for use in the application."""

class Errors(object):
    EMAIL_TAKEN = ('account-email-taken', 'That email is taken')
    PASSWORD_MATCH = ('account-password-confirm', 'Passwords must match')
    USER_NOT_FOUND = ('email-not-found', 'No user with that email exists')
    INCORRECT_PW = ('incorrect-password', 'Incorrect password')
    BET_NAME_TAKEN = ('bet-name-taken', 'That bet name is already taken')
