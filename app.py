# for setting environment variables (when deploying to Heroku or testing)
import os

from flask import Flask, render_template, redirect, request, flash, session, g, jsonify
import requests

from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from forms import *
from models import *
from app_helpers import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgres:///fun_dad'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "sdasdf;lkjl;kj@#$kl;jadfklj")
toolbar = DebugToolbarExtension(app)

connect_db(app)

# HTTPS for development purposes
# $ pip install pyopenssl
# $ flask run --cert=adhoc
if __name__ == "__main__":
    app.run(ssl_context='adhoc')
# https://stackoverflow.com/questions/29458548/can-you-add-https-functionality-to-a-python-flask-web-server


# CURR_USER_KEY = "curr_user"


##############################################################################
##############################################################################
# Begin HTML routes

@app.before_request
def add_user_to_g():
    """If user is logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


@app.route('/', methods=['GET', 'POST'])
def landing_page():
    """Display landing page"""

    return render_template('home-anon.html')


##############################################################################
# login & signup routes

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    """Authenticate user or serve login form."""

    form = UserLoginForm()

    if form.validate_on_submit():
        returning_user = User.authenticate(form.username_email.data, form.password.data)

        if returning_user:
            do_login(returning_user)
            flash(f'Welcome back to FUN DAD, {returning_user.first_name}!', 'success')

            return redirect('/destinations')

        flash('Invalid Username/Password combination', 'danger')

    return render_template('users/login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def create_acount():
    """Create new user and add to DB. Redirect to landing page."""

    form = UserSignupForm()

    if form.validate_on_submit():
        try:
            first_name = form.first_name.data
            last_name = form.last_name.data
            username_email = form.username_email.data
            password = form.password.data

            new_user = User.signup(first_name, last_name, username_email, password)

            db.session.commit()

        except IntegrityError:
            flash("Username/Email already taken", 'danger')
            return render_template('users/signup.html', form=form)

        do_login(new_user)

        return redirect('/destinations')

    else:

        return render_template('/users/signup.html', form=form)


##############################################################################
# Destinations routes

@app.route('/destinations')
def display_destinations():
    """Render page displaying table of:
         park name, number of vists, date of last visit, and travel time."""

    if not g.user:
        flash('Access unauthorized.', 'danger')

        return redirect('/')

    user = User.query.get(g.user.id)

    return render_template('destinations/destinations.html', user=user)



##############################################################################
##############################################################################
# Begin API routes

@app.route('/api/travel-times')
def get_travel_times_response():
    """Call Google Maps "distance matrix" API for travel times.
    Include users coordinates from AJAX request and coordinates from the destinations where the logged-in user has visited. Google matrix API prefers coordinates over physical address. 
    Create a response dict where destination-ids are the keys and travel-times are the values."""
    
    if not g.user:
        flash('Access unauthorized.', 'danger')

        return redirect('/')
    
    user = User.query.get_or_404(g.user.id)
    dest_coords = [(dest.latitude, dest.longitude) for dest in user.destinations]
    
    travel_times = get_travel_times(request, dest_coords)
    trvl_time_dict = {user.destinations[i].id : travel_times[i] for i in range(len(user.destinations))}

    return jsonify(trvl_time_dict)
    