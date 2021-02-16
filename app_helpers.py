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

    return [elmt['duration_in_traffic']['text'] for elmt in dist_time['rows'][0]['elements']]
    

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
    
    return {
        'address': address[0]['formatted_address'],
        'place_id': address[0]['formatted_address']
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
        photo_ids = 'n/a'
    try:
        website = place['result']['website']
    except KeyError:
        website = 'n/a'
    try:
        hours = place['result']['opening_hours']['weekday_text']
    except KeyError:
        hours = 'n/a'
    
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




# TODO remove this block
# for sizing exerimentation 
# photo_urls = ['https://lh3.googleusercontent.com/p/AF1QipNhYrPCBGVFhaLRNEHM4s6YItShEPbImEHKZllA=s1600-h400', 'https://lh3.googleusercontent.com/p/AF1QipNTHS9UNRd724XQmP4XGhenbmZn0Pm_48MfHYF1=s1600-h400', 'https://lh3.googleusercontent.com/p/AF1QipO5HP2ucy2Th3FiXgQmm5t4Y9svDmM5wodwy1M9=s1600-h400', 'https://lh3.googleusercontent.com/p/AF1QipMuDwNKRIdkMd9ZJy-PoZUEcSC3z8PPY2ToXexA=s1600-h400', 'https://lh3.googleusercontent.com/p/AF1QipMOm5-AIFo-ALzjK3_smPudMYgH47QHIV04FOhf=s1600-h400', 'https://lh3.googleusercontent.com/p/AF1QipM5ClrII8uIS_fyjOM57FH_GkEcF4cddhp1H1PY=s1600-h400', 'https://lh3.googleusercontent.com/p/AF1QipMvoxQvwUAp0Puuj342UHpkblsBwC20CVP0yNM4=s1600-h400', 'https://lh3.googleusercontent.com/p/AF1QipP8Vf_r5ASXomQES5ld8wCfViID9BvsZJ1SkID5=s1600-h400', 'https://lh3.googleusercontent.com/p/AF1QipMqfaALLYaaemvGMWQQ3pbVC39DREL5QXap9WVY=s1600-h400', 'https://lh3.googleusercontent.com/p/AF1QipNrS6Qz_snOZetCGgsIH6N9uk29F9b6qe-4o9BE=s1600-h400']

# dest_info = {'name': 'Centennial Park at Houk Stream',
#     'photo_ids': ['ATtYBwL5tMBX0SZ-sAfcvlPXo5Y0WsutQozNDVjBxyX9agspWmBfN2EwLnscL4bxFLmSz-cQx31fU_FsKyoe9LtOYk3uOr9hleBFed-QfRr35wWHOEhHrjb1GOLHDnsSkQLdebBdxrFXfRv5jiZmkqaG3lVoYq0DHEP6mbA_r_YgP462ZWyO',
#     'ATtYBwKMf25dMPnFK1Os65Yqb2E8etaT-7O69ceiXx4bYeIyzDErnxmB71fDQ961isWOr5ZpsH9DBjHEPatAwI6THbCRcJG9uNdHaCvNMLxb73OTOxZ-9lKsGcu2dx2FGIlkbCWxJq098ksN3fCrj1au2445rLPYaZyR5etF_Np3T0maMi0F',
#     'ATtYBwJVkC1VC6izNsizpt0_fui06NNLteQkYQk-SeZfXHTSH62RYEMTkAnK6p7RvFOtUPSbN1Sja29xdFp3mIvH908gCS9DFqfCL6Sd6vVpGLrxk4dbMdb_1JJFA1ihL16eYuoJLjkymBKUVgs16C-Lhjv0_zghWPOkyESVZMbIb2eNqtEt',
#     'ATtYBwLCSK9_Rp_2dtyUX0owiW_jnEFvUAbchLO0HfD2PODUcgEbSnwyTvs-uC1T-VGvRCujZviwD_sxFnKil2u-xVEaeVC4KW_jTy4LTU5LCjk-gLz_f7-reMz2Gtr4FJkDUxJfP3BbYNmSfxtrgn-EWSC9RbU6olywrU47GJM0n6Rm7z3b',
#     'ATtYBwI9d6HaU9rg90psOLkvcnYfR9EzkULjFIG7bbaOeoVpOWISEcoS94frtzITzDH7RdK0yS8KeobDJhkJOnJ2bwKafg9uwYnR8C2LrdPnYztcVZGd2lf2TgQGCgom4MmRMbXHB06U6Ig-GHipf-OEU06xJonQ-XDCnhWZtmIGSFKAbNXb',
#     'ATtYBwKGOwuU01MnqMpZ_47DLUuNn6R0iezP3BzDZGyfr8WVTaDoCV2XMEPNzkw3ZwMmzdIoE9q_lUDJJ17y42HIHrCdHhZZaVWL_9TSNZqJBFJaCc-byzuN-Tk211ALsBMy2EdwnGHW7ZHTxbCuxqZLvdT_9HHo6h_yPzS47NkJMuBR15-k',
#     'ATtYBwI5zO0b3-TDX-eMvMDtZxekCINuzLR1utUePGxJ3Pf2ObD8XcwO6AmPavUxLzdNNGDjWdbtkK0v4p5tRiSjbhIveZGQcdHZEBRarkXUaMDWYo4XhRZ4bVZIzRvP43RfrxHsFJbqdMjeFNcbg1mF29xJspbQPgO2sq0gYISj59HGt2f1',
#     'ATtYBwJJabDFTB7mOGOrr6GUtKF4QDe6sovDqkH3T9lcZE3KE2Ynh4x5wG3ICuT0Xtp7lSFelhsDJdwSJy7HuFunNI5hHXcFfW32BEGNVjQTvAK7XXz6Tb1zjs_J9QCVlpP-oPzLE15JvlfLr0ApReEfEtkQ6Vre3qWEcQfqWcN8fsiwhqC5',
#     'ATtYBwKUR-OHOvf1LazYnKbamLI-Uy6Gq_BCuwq4OqBSZr9QE_FYTEiV4iarFUma_bKypXFInmPa6p2_mjJujDEN2RHAn1CA8QywuLuWb0t_GKOTy2uFdTw_6B52dJT5qcTXdjEudAewJpHLFowtBuevTCo_cF59PVP6aPaFJrlXtHRsxpdR',
#     'ATtYBwKYzsJnI3UjiGTy1DRFbMkGql-QHsve4RlyIN-7XkeWHdojw6i8hNCdr53nwS3uFXHSHf5uZ6lg8m9EjmgUDwiVhyMB8ZCT4_yKO0epXZi9F52qeU0zTZrflHzIi2rr_IpioFevo4rW8xx1nlh2S23WqsrWPEqtGkXDPbB_kk4XhPa8'],
#     'website': 'https://oakwoodohio.gov/parks-natural-areas/',
#     'hours': ['Monday: 9:00 AM – 5:00 PM',
#     'Tuesday: 9:00 AM – 5:00 PM',
#     'Wednesday: 9:00 AM – 5:00 PM',
#     'Thursday: 9:00 AM – 5:00 PM',
#     'Friday: 9:00 AM – 5:00 PM',
#     'Saturday: 9:00 AM – 5:00 PM',
#     'Sunday: 12:00 – 5:00 PM']}