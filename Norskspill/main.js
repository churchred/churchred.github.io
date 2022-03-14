

let ord_database_lett = [
  'ape', 'banan', 'bil', 'blå', 'bok', 'båt', 'drage', 'elg', 'eple', 'fisk',
  'fly', 'gitar', 'gris', 'gul', 'hest', 'hus', 'hår', 'is', 'kake', 'kniv',
  'krone', 'ku', 'lue', 'løve', 'melk', 'mus', 'måke', 'ost', 'piano', 'pære', 
  'rev', 'sko', 'sol', 'stol', 'tre', 'ugle', 'vei'       
]


let ord_database_middels = [
  'ape', 'banan', 'bil', 'blå', 'bok', 'båt', 'drage', 'elg', 'eple', 'fisk',
  'fly', 'gitar', 'gris', 'gul', 'hest', 'hus', 'hår', 'is', 'kake', 'kniv',
  'krone', 'ku', 'lue', 'løve', 'melk', 'mus', 'måke', 'ost', 'piano', 'pære', 
  'rev', 'sko', 'sol', 'stol', 'tre', 'ugle', 'vei',

  'badekar', 'bjørn', 'blomst', 'blyant', 'briller', 'bøtte', 'druer', 'egg',
  'ekorn', 'elefant', 'gaffel', 'grønn', 'hammer', 'hund', 'høne', 'jakke',
  'katt', 'konge', 'mais', 'nøkkel', 'robot', 'rød', 'saks', 'sau', 'seng',
  'snømann', 'sofa', 'spade', 'sverd', 'sykkel', 'vaffel', 'vann', 'vindu'
]


let main_database = []


let prize_database = [
  'cat.PNG', 'fox.PNG', 'spiderman.PNG', 'superman.PNG', 'dog.PNG', 'cupcake.PNG', 'formel1.PNG',
  'pikachu.PNG', 'rose.PNG', 'boat.PNG', 'cookie.PNG', 'books.PNG', 'fotball.PNG', 'boat2.PNG', 'donaldduck.PNG',
  'eevee.PNG', 'mario.PNG', 'luigi.PNG', 'rosalina.PNG', 'wolf.PNG', 'pokemon.PNG', 'pokemon2.PNG', 'ironman.PNG',
  'fox2.PNG', 'crystal.PNG', 'frozen.PNG', 'bighero.PNG', 'treehouse.PNG', 'encanto.PNG', 'link.PNG', 'space.PNG'
]



const max_antall_stamps = prize_database.length

clicked = false

var current_word = ''

var audio_rett = new Audio('Bilder/lyder/correct.mp3');
audio_rett.volume = 0.5;

var audio_open = new Audio('Bilder/lyder/gift_open.mp3');
audio_open.volume = 0.5;

var max_xp = 100; //Hvor mye xp før du får levlet opp MÅ være 100
var curr_xp = 0; //Current xp
var xp_gained = 20; //Hvor mye xp du får per level (bør kunne ganges opp til 100)


var antall_feil = 0
var mulige_feil = 3

//Timeout tid
var timeout = 1500;
var timeout_gift_open = 1000;

//Vanskelighets nivå
var level = 1;

//Mulig utseende på gaver
let gift_sprites = ['gift1.png', 'gift2.png', 'gift3.png', 'gift4.png']



//Denne kjører når vi starter opp siden
function start_up(){

  //Sjekker hvilke level vi er på og lager en ny database
  check_level()


  //Printer ut info
  console.log("Mulige ord:", main_database.length)
  console.log("Mulige stickers:", prize_database.length)
  console.log("Game loaded!")
  console.log("---------------")

  change_img()
}


//Sjekker hvilke level vi er på og lager en ny database
function check_level(){
  if(level == 1){
    main_database = ord_database_lett.slice(0) //Kopierer ord_database
  }
  if(level == 2){
    main_database = ord_database_middels.slice(0) //Kopierer ord_database
  }
  document.getElementById('lvl_btn_id1').innerHTML = "Nivå " + level
}

//Bytter vanskelighetsgrad 
function bytt_level(){
  if(level == 1){
    level = 2
  }
  else if(level == 2){
    level = 1
  }
  console.log("Nivå:", level)
  start_up()
}

