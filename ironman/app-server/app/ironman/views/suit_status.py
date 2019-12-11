from flask import jsonify

from ironman import ironman
from ironman.models.suit import Suit
from external.session_scope import session_scope


@ironman.route('/suit/<suit_id>/video/status', methods=['GET'])
def suit_status(suit_id):
    with session_scope() as session:
        suit = session.query(Suit).get(suit_id)

    if not suit:
        return jsonify(error='404 Not Found: suit not found'), 404

    return jsonify({'status': suit.status}), 200
