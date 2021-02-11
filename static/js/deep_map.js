// 10:50am. Berfore I started refactoring handle success

const base_url = 'https://127.0.0.1:5000';
const errorMsg = document.getElementById('error-msg');


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
    
    const coords = {
        lat,
        lng
    };

    if (window.location.href === `${base_url}/destinations`){
        travelTimes = await getTravelTimes(coords);

        appendTravelTimesDOM(travelTimes);
    }
    else if (window.location.href === `${base_url}/map-view`){
        makeMap(coords)
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

async function getTravelTimes(coords){
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

async function makeMap(coords){
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

    addDestinationMarkers(destData.data, map)
    
}

function addDestinationMarkers(destData, map){
    for (data of destData){
        // console.log('coords:', coords)
        const marker = new google.maps.Marker({
            position: data.TODO,
            map: map,
            title: data.TODO
        });
        
        const origin = callGetCurrPos(handleSuccess, showError, urlResource)
        const parameters = makeParameters(data, origin)

        const contentString =
            `<div id="content"> 
                <a href="https://www.google.com/maps/dir/?api=1&${parameters}&dir_action=navigate">Click this</a>
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

function makeParameters(data, origin){
    return {
        // origin: comma-separated latitude/longitude coordinates
        'origin': origin,
        'destination': data.TODO,
        'destination_place_id': data.place_id,        
    }
}