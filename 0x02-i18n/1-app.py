#!/usr/bin/env python3
"""
Then instantiate the Babel object in your app. Store it in a
module-level variable named babel.

In order to configure available languages in our app, you will
create a Config class that has a LANGUAGES class attribute equal
to ["en", "fr"].

Use Config to set Babel’s default locale ("en") and timezone ("UTC").

Use that class as config for your Flask app.
"""

from flask import Flask
from flask_babel import Babel
from config import Config


class config:
    LANGUAGE = ['eng', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE


app = Flask(__name__)
app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)


@app.route(__name__)
def index():
    return render_template('1-index.html')
