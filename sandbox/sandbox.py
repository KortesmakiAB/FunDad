import googlemaps
from secret_keys import API_KEY
from datetime import datetime
import requests

gmaps = googlemaps.Client(key=API_KEY)

########################################################################
# DRIVE TIME 
        
###############################
# .distance_matrix()        (Python wrapper)

# now = datetime.now()
# dist_time = gmaps.distance_matrix((39.724221,-84.193896),
#                                 '1300 E 1st St, Dayton, OH 45403', 
#                                 mode='driving',
#                                 departure_time=now,
#                                 traffic_model='best_guess')

# dist_time:
# {'destination_addresses': ['1300 E 1st St, Dayton, OH 45403, USA'],
#  'origin_addresses': ['2218 Willowgrove Ave, Dayton, OH 45409, USA'],
#  'rows': [{'elements': [{'distance': {'text': '7.0 km', 'value': 7038},
#      'duration': {'text': '10 mins', 'value': 615},
#      'duration_in_traffic': {'text': '10 mins', 'value': 581},
#      'status': 'OK'}]}],
#  'status': 'OK'}

# duration_in_traffic = dist_time['rows'][0]['elements'][0]['duration_in_traffic']['text']
                
###############################
# OR  directly through googleapis

# dist_time = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json',
#                         params={
#                             "key": API_KEY,
#                             "origins": "2215 Willowgrove Ave, Dayton, OH 45409",
#                             "destinations": "1300 E 1st St, Dayton, OH 45403"
#                         })

# dt = dist_time.json()
# duration = dt['rows'][0]['elements'][0]['duration']['text']
# {'destination_addresses': ['1300 E 1st St, Dayton, OH 45403, USA'],
#  'origin_addresses': ['2215 Willowgrove Ave, Dayton, OH 45409, USA'],
#  'rows': [{'elements': [{'distance': {'text': '7.0 km', 'value': 7018},
#      'duration': {'text': '10 mins', 'value': 612},
#      'status': 'OK'}]}],
#  'status': 'OK'}


########################################################################
# PLACES    -   .find_place(*args, **kwargs)

# fields = ['formatted_address', 'geometry/location', 'icon', 'name', 'photos', 'place_id', 'plus_code', 'types']
# place = gmaps.find_place(['Southern Hills Playground, Kettering, OH'],
#                         input_type='textquery',
#                         fields=fields)

# place:
# {'candidates': [{'formatted_address': 'Kettering, OH 45409, United States',
#    'geometry': {'location': {'lat': 39.7207217, 'lng': -84.1961413}},
#    'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/park-71.png',
#    'name': 'Southern Hills Park',
#    'obfuscated_type': [],
#    'photos': [{'height': 3024,
#      'html_attributions': ['<a href="https://maps.google.com/maps/contrib/105324917305996772201">James Jett</a>'],
#      'photo_reference': 'ATtYBwJemwKt6xiX3RyW-xAtejNKjygG8jrE7Z_uhWGvwgXGm5Z6xI_kNB9_HNmqq_FQWEW1rLTmaCCQJKwREsMsSvF0LIEPXXrG1lN29s-aWnsQqTZ6pRWY07jbeUr6M_K44yjn_RObleRZjxxgXkpP96Ed_4p4BjwA2ESxtnnMareRrYF9',
#      'width': 4032}],
#    'place_id': 'ChIJRdZFgIWGQIgRKRraAEvA2I0',
#    'plus_code': {'compound_code': 'PRC3+7G Kettering, Ohio',
#     'global_code': '86FQPRC3+7G'},
#    'types': ['park',
#     'tourist_attraction',
#     'point_of_interest',
#     'establishment']}],
#  'status': 'OK'}

# photo_reference = place['candidates'][0]['photos'][0]['photo_reference']


########################################################################
# PLACES PHOTO  

###############################
# GoogleAPIs    
    #  This worked MUCH better than the python wrapper '.places_photo()
# NB: 
    # Must get 'photo_reference' from Places API
    # Photos returned by the Photo service are sourced from a variety of locations, including business owners and user contributed photos. In most cases, these photos can be used without attribution, or will have the required attribution included as a part of the image. However, if the returned photo element includes a value in the html_attributions field, you will have to include the additional attribution in your application wherever you display the image.
    # a max_width or max_height arg is required (in pixels)

# photo_reference = 'ATtYBwJemwKt6xiX3RyW-xAtejNKjygG8jrE7Z_uhWGvwgXGm5Z6xI_kNB9_HNmqq_FQWEW1rLTmaCCQJKwREsMsSvF0LIEPXXrG1lN29s-aWnsQqTZ6pRWY07jbeUr6M_K44yjn_RObleRZjxxgXkpP96Ed_4p4BjwA2ESxtnnMareRrYF9'
# photo = requests.get('https://maps.googleapis.com/maps/api/place/photo',
#                     params={
#                         "key": API_KEY,
#                         "photoreference": photo_reference,
#                         "maxwidth": 350
#                     })

