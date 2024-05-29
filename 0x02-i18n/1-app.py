#!/usr/bin/env python3
"""
Use that class as config for your Flask app.
"""

from flask import Flask, render_template
from flask_babel import Babel


class config(object):
    """__summary__

    Retuns:
    	   _type_: _description_

    """
    LANGUAGE = ['eng', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# configure the flask app
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """_summary_
    """
    return render_template('1-index.html')
