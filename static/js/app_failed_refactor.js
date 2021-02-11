const base_url = 'https://127.0.0.1:5000';
const errorMsg = document.getElementById('error-msg');
let coords = {};

/////////////////////////////////////////////////////////////////////
// HELPER functions

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

    travelTimes = await getTravelTimes(coords);

    appendTravelTimesDOM(travelTimes);    
}


async function handleSuccess(position){
    const lat = position.coords.latitude;
    const lng = position.coords.longitude;
    
    coords = {
        'lat': lat,
        'lng': lng
    };  
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


