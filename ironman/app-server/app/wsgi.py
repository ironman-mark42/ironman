from os import environ

from flask import Flask

from ironman import ironman
from external import external


app = Flask(__name__)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(external, url_prefix='/api/db')
app.register_blueprint(ironman, url_prefix='/')
