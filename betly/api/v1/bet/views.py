import uuid

from flask import Blueprint, request
from flask_login import login_required, current_user
from webargs import fields
from webargs.flaskparser import use_args
from werkzeug.exceptions import BadRequest, NotFound

from betly.err_constants import Errors
from betly.api.v1.bet.models import Bet, UserBet
from betly.api.v1.bet.schema import BetSchema

blueprint = Blueprint('bet', __name__, url_prefix='/api/v1/bets')
BET_SCHEMA = BetSchema()

def get_bet_from_guid(guid):
    try:
        uid = uuid.UUID(guid)
    except:
        raise BadRequest(Errors.BAD_GUID)
    bet = Bet.query.filter(Bet.guid == guid).first()
    if bet is None:
        raise NotFound(Errors.BET_NOT_FOUND)
    return bet


@blueprint.route('/list', methods=['GET'], strict_slashes=False)
def list_bets(args=None):
    bets = Bet.query.all()
    return BET_SCHEMA.dumps(bets, many=True).data


@blueprint.route('/', methods=['GET'], strict_slashes=False)
def restful_list_bets(args=None):
    return list_bets(args)


@blueprint.route('/', methods=['POST'], strict_slashes=False)
@login_required
def create_bet():
    bet_data = BET_SCHEMA.load(request.json)
    bet_data.data['organizer'] = current_user
    bet = Bet.create(**bet_data.data)
    return BET_SCHEMA.dumps(bet).data


@blueprint.route('/<string:uid_hex>', methods=['GET'], strict_slashes=False)
def show_bet(uid_hex):
    bet = get_bet_from_guid(uid_hex)
    return BET_SCHEMA.dumps(bet).data


@blueprint.route('/<string:uid_hex>', methods=['DELETE'], strict_slashes=False)
@login_required
def destroy_bet(uid_hex):
    bet = get_bet_from_guid(uid_hex)
    if bet.organizer == current_user:
        bet.delete()
        return ('', 204)
    else:
        raise Forbidden(Errors.NOT_BET_ORGANIZER)


@blueprint.route('/<string:uid_hex>/participants/me', methods=['POST'], strict_slashes=False)
@login_required
def join_bet(name):
    # make sure the bet exists
    bet = Bet.query.filter(Bet.name == name).first()
    if bet is None:
        raise NotFound(Errors.BET_NOT_FOUND)

    # see if a user <-> bet association already exists
    ub = UserBet.query.filter(UserBet.user==current_user, UserBet.bet==bet).first()
    if ub is not None:
        raise BadRequest(Errors.BET_ALREADY_JOINED)
    else:
        ub = UserBet.create(user=current_user, bet=bet)
        return BET_SCHEMA.dumps(bet).data, 201
