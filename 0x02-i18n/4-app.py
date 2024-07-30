#!/usr/bin/env python3
"""A Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Configuration with the LANGUAGES attribute"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index_page():
    """This is the home and index page ('/')"""
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """Selects a language translation to use for request.
    """
    requested_locale = request.args.get('locale')

    if requested_locale and requested_locale in Config.LANGUAGES:
        return requested_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])
