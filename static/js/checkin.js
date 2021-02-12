const addyForm = document.getElementById('get-address');

addyForm.addEventListener('submit', getAddress)

async function getAddress(evt){
    evt.preventDefault();

    const urlResource = 'destinations/checkin';
    callGetCurrPos(urlResource); 
}

async function callReverseGeocode(){
    console.log(coords)
    resp = await axios.post(`${base_url}/api/destinations/checkin`, coords);
    return resp.data;    
}

function appendAddressToForm(address){
    console.log(address);
}