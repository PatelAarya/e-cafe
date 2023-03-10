var updateBtns = document.getElementsByClassName('update-cart')

for(i = 0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId: ',productId,'Action: ',action)


        console.log('User: ',user)
        if(user == ''){
            console.log('User is not logged in')
        }
        else{
            // console.log('User is logged in, sending data')
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('User is authenticated sending data...')

    var url = '/Brothers_cafe/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId:':productId,'Action:':action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:',data)
    })
}