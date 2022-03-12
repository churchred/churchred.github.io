

let ord_database = [
  'tre', 'fisk', 'katt', 'krone', 'hund', 'blomst', 'is', 'hus', 'løve', 'bjørn', 'bil', 'fly',
  'ugle', 'båt', 'eple', 'banan', 'bok', 'blå', 'rød', 'grønn', 'gul', 'elg', 'kake', 'ost', 'sol',
  'mus', 'piano', 'høne', 'sko', 'jakke', 'elefant', 'rev']


let temp_database = ord_database.slice(0)

let prize_database = [
  'cat.PNG', 'fox.PNG', 'spiderman.PNG', 'superman.PNG', 'dog.PNG', 'cupcake.PNG', 'formel1.PNG',
  'pikachu.PNG', 'rose.PNG', 'boat.PNG', 'cookie.PNG', 'books.PNG', 'fotball.PNG', 'boat2.PNG', 'donaldduck.PNG',
  'eevee.PNG', 'mario.PNG', 'luigi.PNG', 'rosalina.PNG', 'wolf.PNG', 'pokemon.PNG']



const max_antall_stamps = prize_database.length

clicked = false

var current_word = ''
var audio_rett = new Audio('Bilder/lyder/correct.mp3');
audio_rett.volume = 0.5;

var max_xp = 100; //Hvor mye xp før du får levlet opp MÅ være 100
var curr_xp = 0; //Current xp
var xp_gained = 100; //Hvor mye xp du får per level (bør være delbar av 100)
var timeout = 1500

//Sjekker om svaret er riktig
function check_answer(){
  if(clicked == false){
    clicked = true
    var user_answer = document.getElementById('svar_input').value //Sjekker hva som står i Input Boksen
    user_answer = user_answer.toLowerCase() //Gjør om til små bokstaver
    if(user_answer == current_word){
      audio_rett.play()
      remove_item_database()
      get_xp()
    }else{
      document.getElementById('svar_input').style.color = 'red'
      clicked = false
    }
  }
}

//Bytter til nytt ord og bilde
function change_img(){
  clear()
  random_number = Math.floor(Math.random()*temp_database.length); //Lager et random tall for å velge random ord i databasen
  document.getElementById("oppg_img").src = "Bilder/spill_img/" + temp_database[random_number] + ".png" //Ny bildelink
  current_word = temp_database[random_number]
  console.log("Nytt ord:", current_word)
  clicked = false
}


//Resetter html ting før neste bilde kommer
function clear(){
  document.getElementById('oppg_img_div').style.visibility = 'visible'
  document.getElementById('svar_input').style.visibility = 'visible'
  document.getElementById('check_btn').style.visibility = 'visible'
  document.getElementById('svar_input').value = ''
  document.getElementById("oppg_img").src = ''
  document.getElementById('svar_input').style.color = 'black'
}


//Fjerner bildet du akkurat hadde fra databasen slik at du ALLTID får et nytt bilde.
function remove_item_database(){
  const index = temp_database.indexOf(current_word)
  temp_database.splice(index, 1)
  console.log(temp_database.length, "/", ord_database.length)
  if(temp_database.length == 0){
    temp_database = ord_database.slice(0)
    console.log("RESETTT")
  }
}

//Hva som skjer når du får xp ved riktig svar
function get_xp(){
  document.getElementById('svar_input').style.color = 'green'
  curr_xp += xp_gained
  if(prize_database.length>0){
    if(curr_xp >= max_xp){
      curr_xp = 0
      get_prize()
    }else{setTimeout(() => {change_img()}, timeout)}
    var new_size = 'width:'+ curr_xp + '%'
    document.getElementById('xpbar').setAttribute("style",new_size);
  }else{
    console.log("None prizes left")
    setTimeout(() => {change_img()}, timeout)
  }
}

//Hva som skjer når du får en premie
function get_prize(){
  if(prize_database.length > 0){
    document.getElementById('oppg_img_div').style.visibility = 'hidden'
    document.getElementById('svar_input').style.visibility = 'hidden'
    document.getElementById('check_btn').style.visibility = 'hidden'

    //Make random stamp
    random_number = Math.floor(Math.random()*prize_database.length);


    //Lager bilde variabel og setter på all info
    var img = document.createElement("img");
    img.setAttribute("class", 'gift_img');
    img.setAttribute("id", "gift_img");
    img.setAttribute("onclick", "open_prize()")
    img.src = "Bilder/gift.png"

    //Add the image
    document.getElementById("content").appendChild(img);
  }else{setTimeout(() => {change_img()}, timeout)}
}

function open_prize(){
  clear()
  var temp = document.getElementById("gift_img");
  document.getElementById("content").removeChild(temp);
  
  //Lager bilde
  var img = document.createElement("img");
  img.src = 'Bilder/prizes/' + prize_database[random_number] 
  img.setAttribute("class", 'prize_img');
  img.setAttribute("id",  'prize_img' + prize_database[random_number]);

  //Lager en Div som bildet
  var iDiv = document.createElement('div');
  iDiv.id = prize_database[random_number];
  iDiv.className = 'stamp_block';
  document.getElementById('prize_box').appendChild(iDiv);

  //Add image
  document.getElementById(iDiv.id).appendChild(img);

  const index = prize_database.indexOf(prize_database[random_number])
  prize_database.splice(index, 1)

  document.getElementById('antall_stamps').innerText = (max_antall_stamps-prize_database.length) + '/' + max_antall_stamps
  document.getElementById(iDiv.id).scrollIntoView(false);
  change_img()
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
