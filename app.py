# for setting environment variables (when deploying to Heroku or testing)
import os

from flask import Flask, render_template, redirect, request, flash, session, g, jsonify
import requests
import googlemaps
from secret_keys import API_KEY
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

# from forms import *
# from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgres:///fun_dad'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "sdasdf;lkjl;kj@#$kl;jadfklj")
toolbar = DebugToolbarExtension(app)

# connect_db(app)

CURR_USER_KEY = "curr_user"


##############################################################################
# User signup/login/logout


@app.before_request
def add_user_to_g():
    """If user is logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


##############################################################################
# HTML Routes


@app.route('/', methods = ['GET', 'POST'])
def create_acount():
    """Create new user and add to DB. Redirect to landing page."""

    return "welcome to fun dad"
