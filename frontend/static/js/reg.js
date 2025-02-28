const btn_reg = document.getElementById('btn_reg')

btn_reg.addEventListener('click', async () => {
    let response = await fetch('/reg',  
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                login: document.getElementById('input_login').value,
                name: document.getElementById('input_name').value,
                surname: document.getElementById('input_surname').value,
                password: document.getElementById('input_password1').value
            })
        }
    )
    if (response.ok){
        window.location.href = '/'
    } 
    else{
        alert((await response.json()).detail)
    }
})