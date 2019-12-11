from flask import jsonify

from ironman import ironman
from ironman.models.suit import Suit
from external.session_scope import session_scope


@ironman.route('/suits', methods=['GET'])
def suit_read_all():
    with session_scope() as session:
        suits = session.query(Suit).all()

    return jsonify({"suits": [suit.to_dict() for suit in suits]})
