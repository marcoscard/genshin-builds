function abrir() {
    var selectiontab = document.querySelector('div#modal-container')
    var html = document.getElementsByName('html')
    selectiontab.style.display = 'block'
    
}

function selecionar(url, character) {
    var img = document.createElement('img')
    var slot = document.getElementById('slot1')
    var selectiontab = document.querySelector('div#modal-container')
    img.src = url
    img.id = 'character1'
    if (!slot.hasChildNodes()) {
        slot.appendChild(img)
    }
    save(character)
    selectiontab.style.display = 'none'
}

function save(character) {
    
}