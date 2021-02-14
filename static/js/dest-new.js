///////////////////////////////////////////////////////
// get address form

const addyForm = document.getElementById('get-address');

addyForm.addEventListener('submit', getAddress)

async function getAddress(evt){
    evt.preventDefault();

    const urlResource = 'destinations/new';
    callGetCurrPos(urlResource); 
}

async function callReverseGeocode(){
    console.log(coords)
    resp = await axios.get(`${base_url}/api/destinations/get-address`, { params: coords});
    return resp.data;    
}

function appendAddressToForm(address){
    const addyInput = document.getElementById('address');
    addyInput.value = address.address;

    //Way to reduce API queries
        // add hidden form field to forms.py for place_id, lat, lng
        // append hidden vals to hidden form fields
}