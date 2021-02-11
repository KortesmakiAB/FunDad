const base_url = 'https://127.0.0.1:5000';
const errorMsg = document.getElementById('error-msg');
let coords = {};

/////////////////////////////////////////////////////////////////////
// SHARED functions

function callGetCurrPos(success, error, resource){
    if (window.location.href === `${base_url}/${resource}`){
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(success, error);
            
        } 
        else {
            errorMsg.innerText = "Geolocation is not supported by this browser.";
        }
    }
}

async function handleSuccess(position){
    const lat = position.coords.latitude;
    const lng = position.coords.longitude;
    
    coords = {
        'lat': lat,
        'lng': lng
    };

    nextAction()
}

async function nextAction(){
    if (window.location.href === `${base_url}/destinations`){
        travelTimes = await getTravelTimes(coords);

        appendTravelTimesDOM(travelTimes);
    }
    else if (window.location.href === `${base_url}/map-view`){
        makeMap()
    }
}

// attr: https://www.w3schools.com/html/html5_geolocation.asp
function showError(error) {
    switch(error.code) {
      case error.PERMISSION_DENIED:
        errorMsg.innerText = "User denied the request for Geolocation."
        break;
      case error.POSITION_UNAVAILABLE:
        errorMsg.innerText = "Location information is unavailable."
        break;
      case error.TIMEOUT:
        errorMsg.innerText = "The request to get user location timed out."
        break;
      case error.UNKNOWN_ERROR:
        errorMsg.innerText = "An unknown error occurred."
        break;
    }
}


/////////////////////////////////////////////////////////////////////
// DESTINATIONS Page

window.onload = function destination() {
    const urlResource = 'destinations'

    callGetCurrPos(handleSuccess, showError, urlResource)
}

async function getTravelTimes(){
    resp = await axios.get(`${base_url}/api/travel-times`, { params: coords});
    return resp.data
}

function appendTravelTimesDOM(obj){
    for (key of Object.keys(obj)){
        const td = document.getElementById(`trvl-time-${key}`);
        td.innerText = obj[key];
    }
}

/////////////////////////////////////////////////////////////////////
// MAP VIEW Page

function initMap(){ 
    const urlResource = 'map-view';

    callGetCurrPos(handleSuccess, showError, urlResource); 
}

async function makeMap(){
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 11,
        center: coords
    });

    const marker = new google.maps.Marker({
        position: coords,
        map: map,
        icon: {
            url: "https://maps.google.com/mapfiles/ms/icons/blue-dot.png"
          }
    });

    destData = await axios.get(`${base_url}/api/coordinates`);

    addDestinationMarkers(destData.data, map, coords)
}

function addDestinationMarkers(destData, map, coords){
    const usrCoords = `${coords.lat},${coords.lng}`;

    for (dest of destData){
        const marker = new google.maps.Marker({
            position: dest.coords,
            map: map,
            title: dest.name
        });

        const contentString =
            `<div id="content"> 
                <a href="https://www.google.com/maps/dir/?api=1&origin=${usrCoords}&destination=${dest.coords}&destination_place_id=${dest.place_id}&dir_action=navigate">${dest.name}</a>
            </div>`;

        const infowindow = new google.maps.InfoWindow({
            content: contentString,
            maxWidth: 200,
        });

        marker.addListener("click", () => {
            infowindow.open(map, marker);
        });
    }
}