# print(dir(photo))
# eg.
# photo.url
# photo.raw
# photo.next - ???
# photo.request - I thikn this makes a GET request for the photo?

###############################
# .places_photo(*args, **kwargs)        (Python wrapper)
    # I don't like this. I get data that I don't know how to use.


# photos = gmaps.places_photo(photo_reference=photo_reference,
#                             max_width=350)

# photos = iterator containing the raw image data, which typically can be used to save an image file locally.
# 2/4/21  NOW THAT I have 'photos' I don't know what to do 
# for photo in photos:
#     im = open(photo, '')
#     im.show()
#     im.close()



########################################################################
# GEOCODE   -   Address into coordinates

###############################
# .geocode()  AND     .reverse_geocode()    -     (Python wrapper)


address = gmaps.geocode('Centennial Park at Houk Stream, Oakwood, OH')

# address:
# [{'address_components': [{'long_name': '2215',
#     'short_name': '2215',
#     'types': ['street_number']},
#    {'long_name': 'Willowgrove Avenue',
#     'short_name': 'Willowgrove Ave',
#     'types': ['route']},
#    {'long_name': 'Dayton',
#     'short_name': 'Dayton',
#     'types': ['locality', 'political']},
#    {'long_name': 'Montgomery County',
#     'short_name': 'Montgomery County',
#     'types': ['administrative_area_level_2', 'political']},
#    {'long_name': 'Ohio',
#     'short_name': 'OH',
#     'types': ['administrative_area_level_1', 'political']},
#    {'long_name': 'United States',
#     'short_name': 'US',
#     'types': ['country', 'political']},
#    {'long_name': '45409', 'short_name': '45409', 'types': ['postal_code']},
#    {'long_name': '1952',
#     'short_name': '1952',
#     'types': ['postal_code_suffix']}],
#   'formatted_address': '2215 Willowgrove Ave, Dayton, OH 45409, USA',
#   'geometry': {'bounds': {'northeast': {'lat': 39.7242003, 'lng': -84.1942423},
#     'southwest': {'lat': 39.7240683, 'lng': -84.19441719999999}},
#    'location': {'lat': 39.72412449999999, 'lng': -84.1943411},
#    'location_type': 'ROOFTOP',
#    'viewport': {'northeast': {'lat': 39.7254832802915,
#      'lng': -84.19298076970848},
#     'southwest': {'lat': 39.7227853197085, 'lng': -84.1956787302915}}},
#   'place_id': 'ChIJryzQxJqGQIgRuT0Qo2yujtI',
#   'types': ['premise']}]

###############################
# Google API      

# coords = requests.get('https://maps.googleapis.com/maps/api/geocode/json',
#                         params={
#                             "key": API_KEY,
#                             "address": "2215 Willowgrove Ave, Dayton, OH 45409"
#                         })

# x = coords.json()

# x:
# {'results': [{'address_components': [{'long_name': '2215',
#      'short_name': '2215',
#      'types': ['street_number']},
#     {'long_name': 'Willowgrove Avenue',
#      'short_name': 'Willowgrove Ave',
#      'types': ['route']},
#     {'long_name': 'Dayton',
#      'short_name': 'Dayton',
#      'types': ['locality', 'political']},
#     {'long_name': 'Montgomery County',
#      'short_name': 'Montgomery County',
#      'types': ['administrative_area_level_2', 'political']},
#     {'long_name': 'Ohio',
#      'short_name': 'OH',
#      'types': ['administrative_area_level_1', 'political']},
#     {'long_name': 'United States',
#      'short_name': 'US',
#      'types': ['country', 'political']},
#     {'long_name': '45409', 'short_name': '45409', 'types': ['postal_code']},
#     {'long_name': '1952',
#      'short_name': '1952',
#      'types': ['postal_code_suffix']}],
#    'formatted_address': '2215 Willowgrove Ave, Dayton, OH 45409, USA',
#    'geometry': {'bounds': {'northeast': {'lat': 39.7242003,
#       'lng': -84.1942423},
#      'southwest': {'lat': 39.7240683, 'lng': -84.19441719999999}},
#     'location': {'lat': 39.72412449999999, 'lng': -84.1943411},
#     'location_type': 'ROOFTOP',
#     'viewport': {'northeast': {'lat': 39.7254832802915,
#       'lng': -84.19298076970848},
#      'southwest': {'lat': 39.7227853197085, 'lng': -84.1956787302915}}},
#    'place_id': 'ChIJryzQxJqGQIgRuT0Qo2yujtI',
#    'types': ['premise']}],
#  'status': 'OK'}
