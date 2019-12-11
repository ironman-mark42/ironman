from os import environ
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from ironman.models.suit import Suit
from external import external


@external.route('/tables_drop')
def tables_drop():
    engine = create_engine('postgres://{}:{}@{}/{}'
                           .format(environ.get('DB_USER'),
                                   environ.get('DB_PASSWORD'),
                                   environ.get('DB_HOST'),
                                   environ.get('DB_NAME')),
                           echo=True)
    Base = declarative_base()
    Suit.__table__.drop(engine)
    return jsonify(engine.table_names())
