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
# dist_time = gmaps.distance_matrix(origins=('2215 Willowgrove Ave, Dayton, OH 45409'),
#                                 destinations=['1300 E 1st St, Dayton, OH 45403','wright State University, Fairborn, OH'], 
#                                 mode='driving',
#                                 departure_time=now,
#                                 traffic_model='best_guess')

# len = len(dist_time['rows'][0]['elements']) - 1
# import pdb
# pdb.set_trace()

# dist_time:
# {'destination_addresses': ['1300 E 1st St, Dayton, OH 45403, USA'],
#  'origin_addresses': ['2218 Willowgrove Ave, Dayton, OH 45409, USA'],
#  'rows': [{'elements': [{'distance': {'text': '7.0 km', 'value': 7038},
#      'duration': {'text': '10 mins', 'value': 615},
#      'duration_in_traffic': {'text': '10 mins', 'value': 581},
#      'status': 'OK'}]}],
#  'status': 'OK'}

# duration_in_traffic = dist_time['rows'][0]['elements'][0]['duration_in_traffic']['text']

# {'destination_addresses': ['1300 E 1st St, Dayton, OH 45403, USA', '3640 Colonel Glenn Hwy, Dayton, OH 4
# 5435, USA'], 'origin_addresses': ['2215 Willowgrove Ave, Dayton, OH 45409, USA'], 'rows': [{'elements':
# [{'distance': {'text': '6.2 km', 'value': 6174}, 'duration': {'text': '11 mins', 'value': 653}, 'duratio
# n_in_traffic': {'text': '10 mins', 'value': 591}, 'status': 'OK'}, {'distance': {'text': '21.2 km', 'val
# ue': 21224}, 'duration': {'text': '17 mins', 'value': 1040}, 'duration_in_traffic': {'text': '17 mins',
# 'value': 1034}, 'status': 'OK'}]}], 'status': 'OK'}

                
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
########################################################################

# https://cloud.google.com/maps-platform/user-guide/product-changes/#places
# The Basic category does not result in any additional charge and includes the following fields:
#     address_component, adr_address, formatted_address, geometry, icon, name, permanently_closed, photo, place_id, plus_code, type, url, utc_offset, vicinity

# The Contact category results in an additional charge and includes the following fields:
#     formatted_phone_number, international_phone_number, opening_hours, website

# The Atmosphere category results in an additional charge and includes the following fields:
#     price_level, rating, review

########################################################################
########################################################################
# PLACES    -   .place(*args, **kwargs)     - Comprehensive details for an individual place.

# fields = ['name', 'photo', 'place_id', 'url']
# place = gmaps.place(place_id='ChIJRdZFgIWGQIgRKRraAEvA2I0', fields=fields)

