const selectiontab = document.getElementById('modal-container')
const listslot = document.getElementsByClassName('slot')
let hiddeninput_character = document.getElementById('form-characters')
let slot = undefined
let character_obj = {}

function abrir(id) {
  slot = listslot[id]
  slot.id = id
  selectiontab.style.display = 'block'
}

function selecionar(url, character) {
  if (slot.hasChildNodes()) {
    let img = document.getElementById('character' + slot.id)
    img.src = url
  }
  else {
    let img = document.createElement('img')
    img.src = url
    img.id = 'character' + slot.id
    slot.appendChild(img)
  }
  character_obj[slot.id] = character
  console.log(character_obj)
  hiddeninput_character.value = JSON.stringify(character_obj)
  console.log(hiddeninput_character)
  selectiontab.style.display = 'none'

  // var myJSON = JSON.stringify(character_obj)
  // hiddeninput_character.value = myJSON
  // selectiontab.style.display = 'none'
  // console.log(character_obj)
  // console.log(myJSON)
}
