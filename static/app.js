const base_url = 'https://127.0.0.1:5000';

window.onload = function() {
    if (window.location.href === `${base_url}/destinations`){
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(handleSuccess);
        } 
        else {
            console.log("Geolocation is not supported by this browser.");
        }
    }
}

function handleSuccess(position){
    const lat = position.coords.latitude;
    const lng = position.coords.longitude;
    
    const coords = {
        lat,
        lng
    };
    console.log('coords:', coords);
    travelTimes = getTravelTimes(coords);
}

async function getTravelTimes(coords){
    // const travelTimes = await axios.get(`${base_url}/api/travel-times`, { params: coords});
    // return travelTimes;
    return await axios.get(`${base_url}/api/travel-times`, { params: coords});
}