# FUN DAD

### purpose: 
A toolkit for orchestrating kiddo fun, using the browser on your phone.
### url: 
[https://fun-dad.herokuapp.com/](https://fun-dad.herokuapp.com/)
### genesis:
Part of my daily responsibilities as a dad is to take my kids to different parks, playgrounds, and places for fun, exercise, and of course for sanity preservation. 
Sometimes I find marvelous new places but forget about them in a month. Sometimes I'm not sure about the location of a playground or how long it will take for me to get there and back before dinner.
Turn-by-turn directions would be a huge plus. 
<br>If only there was a way to wrap all of this information together in a mobile app while tossing in a dad joke for good measure...
<br>
<br>

<img src="static/mdGifs/list-map.gif" width="200">
<img src="static/mdGifs/destination.gif" width="200">
<img src="static/mdGifs/gmaps-launch.gif" width="200">
<img src="static/mdGifs/checkin.gif" width="200">

## Features:
**Table Containing users previous destinations:** <br> 
This is the data most helpful to a user when deciding which destination they will return to next.
- Name, which is a link to a page with specific location details
- Number of visits
- Date of last visit
- Travel time in traffic

**Destination Details:**  
Using the Google Places API, display any of the following data as available:
- Photo Carousel  
    Photo reference ids harvesested from Google Places API then photo urls fetched via Google Places Photos API
- Link to destination website
- Hours of operation
- Edit name of destination
- Delete destination

**Map View, an interactive Google Map:**
- Blue marker for position of user
- Red markers for positions of destinations
- Clicking on a marker reveals a cross-platform link which launches turn-by-turn directions in the native Google Maps app

**Check-In:**
- User should check-in each time visiting a destination, chosing from list of previous destinations

**Add a new destination:**
- User may use their browsers geolocation service to provide current address
- User may create and checkin to a new destination

**Create Account/Login/Logout:**
- Bcrypyt used to hash passwords


**API's used:**
- [Google Places API](https://developers.google.com/places/web-service/details)
    - [Google Place Photos API](https://developers.google.com/places/web-service/photos)
- [Google Distance Matrix](https://developers.google.com/maps/documentation/distance-matrix/overview)
- [Google Maps JavaScript](https://developers.google.com/maps/documentation/javascript/overview)
- [Google Geocoding and Reverse Geocoding](https://developers.google.com/maps/documentation/geocoding/overview)
- [Dad Jokes API](https://rapidapi.com/KegenGuyll/api/dad-jokes)
<br>
<br>

## Stack:
Front End:
- JavaScript
- AJAX
- Bootstrap
- HTML/CSS

Back End:
- Python/Flask (server)
- Flask WTF (What the Forms)
- Bcrypt (password encryption)

Database:
- PostgreSQL (database)
- Flask SQLAlchemy (ORM)
