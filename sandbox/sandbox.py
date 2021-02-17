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
#                                 destinations=['1300 E 1st St, Dayton, OH 44224','wright State University, Fairborn, OH'], 
#                                 mode='driving',
#                                 departure_time=now,
#                                 traffic_model='best_guess')

# len = len(dist_time['rows'][0]['elements']) - 1

# Errors: NameError
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

# fields = ['name', 'photo', 'place_id', 'opening_hours', 'website']
# # place = gmaps.place(place_id='ChIJvd5c0HOBQIgRGNiQ5jUwbrI', fields=fields)

# b = {'html_attributions': [],
#  'result': {'name': 'Boonshoft Museum of Discovery',
#             'opening_hours': {'open_now': False,
#                             'periods': [{'close': {'day': 0, 'time': '1700'},
#                                         'open': {'day': 0, 'time': '1200'}},
#                                         {'close': {'day': 1, 'time': '1700'}, 'open': {'day': 1, 'time': '0900'}},
#                                         {'close': {'day': 2, 'time': '1700'}, 'open': {'day': 2, 'time': '0900'}},
#                                         {'close': {'day': 3, 'time': '1700'}, 'open': {'day': 3, 'time': '0900'}},
#                                         {'close': {'day': 4, 'time': '1700'}, 'open': {'day': 4, 'time': '0900'}},
#                                         {'close': {'day': 5, 'time': '1700'}, 'open': {'day': 5, 'time': '0900'}},
#                                         {'close': {'day': 6, 'time': '1700'}, 'open': {'day': 6, 'time': '0900'}}],
#                             'weekday_text': ['Monday: 9:00 AM – 5:00 PM',
#                                 'Tuesday: 9:00 AM – 5:00 PM',
#                                 'Wednesday: 9:00 AM – 5:00 PM',
#                                 'Thursday: 9:00 AM – 5:00 PM',
#                                 'Friday: 9:00 AM – 5:00 PM',
#                                 'Saturday: 9:00 AM – 5:00 PM',
#                                 'Sunday: 12:00 – 5:00 PM']},
#             'photos': [{'height': 1365,
#                         'html_attributions': ['<a href="https://maps.google.com/maps/contrib/109694830663985866651">Boonshoft Museum of Discovery</a>'],
#                         'photo_reference': 'ATtYBwL-uJfey1-24qsFz0b7sArtJa77rIvHKIp_g7GF_MxKg1aCXqlj6mVQhnBfM26AmYPX4cNqcxpahtHNy7TWvK5eUe7wiP8l4ATwVbdR_OfQjfVZN_cO6v1RyFCDRvq5_J30o5rylnETuuWFxUFJFeKs2pi-ulDkG6rkFHErs15GKAZb',
#                         'width': 2048},
#                     {'height': 2620,
#                         'html_attributions': ['<a href="https://maps.google.com/maps/contrib/113728012717898709750">Dustin Manor</a>'],
#                         'photo_reference': 'ATtYBwKdgv2HanNWB2jUmmrYmRbVbz0IT__UQpcCiMwJpbyHJJ6IsytOPCasK85WRNtzQI0SjcjF8L63lbUGO4eomb0sS3gpyCzXuF7UrUWjyRKWwXaIqpzJ50rwSxw0n3ZqpTu-rAfwV9V7bjnRqmgXrphVG8V99rHIUZcjEbWKSOpOURAh',
#                         'width': 4656},
#                     {'height': 2160,
#                         'html_attributions': ['<a href="https://maps.google.com/maps/contrib/115461152148490437135">Heather Bucher</a>'],
#                         'photo_reference': 'ATtYBwLtxxuO2XgEr1ICZyixaUKqOAkOqSJApdWpmfxEGOW1_qUOn8L3u8Q1D0SfxiK11FxBG0WzMGS5qjSMrTDYSTqyTlXTQoAQqz3znVYX5lTKi6m79xPyYtm_Rns_YnUAKafVRPi_82Q9_U0qA74VR-jS2HZEwBN1kQcTCG33pIS3ODln',
#                         'width': 2880},
#                     {'height': 3036,
#                         'html_attributions': ['<a href="https://maps.google.com/maps/contrib/117890020656337989815">John-Paul Ownby</a>'],
#                         'photo_reference': 'ATtYBwLYs8FkpqFbC_ylpdbSYXMrwiJwdrHzi63J64uYUnsbScx-wecRT9j9AK5iU70pA6LD5F4xqaftfmZueSUU6-7MXVunucwYv2Ov8uiqYJS9GUuMtpFJp9G38PUclYbq0xGWGl6x6sRDDi4FPQelKsbCSRj9EPW7ZOM6oKsYu2NJ0kYr',
#                         'width': 4048},
#                     {'height': 3024,
#                         'html_attributions': ['<a href="https://maps.google.com/maps/contrib/106762511050368251555">Russell Knipp</a>'],
#                         'photo_reference': 'ATtYBwIXS-kStVQ5cSe8AL8kM7ozOGwsj6V_QL76HAAdALToWtFxyZX9rflhczi-5lel9kEDaYWo3759UpdboqVdIh4VSQ5rPStgp_BnSW3YNntfkqEVAZMjl243i88e3s9KJOFZUu2Y5YfR916BR6FvGOMBvvxgV2dJoAn7H-x1AVp642N8',
#                         'width': 4032},
#                     {'height': 4160,
#                         'html_attributions': ['<a href="https://maps.google.com/maps/contrib/114168203907535647944">Johnathan Griswold</a>'],
#                         'photo_reference': 'ATtYBwJEiHy6-UmRfqjkhR6-lNV1X8waeSxcOx1kFaxdb0VZtFFJ1nQLbva7jdI9bYO1YBA9wg23zaA26XTOrLzhrry50GQJfSdYe4s2PzkaC5pKXjCojzFi4qvhqZF3Wxfg2-zACtkd00IUP00V1j9IA9qsfs2sOCScnnkK4aDnUcHtBoZN',
#                         'width': 3120},
#                     {'height': 1440,
#                         'html_attributions': ['<a href="https://maps.google.com/maps/contrib/117745312980000935803">Michael Harris</a>'],
#                         'photo_reference': 'ATtYBwJOjCyexKX7kSshGlddUpCR22fm5LsO0JBLo19a5fHZSaaI_tdfjLppWZiNttaJpRCxXVZhhGnqJLtxkSCC2tle4dtoe9h_KCUl6pim2B1r7JJGqmNwbh3lTgIeACIQUXABwzEmBW26Xak9kEjbJqmZL-S9yj-Jsn5P6GWFgaPN6QsE',
#                         'width': 2560},
#                     {'height': 1866,
#                         'html_attributions': ['<a href="https://maps.google.com/maps/contrib/109694830663985866651">Boonshoft Museum of Discovery</a>'],
#                         'photo_reference': 'ATtYBwKoMW6Q2dN0AXR2CNq2srMfukRVSFTRaydcRU0mpuUshzOnFmYD6s4Iu-kWX5fnf6GUERO1d5BZLjKzrGsIhfS-nyQ8PoukNNi6Xdb2vhQ4xpwLIWw-_LpeJnSjqaE7xF9KkZj62970Yh5MwyBxNrphR4keA8CpbqhhoiTAwAYuCb5L',
#                         'width': 2912},
#                     {'height': 3024,
#                         'html_attributions': ['<a href="https://maps.google.com/maps/contrib/107073518753744848393">Katie Hallock</a>'],
#                         'photo_reference': 'ATtYBwI9f41qkavn1Scpk5G9xylki5mmt-uz6hkZPFH-kHzLBgvpCys_FM1IrjZS0z9E-C0y5r1lAWkPHAtTXt7Uo5FGBUGxuSNMWlTf-cVKyNvyJ3-7fC7armwkBl_mJwo3C4TezdXDrlA8w4PfNDopd8o5LhWDHd6zDTIkZ6r65o5fNFFc',
#                         'width': 4032},
#                     {'height': 3024,
#                         'html_attributions': ['<a href="https://maps.google.com/maps/contrib/104369181846204953688">R C</a>'],
#                         'photo_reference': 'ATtYBwLkQdag3E32IcXNEsBq3JBYY_j-DMm2XJ-c2QDD2eOfNsiyYPYH9SDTgAyi7Q3jTNnoGPfBNPZewR9g2LtI5xN05gAgUWWxkcLX8al8m3LA6xHeGzbCWvBYS73Gl89SARDgtkKMsWIoU9wJkEXwV7W1cSi4UDZINl0WIyCF6aeCvzFo',
#                         'width': 4032}],
#   'place_id': 'ChIJvd5c0HOBQIgRGNiQ5jUwbrI',
#   'website': 'http://www.boonshoftmuseum.org/'},
#  'status': 'OK'}
 
