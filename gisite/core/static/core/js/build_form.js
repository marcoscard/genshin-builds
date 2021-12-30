function abrir() {
    var selectiontab = document.querySelector('div#modal-container')
    selectiontab.style.display = 'block'
    
}

function selecionar(url, character) {
    var img = document.createElement('img')
    var slot = document.getElementById('slot1')
    var selectiontab = document.querySelector('div#modal-container')
    var hiddeninput_character = document.getElementById('id_characters')
    img.src = url
    img.id = 'character1'
    if (!slot.hasChildNodes()) {
        slot.appendChild(img)
    }
    var character_obj = {"1": character}
    var myJSON = JSON.stringify(character_obj)
    hiddeninput_character.value = myJSON
    selectiontab.style.display = 'none'
    console.log(character_obj)
    console.log(myJSON)
}