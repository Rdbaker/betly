# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt
import uuid

from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID

from betly.models import Column, Model, SurrogatePK, db, reference_col, relationship
from betly.extensions import bcrypt


class Account(SurrogatePK, Model):
    """Logic to tie account management to a user."""

    __tablename__ = 'account'
    email = Column(db.String(80), unique=True, nullable=False)
    #: The hashed password
    password = Column(db.String(128), nullable=True)
    user = relationship('User', uselist=False, back_populates='account')

    def __init__(self, email, password, **kwargs):
        db.Model.__init__(self, email=email, **kwargs)
        self.set_password(password)
        self.user = User.create(email=email)

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    def __repr__(self):
        """Get the string version of this model."""
        return '<Account({email!r})>'.format(email=self.email)


class User(UserMixin, Model):
    """A user of the app."""

    __tablename__ = 'user'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(db.String(80), unique=True, nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)
    account_id = Column(db.Integer, db.ForeignKey('account.id'))
    account = relationship('Account', back_populates='user')
    user_bets = relationship('UserBet', backref='user', cascade='delete')

    def get_id(self):
        """Return a unique identifier for this user."""
        return self.email

    @property
    def full_name(self):
        """Full user name."""
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({email!r})>'.format(email=self.email)
