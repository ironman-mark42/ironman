from flask import jsonify

from ironman import ironman
from ironman.models.suit import Suit
from external.session_scope import session_scope


@ironman.route('/suit/<suit_id>', methods=['GET'], strict_slashes=False)
def suit_read(suit_id):
    with session_scope() as session:
        suit = session.query(Suit).get(suit_id)

    if not suit:
        return jsonify(error='404 Not Found: suit not found'), 404

    return jsonify(suit.to_dict()), 200
