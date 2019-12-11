from flask import render_template

from ironman import ironman
from ironman.models.suit import Suit
from external.session_scope import session_scope


@ironman.route('/', methods=['GET'])
def index():
    with session_scope() as session:
        suits = session.query(Suit).all()

    return render_template('index.html', suits=[suit.to_dict() for suit in suits])
