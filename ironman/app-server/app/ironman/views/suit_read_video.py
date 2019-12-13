from flask import jsonify

from ironman import ironman
from ironman.models.suit import Suit
from external.session_scope import session_scope


@ironman.route('/suit/<suit_id>/description', methods=['GET'])
def suit_read_video(suit_id):
    with session_scope() as session:
        suit = session.query(Suit).get(suit_id)

    if not suit:
        return jsonify(error='404 Not Found: suit not found'), 404

    return jsonify({'description': suit.description}), 200
