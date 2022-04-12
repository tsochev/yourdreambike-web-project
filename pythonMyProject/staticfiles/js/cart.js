let updateButtons = document.getElementsByClassName('update-cart')

for(let i = 0; i < updateButtons.length; i++){
    updateButtons[i].addEventListener('click', function (){
        let bikeId = this.dataset.bike
        let action = this.dataset.action
        console.log('bikeID:', bikeId, 'action:', action)

        console.log('USER:', user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }
        else{
            updateUserOrder(bikeId, action)
        }
    })
}

function updateUserOrder(bikeId, action){
    console.log('User is logged in, sending data..')

    let url = '/bikes/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'bike': bikeId, 'action': action})
    })

        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data:', data)
            location.reload()
        })
}


