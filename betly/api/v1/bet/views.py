from flask import Blueprint, request
from flask_login import login_required, current_user
from webargs import fields
from webargs.flaskparser import use_args
from werkzeug.exceptions import BadRequest

from betly.api.v1.bet.models import Bet, UserBet
from betly.api.v1.bet.schema import BetSchema

blueprint = Blueprint('bet', __name__, url_prefix='/api/v1/bet')
BET_SCHEMA = BetSchema()


@blueprint.route('/list', methods=['GET'], strict_slashes=False)
def list_bets(args=None):
    bets = Bet.query.all()
    return BET_SCHEMA.dumps(bets).data


@blueprint.route('/', methods=['POST'], strict_slashes=False)
def create_bet():
    bet_data = BET_SCHEMA.load(request.json)
    bet_data.data['organizer'] = current_user
    Bet.create(**bet_data.data)
    return bet_data.data
