from flask import session, g
from datetime import datetime

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

def get_travel_times(lat, lng, dest_coords):
    """TODO"""
    
    now = datetime.now()
    resp = gmaps.distance_matrix(origins=(lat, lng), 
                                        destinations=dest_coords,
                                        mode='driving',
                                        departure_time=now,
                                        traffic_model='best_guess')

    # iterate over dist_time['rows'][0]['elements']
    # return a json-ready response
    dist_time['rows'][0]['elements'][ITERATE_ME]['duration_in_traffic']['text']
    raise
    import pdb
    pdb.set_trace()