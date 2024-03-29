# -*- coding: utf-8 -*-
"""Bet models."""
import datetime as dt
import uuid

from sqlalchemy.dialects.postgresql import UUID


from betly.models import Column, Model, db, relationship, reference_col
from betly.api.v1.users.models import User


class Bet(Model):
    """The Bet that is being made between people"""

    __tablename__ = 'bet'

    guid = Column(UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid.uuid4)
    organizer_id = reference_col('user')
    organizer = relationship('User', backref='bets_as_organizer')
    name = Column(db.Text(), nullable=False, unique=True)
    url_name = Column(db.String(100), nullable=False, unique=True)
    description = Column(db.Text(), nullable=True)
    bet_type = Column(db.Text(), nullable=True)
    options = Column(db.Text(), nullable=True)
    amount = Column(db.Float(precision=2), nullable=True)
    bet_status = Column(db.Text(), nullable=True)
    outcome_option_value = Column(db.Text(), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    user_bets = relationship('UserBet', backref='bet', cascade='delete')

    deleted_at = Column(db.DateTime, nullable=True, default=dt.datetime.utcnow)

    def __init__(self, name, **kwargs):
        """Create instance."""
        url_name = self.create_url_name(name)
        db.Model.__init__(self, name=name, url_name=url_name, **kwargs)

    @classmethod
    def create_url_name(cls, bet_name):
        return bet_name.lower().replace(' ', '-')

    @property
    def participants(self):
        return [ub.user for ub in self.user_bets]


class UserBet(Model):
    """Thsi is an entry for a user into a bet"""

    __tablename__ = "user_bet"

    user_guid = reference_col('user', primary_key=True)
    user = relationship('User', backref='user_bets')
    bet_guid = reference_col('bet', pk_name='guid', primary_key=True)
    bet = relationship('Bet', backref='user_bets')
