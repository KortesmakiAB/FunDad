# for setting environment variables (when deploying to Heroku or testing)
import os

from flask import Flask, render_template, redirect, request, flash, session, g, jsonify, url_for

from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from forms import *
from models import *
from app_helpers import *
from secret_keys import API_MAP_KEY

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgres:///fun_dad'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'sdasdf;lkjl;kj@#$kl;jadfklj')

toolbar = DebugToolbarExtension(app)

connect_db(app)

# HTTPS for development purposes
# $ pip install pyopenssl
# $ flask run --cert=adhoc
if __name__ == "__main__":
    app.run(ssl_context='adhoc')
# https://stackoverflow.com/questions/29458548/can-you-add-https-functionality-to-a-python-flask-web-server


CURR_USER_KEY = "curr_user"


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

    # if logged in, redirect
    if g.user:
        return redirect(url_for('display_destinations'))
        
    return render_template('home-anon.html')


##############################################################################
# login, logout, & signup routes

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    """Authenticate user or serve login form."""

    form = UserLoginForm()

    if form.validate_on_submit():
        returning_user = User.authenticate(form.username_email.data, form.password.data)

        if returning_user:
            do_login(returning_user)
            flash(f'Welcome back to FUN DAD, {returning_user.first_name}!', 'success')

            return redirect(url_for('display_destinations'))

        flash('Invalid Username/Password combination', 'danger')

    return render_template('users/login.html', form=form)


@app.route('/logout')
def logout_user():
    """Authenticate user or serve login form."""
    
    do_logout()

    return redirect(url_for('landing_page'))


@app.route('/signup', methods=['GET', 'POST'])
def create_account():
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
            flash('Username/Email already taken', 'danger')

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

    if check_authorization():
        return redirect(url_for('landing_page'))

    user = User.query.get(g.user.id)

    return render_template('destinations/destinations.html', user=user)


@app.route('/destinations/checkin', methods=['GET', 'POST'])
def handle_checkin():
    """GET: Serve form for user to check in at a destination.
    POST: Add a new Visit."""

    if check_authorization():
        return redirect(url_for('landing_page'))

    form = CheckInForm()
    user = User.query.get(g.user.id)
    destinations = [(dest.id, dest.name) for dest in user.destinations]
    form.destination.choices = destinations

    if form.validate_on_submit():
        dest_id = form.destination.data

        user_dest = db.session.query(UserDestination).filter_by(user_id=g.user.id, dest_id=dest_id).first()
        
        visit = Visit(usr_dest=user_dest.id)
        db.session.add(visit)
        db.session.commit()
        
        dest = db.session.query(Destination).filter_by(id=dest_id).first()

        flash(f'Welcome back to {dest.name}!', 'success')

        return redirect(url_for('display_destinations'))

    return render_template('destinations/checkin.html', user=user, form=form)


@app.route('/destinations/new', methods=['GET', 'POST'])
def add_new_destination():
    """Extract form data then geocode (lookup coordinates and place_id). 
    Add new destination to destinations table.
    Add new user_destination to users_destinations table.
    Add visit to visits table."""

    if check_authorization():
        return redirect(url_for('landing_page'))

    form = NewDestinationForm()

    if form.validate_on_submit():
        name = form.name.data
        address = form.address.data

        resp = geocode_address((name + address))
        
        try:
            dest = Destination(name=name, 
                            place_id=resp['place_id'], 
                            latitude=resp['latitude'], 
                            longitude=resp['longitude'])
            db.session.add(dest)
            db.session.commit()

            user_dest = UserDestination(user_id=g.user.id, dest_id=dest.id)
            db.session.add(user_dest)
            db.session.commit()

            visit = Visit(usr_dest=user_dest.id)
            db.session.add(visit)
            db.session.commit()
            
            flash('Destination successfully added. You are checked in!', 'success')

            return redirect(url_for('display_destinations'))

        except TypeError:
            flash('Error: unable to add new destination.', 'warning')
            
            return redirect(url_for('add_new_destination'))
        
        except IntegrityError:
            flash('Error: must enter a unique address.', 'warning')

            return redirect(url_for('add_new_destination'))

    user = User.query.get(g.user.id)

    return render_template('destinations/dest-new.html', user=user, form=form)