//Resetter html ting før neste bilde kommer
function clear(){
  document.getElementById('oppg_img').style.visibility = 'visible'
  document.getElementById("svar_input").disabled = false;
  document.getElementById("check_btn").disabled = false;
  document.getElementById('svar_input').style.color = 'black'
}

//Bytter til nytt ord og bilde
function change_img(){
  current_word = Math.floor(Math.random()*main_database.length); //Lager et random tall for å velge random ord i databasen
  document.getElementById("oppg_img").src = "Bilder/spill_img/" + main_database[current_word] + ".png" //Ny bildelink
  console.log("Nytt ord:", main_database[current_word])
  document.getElementById('svar_input').value = null
  clicked = false
}

//Sjekker om svaret er riktig
function check_answer(){
  if(clicked == true){return}
  clicked = true
  var user_answer = document.getElementById('svar_input').value //Sjekker hva som står i Input Boksen
  user_answer = user_answer.toLowerCase() //Gjør om til små bokstaver
  if(user_answer == main_database[current_word]){
    audio_rett.play()
    document.activeElement.blur()
    remove_item_database()
    get_xp()
    clicked = false
    document.getElementById('rett_svar').style.visibility = 'hidden'
    antall_feil = 0
    
  }else{
    document.getElementById('svar_input').style.color = 'red'
    clicked = false
    antall_feil += 1
    console.log("Antall feil: " + antall_feil + "/" + mulige_feil)
    if(antall_feil >= mulige_feil){
      antall_feil = 0
      document.getElementById('rett_svar').style.visibility = 'visible'
      document.getElementById('rett_svar').innerHTML = main_database[current_word]
    }
  }
}

//Fjerner bildet du akkurat hadde fra databasen slik at du ALLTID får et nytt bilde.
function remove_item_database(){
  //Fjerner ordet fra databasen
  main_database.splice(current_word, 1)

  //Resetter databasen hvis den er tomn
  if(main_database.length == 0){
    console.log("Resetter database..")
    check_level()
  }

  if(level == 1){console.log(main_database.length + "/" + ord_database_lett.length + " ord igjen")}
  if(level == 2){console.log(main_database.length + "/" + ord_database_middels.length + " ord igjen")}
  console.log("---------------")
}


//Hva som skjer når du får xp ved riktig svar
function get_xp(){
  document.getElementById('svar_input').style.color = 'green'
  curr_xp += xp_gained
  if(prize_database.length>0){
    if(curr_xp >= max_xp){
      curr_xp = 0
      get_gift()
    }else{setTimeout(() => {change_img()}, timeout)}
    var new_size = 'width:'+ curr_xp + '%'
    document.getElementById('xpbar').setAttribute("style",new_size);
  }else{
    console.log("None prizes left")
    setTimeout(() => {change_img()}, timeout)
  }
}


//Hva som skjer når du får en premie
function get_gift(){
  if(prize_database.length > 0){
    document.getElementById('oppg_img').style.visibility = 'hidden'
    document.getElementById("svar_input").disabled = true;
    document.getElementById("check_btn").disabled = true;
    
    //Get random gift-img fra array
    var rand = Math.floor(Math.random()*gift_sprites.length);
    document.getElementById('gift_img').src = "Bilder/gaver/" + gift_sprites[rand]
    document.getElementById('gift_img').style.visibility = 'visible'

  }else{setTimeout(() => {change_img()}, timeout)}
}


function open_gift(){
  if(clicked == true){return}
  clicked = true
  audio_open.play()
  console.log("Opening gift..")

  setTimeout(() => {
    clear()
    document.getElementById("gift_img").style.visibility = 'hidden';

    var random_number = Math.floor(Math.random()*prize_database.length);
    
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

    prize_database.splice(random_number, 1)

    document.getElementById(iDiv.id).scrollIntoView(false);
    change_img()}, timeout_gift_open)
}


addEventListener('keyup', ({key}) =>{

  document.getElementById('svar_input').style.color = 'black'

  //Sjekker om vi trykker på enterknappen
  if(key == "Enter"){
    check_answer()
  }
})