# place = {'html_attributions': [], 'result': {'name': 'Centennial Park at Houk Stream', 'photos': [{'height': 3000, 'html_attributions': ['<ahref="https://maps.google.com/maps/contrib/107105990195332493964">Jeff Anderson</a>'], 'photo_reference': 'ATtYBwL5tMBX0SZ-sAfcvlPXo5Y0WsutQozNDVjBxyX9agspWmBfN2EwLnscL4bxFLmSz-cQx31fU_FsKyoe9LtOYk3uOr9hleBFed-QfRr35wWHOEhHrjb1GOLHDnsSkQLdebBdxrFXfRv5jiZmkqaG3lVoYq0DHEP6mbA_r_YgP462ZWyO', 'width': 4000}, {'height': 3024, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/105751133502794738916">Brad Fairfax</a>'], 'photo_reference': 'ATtYBwKMf25dMPnFK1Os65Yqb2E8etaT-7O69ceiXx4bYeIyzDErnxmB71fDQ961isWOr5ZpsH9DBjHEPatAwI6THbCRcJG9uNdHaCvNMLxb73OTOxZ-9lKsGcu2dx2FGIlkbCWxJq098ksN3fCrj1au2445rLPYaZyR5etF_Np3T0maMi0F', 'width': 4032}, {'height':3024, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/112295572036242987396">Jamie Obermeyer</a>'], 'photo_reference': 'ATtYBwJVkC1VC6izNsizpt0_fui06NNLteQkYQk-SeZfXHTSH62RYEMTkAnK6p7RvFOtUPSbN1Sja29xdFp3mIvH908gCS9DFqfCL6Sd6vVpGLrxk4dbMdb_1JJFA1ihL16eYuoJLjkymBKUVgs16C-Lhjv0_zghWPOkyESVZMbIb2eNqtEt', 'width': 4032}, {'height': 4128, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/106120600894759740840">Donnie Holland</a>'], 'photo_reference': 'ATtYBwLCSK9_Rp_2dtyUX0owiW_jnEFvUAbchLO0HfD2PODUcgEbSnwyTvs-uC1T-VGvRCujZviwD_sxFnKil2u-xVEaeVC4KW_jTy4LTU5LCjk-gLz_f7-reMz2Gtr4FJkDUxJfP3BbYNmSfxtrgn-EWSC9RbU6olywrU47GJM0n6Rm7z3b', 'width': 2322}, {'height': 3024, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/109515622218133428811">George Saad</a>'], 'photo_reference': 'ATtYBwI9d6HaU9rg90psOLkvcnYfR9EzkULjFIG7bbaOeoVpOWISEcoS94frtzITzDH7RdK0yS8KeobDJhkJOnJ2bwKafg9uwYnR8C2LrdPnYztcVZGd2lf2TgQGCgom4MmRMbXHB06U6Ig-GHipf-OEU06xJonQ-XDCnhWZtmIGSFKAbNXb', 'width': 4032}, {'height': 4032, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/107914718764762506572">The Cute Baby</a>'], 'photo_reference': 'ATtYBwKGOwuU01MnqMpZ_47DLUuNn6R0iezP3BzDZGyfr8WVTaDoCV2XMEPNzkw3ZwMmzdIoE9q_lUDJJ17y42HIHrCdHhZZaVWL_9TSNZqJBFJaCc-byzuN-Tk211ALsBMy2EdwnGHW7ZHTxbCuxqZLvdT_9HHo6h_yPzS47NkJMuBR15-k', 'width': 1960}, {'height': 3024, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/105132829706374400796">Bruno Matisin</a>'], 'photo_reference': 'ATtYBwI5zO0b3-TDX-eMvMDtZxekCINuzLR1utUePGxJ3Pf2ObD8XcwO6AmPavUxLzdNNGDjWdbtkK0v4p5tRiSjbhIveZGQcdHZEBRarkXUaMDWYo4XhRZ4bVZIzRvP43RfrxHsFJbqdMjeFNcbg1mF29xJspbQPgO2sq0gYISj59HGt2f1', 'width': 4032}, {'height': 3024, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/112295572036242987396">Jamie Obermeyer</a>'], 'photo_reference': 'ATtYBwJJabDFTB7mOGOrr6GUtKF4QDe6sovDqkH3T9lcZE3KE2Ynh4x5wG3ICuT0Xtp7lSFelhsDJdwSJy7HuFunNI5hHXcFfW32BEGNVjQTvAK7XXz6Tb1zjs_J9QCVlpP-oPzLE15JvlfLr0ApReEfEtkQ6Vre3qWEcQfqWcN8fsiwhqC5', 'width': 4032}, {'height': 4032, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/101177918721489015430">Mike Smith</a>'], 'photo_reference': 'ATtYBwKUR-OHOvf1LazYnKbamLI-Uy6Gq_BCuwq4OqBSZr9QE_FYTEiV4iarFUma_bKypXFInmPa6p2_mjJujDEN2RHAn1CA8QywuLuWb0t_GKOTy2uFdTw_6B52dJT5qcTXdjEudAewJpHLFowtBuevTCo_cF59PVP6aPaFJrlXtHRsxpdR', 'width': 3024}, {'height': 3024, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/105751133502794738916">Brad Fairfax</a>'], 'photo_reference': 'ATtYBwKYzsJnI3UjiGTy1DRFbMkGql-QHsve4RlyIN-7XkeWHdojw6i8hNCdr53nwS3uFXHSHf5uZ6lg8m9EjmgUDwiVhyMB8ZCT4_yKO0epXZi9F52qeU0zTZrflHzIi2rr_IpioFevo4rW8xx1nlh2S23WqsrWPEqtGkXDPbB_kk4XhPa8', 'width': 4032}], 'place_id':'ChIJJzjSCCyEQIgRQIeUXsPJqCQ', 'website': 'https://oakwoodohio.gov/parks-natural-areas/'}, 'status': 'OK'}

