from flask import session, g, flash
from datetime import datetime

from secret_keys import API_KEY
import googlemaps

gmaps = googlemaps.Client(key=API_KEY)

CURR_USER_KEY = "curr_user"


##############################################################################
# User login/logout helper functions

def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


def check_authorization():
    """Is a user logged in? If not, return True."""

    if not g.user:
        flash('Access unauthorized.', 'danger')

        return True


##############################################################################
# API global variable

messages = {
    'unauth' : {'unauthorized': 'Access unauthorized.'},
}


##############################################################################
# API route helper functions

def check_API_authorization():
    """Is a user logged in? If not, return True."""

    if not g.user:
        return True


def get_travel_times(request, dest_coords):
    """Call Google Maps "distance matrix" API for travel times.
    Include users coordinates from AJAX request and coordinates from the destinations where the logged-in user has visited. 
    Google matrix API prefers coordinates over physical address.  """
    
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    now = datetime.now()
    dist_time = gmaps.distance_matrix(origins=(lat, lng), 
                                        destinations=dest_coords,
                                        mode='driving',
                                        departure_time=now,
                                        traffic_model='best_guess')

    return [elmt['duration_in_traffic']['text'] for elmt in dist_time['rows'][0]['elements']]
    

def make_dest_dicts(user):
    """Make dictionary containing data for current users previous destinations."""

    return [{
        'name': dest.name,
        'coords': {'lat': dest.latitude, 'lng': dest.longitude},
        'place_id': dest.place_id,
    } for dest in user.destinations]


def geocode_address(address):
    """Use address to get latitude, longitude, place_id."""

    resp = gmaps.geocode(address)

    return {
        'place_id': resp[0]['place_id'],
        'latitude': resp[0]['geometry']['location']['lat'],
        'longitude': resp[0]['geometry']['location']['lng']        
    }


def get_reverse_geocode(request):
    """Use coordinates to get street address and place id via Google Reverse Geocoding API."""
    
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    user_coords = f'{lat},{lng}'

    address = gmaps.reverse_geocode(latlng=user_coords,
                                    result_type='street_address')
                                    # location_type='ROOFTOP')
    
    return {
        'address': address[0]['formatted_address'],
        'place_id': address[0]['formatted_address']
    }