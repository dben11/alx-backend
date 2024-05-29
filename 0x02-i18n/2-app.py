#!/usr/bin/env python3
"""A function decorator
"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """_sumation_

    Return:
    	   _type_: _description_
    """
    LANGUAGE = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


    # configure the flask app
    app = Flask(__name__)
    app.config.from_object(Config)
    babel = Babel(app)


    @babel.localeselector
    def get_locale():
	"""_sum_

	Returns:
		_type_: _description_
	"""
	return request.accept_language.best_match(app.config['LANGUAGES'])


    @app.route('/')
    def index():
	"""_sum_
	"""
	return render_template('2-index.html')
