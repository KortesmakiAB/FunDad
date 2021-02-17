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
    resp = await axios.get(`${base_url}/api/destinations/get-address`, { params: coords});
    return resp.data;    
}

function appendAddressToForm(address){
    console.log(address)
    const addyInput = document.getElementById('address');
    addyInput.value = address.address;

    const div = document.getElementById('new-dest-errors')
    for (let error of address.errors){
        const p = document.createElement('p');
        p.setAttribute('class', 'text-danger');
        p.innerText = error;
        div.append(p)
        
    }

    //Way to reduce API queries
        // add hidden form field to forms.py for place_id, lat, lng
        // append hidden vals to hidden form fields
}