@app.route('/destinations/<int:id>', methods=['GET', 'POST'])
def show_destination_details(id):
    """
    GET: From Google Places API, show destination info: Name, website, hours, pics(adjustable number from 0-10), and display form to edit name of destination as  given by user.
    POST: Update name of destination as  given by user.
    """

    if check_authorization():
        return redirect(url_for('landing_page'))
    
    dest = Destination.query.get_or_404(id)

    form = EditDestinationForm(obj=dest)

    if form.validate_on_submit():
        dest.name = form.name.data
        db.session.commit()
        
        flash('Destination updated.', 'success')
        
        return redirect(url_for('display_destinations'))


    dest_info = get_dest_info(dest.place_id)

    try:
        photo_urls = get_photo_urls(dest_info['photo_ids'])
        max_imgs = 5 if len(photo_urls) >= 5 else len(photo_urls) - 1

    except KeyError:
        photo_urls = None
        max_imgs = None

    user = User.query.get(g.user.id)

    return render_template('destinations/dest-detail.html', user=user, dest_info=dest_info, photos=photo_urls, max_imgs=max_imgs, form=form, id=id)


@app.route('/destinations/<int:id>/delete', methods=['POST'])
def delete_destination(id):
    """Delete a destination"""

    if check_authorization():
        return redirect(url_for('landing_page'))

    dest = Destination.query.get_or_404(id)

    db.session.delete(dest)
    db.session.commit()

    flash('Destination deleted.', 'danger')
        
    return redirect(url_for('display_destinations'))
        

##############################################################################
# Map View routes

@app.route('/map-view')
def display_map_view():
    """Display HTML for map view page."""

    if check_authorization():
        return redirect(url_for('landing_page'))

    user = User.query.get(g.user.id)

    return render_template('map-view.html', user=user, key=API_MAP_KEY)


##############################################################################
##############################################################################
# Begin API routes

error = {

}

@app.route('/api/travel-times')
def get_travel_times_response():
    """Call Google Maps "distance matrix" API for travel times.
    Include users coordinates from AJAX request and coordinates from the destinations where the logged-in user has visited. Google matrix API prefers coordinates over physical address. 
    Create a response dict where destination-ids are the keys and travel-times are the values."""
    
    if check_API_authorization():
        return jsonify(messages['unauth'])
        
    user = User.query.get_or_404(g.user.id)
    dest_coords = [(dest.latitude, dest.longitude) for dest in user.destinations]
    
    travel_times = get_travel_times(request, dest_coords)
    
    if travel_times:
        trvl_time_dict = {user.destinations[i].id : travel_times[i] for i in range(len(user.destinations))}
    else:
        trvl_time_dict = {user.destinations[i].id : 'n/a' for i in range(len(user.destinations))}

    return jsonify(trvl_time_dict)


@app.route('/api/coordinates')
def get_destination_data():
    """Get data for current users previous destinations."""

    if check_API_authorization():
        return jsonify(messages['unauth'])

    user = User.query.get_or_404(g.user.id)

    destinations_data = make_dest_dicts(user)
    
    return jsonify(destinations_data)
    

@app.route('/api/destinations/get-address')
def reverse_geocode_address():
    """Accept coords. Call Google Maps API reverse geocode to get physical address."""

    if check_API_authorization():
        return jsonify(messages['unauth'])
    
    obj = {
        'errors':[]
    }
    
    resp = get_reverse_geocode(request)

    if resp['address']:
        obj['address'] = resp['address']
    else:
        obj['address'] = ''
        obj['errors'].append('Address unavailable.')
        
        

    if resp['place_id']:
        obj['place_id'] = resp['place_id']
    else:
        obj['place_id'] = None
        obj['errors'].append('Place id unavailable.')
    
    return jsonify(obj) 


    