place = {'html_attributions': [],
 'result': {'name': 'Southern Hills Park',
  'photos': [{'height': 3024,
              'html_attributions': ['<a href="https://maps.google.com/maps/contrib/105324917305996772201">James Jett</a>'],
              'photo_reference': 'ATtYBwJIabPFv2m4AkozY-9k_axPnq1yEkJvjVA_YniZb2jzijLj58s32VdAaB1ADEvawigIS_7rM2VndMmXHNdF_g5h7XU6jKM46HpJbFpS1j77KOYtmeD2Jo9Gyfz2NDBcOF5AHiAZKugyRIrwfsmpAEovqlLo6diaP2Bwv9HyoHteFGJw',
                'width': 4032},
            {'height': 3024,
                'html_attributions': ['<a href="https://maps.google.com/maps/contrib/105324917305996772201">James Jett</a>'],
                'photo_reference': 'ATtYBwKNK8p8Of59kc-vj7YDer6Ex1uIND12yzlLMvs7pNN_t7BxdIlKMJzw6mPnUBldVzdv3WwVj-lv1CukgxP6kxMIAIQyHhJcOXuJu611quFKIo9634Cq6z-TfLqSdfjdDLKwwjPPADxbSUr_oy0aqyqN_vHNjWHCWBbHfuQitLb-lOzf',
                'width': 4032},
            {'height': 4160,
                'html_attributions': ['<a href="https://maps.google.com/maps/contrib/106205926960862233093">Tanya Morgan</a>'],
                'photo_reference': 'ATtYBwIY35KsKeR2GT6hbq6jXI8ywNV1hYNJtASVs_UkBEtGq-KTjafBmDSM73k2mcfbmwNc2-PQFwmWxTRX4Ch9CllBQuGW9SblJGGALuBU8iGhgnH1ImJSHZxAWmEMPScWAgH19DKSeprVsQjt4t76pZljJYQBwgM37l2RgjpK8hVVj_hz',
                'width': 3120},
            {'height': 4160,
                'html_attributions': ['<a href="https://maps.google.com/maps/contrib/106205926960862233093">Tanya Morgan</a>'],
                'photo_reference': 'ATtYBwKkkdO0pzfvmZEIflc01d2PdHz2TYPBUYlDb7_cAkE3dycbxzBjEpF8JgNUNnS0dW_tA78ZcsDb1zka_mq8oi-wITMJg6k-qgK5zYCIm4MtgbVWl4WcSlbLfK3EqSWDsr6p2b71AX47PVyFCH9VAdrIatapW_3n8-jos1JiTvDsUpY_',
                'width': 3120},
            {'height': 4160,
                'html_attributions': ['<a href="https://maps.google.com/maps/contrib/111299640546577933152">Michael Willis</a>'],
                'photo_reference': 'ATtYBwKnECZNYaTdgZ1_39mnckKQsN6LUvRmAa8ChR02S42TxnzdVP_CfJTaPFYnXuhp4XaSO417orcZx5OC3J1jS1u9MGRjV7F_agdXe5TKFpQGxqtJ5YX1kERfr5wOXUJ46i2IQSW7_N-26nJYfXXBNn3cyejF-8jYNOko5qd7CJ7fp7IE',
                'width': 2340},
            {'height': 3024,
                'html_attributions': ['<a href="https://maps.google.com/maps/contrib/105324917305996772201">James Jett</a>'],
                'photo_reference': 'ATtYBwJ0K5XFAGLDONR5fuNCyx0fbk-SZg3FX4pWBC61VtwzZmAzDPb1EdJPpb4LPl4rX5ub-lmwO_sRYu6Ryv1mB82cgHNjvIK_u-rtZ91tcrikNDsClxoL6Jf5yKthGdv5ifHvIqQ4eZFkgEBt-ke3ucej1Acm8DccfdzKFocRexaKYKjL',
                'width': 4032},
            {'height': 4000,
                'html_attributions': ['<a href="https://maps.google.com/maps/contrib/106741156774489974114">Ryan W</a>'],
                'photo_reference': 'ATtYBwKF_zpSs0iPCDuLBRoD4hO_j_ztMtygAPEym0GAHOprgeA3pBXH3uEr-nYC9R8pe59aP8Fdj3_J3TWc6yF57hoP2umTNe4vPG5UtKpYb1KJN3PcZ3pgsoK98RtCx6_Yid6PVcp5vr4jz_SjCVpQiZSHeM0a5AftEgNXaJCfCZGCHoC8',
                'width': 3000},
            {'height': 3024,
                'html_attributions': ['<a href="https://maps.google.com/maps/contrib/105324917305996772201">James Jett</a>'],
                'photo_reference': 'ATtYBwLtlaAvfs4z6pFAs1xx3LjvTSLZlvA7Bd0vYaypFA_FuJ0St_9s4IRY7yPZT8Pqjmc-FNevVjCJnWKYr9zk7WsVe8-nhY9gTFIzDntlW6BRq7ZWCh1saq4J-daR1toVMBSI6ibmiHRNZSDqto9MK8OTXhhVVmrWCUnH7XhwERkg0VSj',
                'width': 4032},
            {'height': 4608,
                'html_attributions': ['<a href="https://maps.google.com/maps/contrib/112097783725407416477">danielle hobbs</a>'],
                'photo_reference': 'ATtYBwIPD9uvL9urlOiP1THUYsb503eo4OOhKA9g0OEKkunuz55yf1tBG11JpaTE9RSaUPG8-EVyZ2q9yFNmiyuF6SrA7foO33cBDATPeJJihz1y5zPj3ORLqTkchXrZ7NxF1vvA1fvfPCd9RyAgF2auCq2h2vd-cfblQ-tljbf7IkX_cWV6',
                'width': 3456},
            {'height': 4160,
                'html_attributions': ['<a href="https://maps.google.com/maps/contrib/106205926960862233093">Tanya Morgan</a>'],
                'photo_reference': 'ATtYBwKNXAQkOmzMsBMDXIdqRzFJwhXEG6Z5BHJYi4DuBX62fQMv1th4zvxLLKdYgfNvSVBsdlou17RgM4THLqHsTR63wdjjLzVbUqLF5rCniJoqKrD2_nCmob3V7gUCGwxuKWGE7xs_cotue5Xie8wEBH7KFxG5A3pDfStOfL9twBCyF4eD',
                'width': 3120}],
  'place_id': 'ChIJRdZFgIWGQIgRKRraAEvA2I0',
  'url': 'https://maps.google.com/?cid=10221130782686714409'},
 'status': 'OK'}

