

let ord_database = ['tre', 'fisk', 'katt', 'krone', 'hund', 'blomst']
var current_word = ''
var audio_rett = new Audio('Bilder/lyder/correct.mp3');
audio_rett.volume = 0.5;

//Sjekker om svaret er riktig
function check_answer(){
  var user_answer = document.getElementById('svar_input').value //Sjekker hva som står i Input Boksen
  user_answer = user_answer.toLowerCase() //Gjør om til små bokstaver
  if(user_answer == current_word){
    audio_rett.play()
    document.getElementById('svar_input').style.color = 'green'
    setTimeout(() => {change_img()}, 1000)
    
  }else(document.getElementById('svar_input').style.color = 'red')
}

//Bytter til nytt ord og bilde
function change_img(){
  clear()
  random_number = Math.floor(Math.random()*ord_database.length); //Lager et random tall for å velge random ord i databasen
  document.getElementById("oppg_img").src = "Bilder/spill_img/" + ord_database[random_number] + ".png" //Ny bildelink
  current_word = ord_database[random_number]
  console.log("Nytt ord:", current_word)
}

function clear(){
  document.getElementById('svar_input').value = ''
  document.getElementById("oppg_img").src = ''
  document.getElementById('svar_input').style.color = 'black'
}





addEventListener('keyup', ({key}) =>{
  document.getElementById('svar_input').style.color = 'black'
  //Sjekker om vi trykker på enterknappen
  if(key == "Enter"){
    check_answer()
  }
  if(key == " "){
    change_img()
  }
})
