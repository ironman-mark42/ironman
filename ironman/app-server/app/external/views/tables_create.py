from os import environ

from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from ironman.models.suit import Suit
from external import external
from external.session_scope import session_scope


@external.route('/tables_create')
def tables_create():
    engine = create_engine('postgres://{}:{}@{}/{}'
                           .format(environ.get('DB_USER'),
                                   environ.get('DB_PASSWORD'),
                                   environ.get('DB_HOST'),
                                   environ.get('DB_NAME')),
                           echo=True)
    Base = declarative_base()
    Suit.__table__.create(engine)

    # populate database with test data
    with session_scope() as session:
        suit = Suit()
        suit.model = 'mk1'
        suit.status = 'Destroyed in Escape from the Cave.'
        suit.first_appearance = 'Iron Man'
        suit.image_file = 'mk1.jpg'
        suit.video_file = 'test.gif'
        suit.description = '''The first Iron Man suit, the Mark I was created from Jericho missile parts while Tony Stark was being held captive in a cave in Afghanistan. The original Hall of Armors created by Tony after the first Iron Man film contained the armors Mark I to Mark IV, before being upgraded to house Mark I through Mark VII.'''
        session.add(suit)

    with session_scope() as session:
        suit = Suit()
        suit.model = 'mk2'
        suit.status = 'Destroyed by the Mandarin'
        suit.first_appearance = 'Iron Man'
        suit.image_file = 'mk2.jpg'
        suit.video_file = 'test.gif'
        suit.description = '''Designed as a prototype, this suit was used to explore flight potential and had almost no weapons, before quickly giving way to the Mark III. It was temporarily confiscated by the U.S. Military and was converted into the War Machine Mark I before Tony got it back and reverted it to the Mark II.'''
        session.add(suit)

    with session_scope() as session:
        suit = Suit()
        suit.model = 'mk3'
        suit.status = 'Destroyed by the Mandarin'
        suit.first_appearance = 'Iron Man'
        suit.image_file = 'mk3.jpg'
        suit.video_file = 'test2.gif'
        suit.description = '''This was the first armor to feature the iconic red and gold design.'''
        session.add(suit)

    with session_scope() as session:
        suit = Suit()
        suit.model = 'mk4'
        suit.status = 'Destroyed by the Mandarin'
        suit.first_appearance = 'Iron Man 2'
        suit.image_file = 'mk4.jpg'
        suit.video_file = 'test.gif'
        suit.description = '''After the Mark III took heavy damage in Tony’s fight with the Iron Mongor, this suit was built as a direct replacement, with only a few minor changes from the previous model.'''
        session.add(suit)

    with session_scope() as session:
        suit = Suit()
        suit.model = 'mk5'
        suit.status = 'Destroyed by the Mandarin'
        suit.first_appearance = 'Iron Man 2'
        suit.image_file = 'mk4.jpg'
        suit.video_file = 'test.gif'
        suit.description = '''The Mark V was an emergency suit, designed to be portable by collapsing into a briefcase.'''
        session.add(suit)

    return jsonify(engine.table_names())
