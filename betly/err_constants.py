# -*- coding: utf-8 -*-
"""Error codes for use in the application."""

class Errors(object):
    EMAIL_TAKEN = ('account-email-taken', 'That email is taken')
    PASSWORD_MATCH = ('account-password-confirm', 'Passwords must match')
    USER_NOT_FOUND = ('email-not-found', 'No user with that email exists')
    INCORRECT_PW = ('incorrect-password', 'Incorrect password')
    BET_NAME_TAKEN = ('bet-name-taken', 'That bet name is already taken')
    BET_NAME_MISSING = ('bet-name-missing', 'Bet name is a required field')
    BET_NOT_FOUND = ('bet-not-found', 'No bet with that name exists')
    BET_ALREADY_JOINED = ('bet-already-joined', 'You already joined that bet')