# try:
#     name = place['result']['name']
# except KeyError:
#     name = 'n/a'
# try:
#     photo_ids = [photo['photo_reference'] for photo in place['result']['photos']]
# except KeyError:
#     photo_ids = 'n/a'
# try:
#     website = place['result']['website']
# except KeyError:
#     website = 'n/a'
# try:
#     hours = b['result']['opening_hours']['weekday_text']
# except KeyError:
#     hours = 'n/a'

# a = {
#         'name': name,
#         'photo_ids': photo_ids,
#         'website': website,
#         'hours': hours
# }

# a = {'html_attributions': [],
#  'result': {'name': 'Southern Hills Park',
#   'photos': [{'height': 3024,
#               'html_attributions': ['<a href="https://maps.google.com/maps/contrib/105324917305996772201">James Jett</a>'],
#               'photo_reference': 'ATtYBwJIabPFv2m4AkozY-9k_axPnq1yEkJvjVA_YniZb2jzijLj58s32VdAaB1ADEvawigIS_7rM2VndMmXHNdF_g5h7XU6jKM46HpJbFpS1j77KOYtmeD2Jo9Gyfz2NDBcOF5AHiAZKugyRIrwfsmpAEovqlLo6diaP2Bwv9HyoHteFGJw',
#                 'width': 4032},
#             {'height': 3024,
#                 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/105324917305996772201">James Jett</a>'],
#                 'photo_reference': 'ATtYBwKNK8p8Of59kc-vj7YDer6Ex1uIND12yzlLMvs7pNN_t7BxdIlKMJzw6mPnUBldVzdv3WwVj-lv1CukgxP6kxMIAIQyHhJcOXuJu611quFKIo9634Cq6z-TfLqSdfjdDLKwwjPPADxbSUr_oy0aqyqN_vHNjWHCWBbHfuQitLb-lOzf',
#                 'width': 4032},
#             {'height': 4160,
#                 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/106205926960862233093">Tanya Morgan</a>'],
#                 'photo_reference': 'ATtYBwIY35KsKeR2GT6hbq6jXI8ywNV1hYNJtASVs_UkBEtGq-KTjafBmDSM73k2mcfbmwNc2-PQFwmWxTRX4Ch9CllBQuGW9SblJGGALuBU8iGhgnH1ImJSHZxAWmEMPScWAgH19DKSeprVsQjt4t76pZljJYQBwgM37l2RgjpK8hVVj_hz',
#                 'width': 3120},
#             {'height': 4160,
#                 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/106205926960862233093">Tanya Morgan</a>'],
#                 'photo_reference': 'ATtYBwKkkdO0pzfvmZEIflc01d2PdHz2TYPBUYlDb7_cAkE3dycbxzBjEpF8JgNUNnS0dW_tA78ZcsDb1zka_mq8oi-wITMJg6k-qgK5zYCIm4MtgbVWl4WcSlbLfK3EqSWDsr6p2b71AX47PVyFCH9VAdrIatapW_3n8-jos1JiTvDsUpY_',
#                 'width': 3120},
#             {'height': 4160,
#                 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/111299640546577933152">Michael Willis</a>'],
#                 'photo_reference': 'ATtYBwKnECZNYaTdgZ1_39mnckKQsN6LUvRmAa8ChR02S42TxnzdVP_CfJTaPFYnXuhp4XaSO417orcZx5OC3J1jS1u9MGRjV7F_agdXe5TKFpQGxqtJ5YX1kERfr5wOXUJ46i2IQSW7_N-26nJYfXXBNn3cyejF-8jYNOko5qd7CJ7fp7IE',
#                 'width': 2340},
#             {'height': 3024,
#                 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/105324917305996772201">James Jett</a>'],
#                 'photo_reference': 'ATtYBwJ0K5XFAGLDONR5fuNCyx0fbk-SZg3FX4pWBC61VtwzZmAzDPb1EdJPpb4LPl4rX5ub-lmwO_sRYu6Ryv1mB82cgHNjvIK_u-rtZ91tcrikNDsClxoL6Jf5yKthGdv5ifHvIqQ4eZFkgEBt-ke3ucej1Acm8DccfdzKFocRexaKYKjL',
#                 'width': 4032},
#             {'height': 4000,
#                 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/106741156774489974114">Ryan W</a>'],
#                 'photo_reference': 'ATtYBwKF_zpSs0iPCDuLBRoD4hO_j_ztMtygAPEym0GAHOprgeA3pBXH3uEr-nYC9R8pe59aP8Fdj3_J3TWc6yF57hoP2umTNe4vPG5UtKpYb1KJN3PcZ3pgsoK98RtCx6_Yid6PVcp5vr4jz_SjCVpQiZSHeM0a5AftEgNXaJCfCZGCHoC8',
#                 'width': 3000},
#             {'height': 3024,
#                 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/105324917305996772201">James Jett</a>'],
#                 'photo_reference': 'ATtYBwLtlaAvfs4z6pFAs1xx3LjvTSLZlvA7Bd0vYaypFA_FuJ0St_9s4IRY7yPZT8Pqjmc-FNevVjCJnWKYr9zk7WsVe8-nhY9gTFIzDntlW6BRq7ZWCh1saq4J-daR1toVMBSI6ibmiHRNZSDqto9MK8OTXhhVVmrWCUnH7XhwERkg0VSj',
#                 'width': 4032},
#             {'height': 4608,
#                 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/112097783725407416477">danielle hobbs</a>'],
#                 'photo_reference': 'ATtYBwIPD9uvL9urlOiP1THUYsb503eo4OOhKA9g0OEKkunuz55yf1tBG11JpaTE9RSaUPG8-EVyZ2q9yFNmiyuF6SrA7foO33cBDATPeJJihz1y5zPj3ORLqTkchXrZ7NxF1vvA1fvfPCd9RyAgF2auCq2h2vd-cfblQ-tljbf7IkX_cWV6',
#                 'width': 3456},
#             {'height': 4160,
#                 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/106205926960862233093">Tanya Morgan</a>'],
#                 'photo_reference': 'ATtYBwKNXAQkOmzMsBMDXIdqRzFJwhXEG6Z5BHJYi4DuBX62fQMv1th4zvxLLKdYgfNvSVBsdlou17RgM4THLqHsTR63wdjjLzVbUqLF5rCniJoqKrD2_nCmob3V7gUCGwxuKWGE7xs_cotue5Xie8wEBH7KFxG5A3pDfStOfL9twBCyF4eD',
#                 'width': 3120}],
#   'place_id': 'ChIJRdZFgIWGQIgRKRraAEvA2I0',
#   'url': 'https://maps.google.com/?cid=10221130782686714409'},
#  'status': 'OK'}

# x = [photo['photo_reference'] for photo in place['result']['photos']]

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

# address = gmaps.geocode('Aaron, 2215 Willowgrove Ave, 45409')

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

# v = address[0]['geometry']

###############################
# .reverse_geocode()    (Python wrapper)

# address = gmaps.reverse_geocode(latlng={'lat': 39.778571, 'lng': -84.070058},
#                                     result_type='street_address')
# d = address[0]['place_id']

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





# photo_urls = ['https://lh3.googleusercontent.com/p/AF1QipNhYrPCBGVFhaLRNEHM4s6YItShEPbImEHKZllA=s1600-h400']

# max_imgs = 5 if len(photo_urls) >= 5 else len(photo_urls) - 1

obj = {
        'errors':['l']
}
if obj['errors']:
    a = 1 
obj['address'] = 'hello'