x = [photo['photo_reference'] for photo in place['result']['photos']]

########################################################################
# PLACES    -   .find_place(*args, **kwargs)

# fields = ['formatted_address', 'geometry/location', 'name', 'photos', 'place_id']
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

# {'candidates': [{'formatted_address': 'Kettering, OH 45409, United States',
#                 'geometry': {'location': {'lat': 39.7207217, 'lng': -84.1961413}},
#                 'name': 'Southern Hills Park',
#                 'photos': [{'height': 3024,
#                             'html_attributions': ['<a href="https://maps.google.com/maps/contrib/105324917305996772201">James Jett</a>'],
#                             'photo_reference': 'ATtYBwLdBHJvCZnLHtnnuwSpKcO26qlclaBkiUhFlbY4d8NLGtBfr7yKuDgF5r8tlieu2yOeAj-taCfZ-o7GR5n5BoqqGrsuwpRolUo8toy6b05-g9TDytfUTs4BlHjVx6N2vKgxQtstq13mnXwwRZMgGNr7-_O5Uon9bFMDxUdy4i7Kywdt',
#                             'width': 4032}],
#                 'place_id': 'ChIJRdZFgIWGQIgRKRraAEvA2I0'}],
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

# photo_reference = ['ATtYBwKNXAQkOmzMsBMDXIdqRzFJwhXEG6Z5BHJYi4DuBX62fQMv1th4zvxLLKdYgfNvSVBsdlou17RgM4THLqHsTR63wdjjLzVbUqLF5rCniJoqKrD2_nCmob3V7gUCGwxuKWGE7xs_cotue5Xie8wEBH7KFxG5A3pDfStOfL9twBCyF4eD', 'ATtYBwKkkdO0pzfvmZEIflc01d2PdHz2TYPBUYlDb7_cAkE3dycbxzBjEpF8JgNUNnS0dW_tA78ZcsDb1zka_mq8oi-wITMJg6k-qgK5zYCIm4MtgbVWl4WcSlbLfK3EqSWDsr6p2b71AX47PVyFCH9VAdrIatapW_3n8-jos1JiTvDsUpY_']
# photo = requests.get('https://maps.googleapis.com/maps/api/place/photo',
#                     params={
#                         "key": API_KEY,
#                         "photoreference": photo_reference,
#                         "maxheight": 400
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
# .geocode()            (Python wrapper)

# address = gmaps.geocode('Centennial Park at Houk Stream, Oakwood, OH')

