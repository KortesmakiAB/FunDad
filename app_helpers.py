from flask import session, g
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


##############################################################################
# API route helper functions

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
    