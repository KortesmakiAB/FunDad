from flask import session, g, flash
from datetime import datetime
import requests

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

    try:
        return [elmt['duration_in_traffic']['text'] for elmt in dist_time['rows'][0]['elements']]
        
    except KeyError:
        return None
    

def make_dest_dicts(user):
    """Make dictionary containing data for current users previous destinations."""

    return [{
        'name': dest.name,
        'coords': {'lat': dest.latitude, 'lng': dest.longitude},
        'place_id': dest.place_id,
    } for dest in user.destinations]


def geocode_address(name_address):
    """Use address to get latitude, longitude, place_id."""

    resp = gmaps.geocode(name_address)

    try: 
        place_id = resp[0]['place_id']
    except KeyError:
        place_id = None

    try: 
        latitude = resp[0]['geometry']['location']['lat']
    except KeyError:
        latitude = None

    try: 
        longitude = resp[0]['geometry']['location']['lng']        
    except KeyError:
        longitude = None

    return {
        'place_id': place_id,
        'latitude': latitude,
        'longitude': longitude 
    }


def get_reverse_geocode(request):
    """Use coordinates to get street address and place id via Google Reverse Geocoding API."""
    
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    user_coords = f'{lat},{lng}'

    rev_address = gmaps.reverse_geocode(latlng=user_coords,
                                    result_type='street_address')

    try:
        address = rev_address[0]['formatted_address']
    except KeyError:
        address = None

    try:
        place_id = rev_address[0]['place_id']
    except KeyError:
        place_id = None

    return {
        'address': address,
        'place_id': place_id
    }


def get_dest_info(place_id):
    """Use a place id to:
    fetch a maximum of 10 photos,
    fetch place name,"""

    fields = ['name', 'photo', 'place_id', 'opening_hours', 'website']
    place = gmaps.place(place_id=place_id, fields=fields)
   
    try:
        name = place['result']['name']
    except KeyError:
        name = 'n/a'

    try:
        photo_ids = [photo['photo_reference'] for photo in place['result']['photos']]
    except KeyError:
        photo_ids = None

    try:
        website = place['result']['website']
    except KeyError:
        website = 'n/a'

    try:
        hours = place['result']['opening_hours']['weekday_text']
    except KeyError:
        hours = None
    
    return {
        'name': name,
        'photo_ids': photo_ids,
        'website': website,
        'hours': hours
    }
  

def get_photo_urls(photo_ids):
    """Use list of photo ids to call Google Places Photo API and get a list of photos urls."""

    photo_urls = []

    for photo_id in photo_ids:
        photo = requests.get('https://maps.googleapis.com/maps/api/place/photo',
                    params={
                        "key": API_KEY,
                        "photoreference": photo_id,
                        "maxheight": 300
                    })
        
        photo_urls.append(photo.url)
    
    return photo_urls


def get_dad_joke():
    """Fetch dad joke."""

    headers = {
    'x-rapidapi-key': "193bf7374amshc41094bb7b0edddp12f315jsn8f3e99c0f3f5",
    'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
    }
    
    resp = requests.get('https://dad-jokes.p.rapidapi.com/random/joke', headers=headers)
    
    joke_resp = resp.json()

    try:
        return {
            'setup': joke_resp['body'][0]['setup'],
            'punchline': joke_resp['body'][0]['punchline'],
        }
    except KeyError:
        return {
            'error': 'Dad joke not available.'
        }