# address:
# v = [{'address_components': [{'long_name': '2215',
#                         'short_name': '2215',
#                          'types': ['street_number']},
#                         {'long_name': 'Willowgrove Avenue',
#                         'short_name': 'Willowgrove Ave',
#                         'types': ['route']},
#                         {'long_name': 'Dayton',
#                             'short_name': 'Dayton',
#                             'types': ['locality', 'political']},
#                         {'long_name': 'Montgomery County',
#                             'short_name': 'Montgomery County',
#                             'types': ['administrative_area_level_2', 'political']},
#                         {'long_name': 'Ohio',
#                             'short_name': 'OH',
#                             'types': ['administrative_area_level_1', 'political']},
#                         {'long_name': 'United States',
#                             'short_name': 'US',
#                             'types': ['country', 'political']},
#                         {'long_name': '45409', 'short_name': '45409', 'types': ['postal_code']},
#                         {'long_name': '1952',
#                             'short_name': '1952',
#                             'types': ['postal_code_suffix']}],
#   'formatted_address': '2215 Willowgrove Ave, Dayton, OH 45409, USA',
#   'geometry': {'bounds': {'northeast': {'lat': 39.7242003, 'lng': -84.1942423},
#                         'southwest': {'lat': 39.7240683, 'lng': -84.19441719999999}},
#                 'location': {'lat': 39.72412449999999, 'lng': -84.1943411},
#                 'location_type': 'ROOFTOP',
#                 'viewport': {'northeast': {'lat': 39.7254832802915,
#                                             'lng': -84.19298076970848},
#                             'southwest': {'lat': 39.7227853197085, 'lng': -84.1956787302915}}},
#   'place_id': 'ChIJryzQxJqGQIgRuT0Qo2yujtI',
#   'types': ['premise']}]

# vv = v[0]['geometry']['location']

###############################
# .reverse_geocode()    (Python wrapper)


# x = [{'address_components': [{'long_name': '1352', 'short_name': '1352', 'types': ['street_number']}, 
#                             {'long_name': 'Sanzon Drive', 'short_name': 'Sanzon Dr', 'types': ['route']}, 
#                             {'long_name':'Fairborn', 'short_name': 'Fairborn', 'types': ['locality', 'political']}, 
#                             {'long_name': 'Bath Township', 'short_name': 'Bath Township', 'types': ['administrative_area_level_3', 'political'] }, 
#                             {'long_name': 'Greene County', 'short_name': 'Greene County', 'types': ['administrative_area_level_2', 'political']}, 
#                             {'long_name': 'Ohio', 'short_name': 'OH', 'types': ['administrative_area_level_1', 'political']}, 
#                             {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}, 
#                             {'long_name': '45324', 'short_name': '45324', 'types': ['postal_code']}, 
#                             {'long_name': '2072', 'short_name': '2072', 'types': ['postal_code_suffix']}], 
#     'formatted_address': '1352 Sanzon Dr, Fairborn, OH 45324, USA', 
#     'geometry': {'location': {'lat': 39.778571, 'lng': -84.070058}, 
#                 'location_type': 'ROOFTOP', 
#                 'viewport': {'northeast': {'lat': 39.7799199802915, 'lng': -84.06870901970849}, 
#                 '             southwest': {'lat': 39.7772220197085, 'lng': -84.0714069802915}}}, 
#     'place_id': 'ChIJpyKN-O-cQIgRyVKYBKlYqPc', 
#     'plus_code': {'compound_code': 'QWHH+CX Fairborn, OH, USA', 'global_code': '86FQQWHH+CX'}, 
#     'types': ['street_address']}]


# y = x[0]['formatted_address']

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





photo_urls = ['https://lh3.googleusercontent.com/p/AF1QipNhYrPCBGVFhaLRNEHM4s6YItShEPbImEHKZllA=s1600-h400']

max_imgs = 5 if len(photo_urls) >= 5 else len(photo_urls) - 1