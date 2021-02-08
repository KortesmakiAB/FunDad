const base_url = 'https://127.0.0.1:5000';

window.onload = function() {
    if (window.location.href === `${base_url}/destinations`){
        if (navigator.geolocation) {
            const position = navigator.geolocation.getCurrentPosition(success);
            console.log(position);
          } else {
            console.log("Geolocation is not supported by this browser.");
          }
    }
}

function success(position){
    const coords = position.coords
    // console.log('lat', coords.latitude, "long", coords.longitude);
    // app.js:16 lat 39.698432 long -84.1416704

    travelTimes = getTravelTimes(coords)
}

async function getTravelTimes(coords){
    const travelTimes = await axios.get('')
}