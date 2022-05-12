//[Engelsk - Norsk]
let food_database = [
  [['food'],['mat']], 
  [['cupcake', 'muffin'],['muffin']], 
  [['to eat'],['å spise']],
  [['drinks'],['drikke']], 
  [['to drink'],['å drikke']], 
  [['cheese'],['ost']], 
  [['milk'],['melk']], 
  [['apple'],['eple']], 
  [['chocolate'],['sjokolade']], 
  [['ham'],['skinke']],
  [['bread'],['brød']],
  [['tomato'],['tomat']],
  [['potato'],['potet']],
  [['cucumber'],['agurk']],
  [['coffee'],['kaffe']],
  [['tea'],['te']],
  [['jam'],['syltetøy']],
  [['banana'],['banan']],
  [['candy', 'sweets', 'lollies'],['godteri']]
]

let body_database = [
  [['arm'],['arm']],
  [['leg'],['ben']],
  [['head'],['hode']],
  [['nose'],['nese']],
  [['teeth'],['tenner']],
  [['foot'],['fot']],
  [['feet'],['føtter']],
  [['ear'],['øre']],
  [['chin'],['hake']],
  [['eyes'],['øyne', 'øyer']],
  [['hair'],['hår']],
  [['finger'],['finger']]
]

let animal_database = [
  [['dog'],['hund']],
  [['cat'],['katt']],
  [['horse'],['hest']],
  [['sheep'],['sau']],
  [['fish'],['fisk']],
  [['moose'],['elg']],
  [['hen'],['høne']],
  [['cow'],['ku']],
  [['elephant'],['elefant']],
  [['fox'],['rev']],
  [['bull', 'ox'],['okse']],
  [['lion'],['løve']],
  [['puppy'],['valp']],
  [['kitten'],['kattunge']],
  [['shark'],['hai']],
  [['jellyfish'],['manet']]
]

let house_database = [
  [['house'],['hus']],
  [['bathroom'],['bad']],
  [['kitchen'],['kjøkken']],
  [['window'],['vindu']],
  [['grass'],['gress']],

  [['bed'],['seng']],
  [['sink'],['vask']],
  [['couch'],['sofa']],
  [['mirror'],['speil']],
  [['cupboard'],['skap', 'kott']],

  [['chair'],['stol']],
  [['books'],['bøker']],
  [['table'],['bord']],
  [['door'],['dør']]
]

let umbrella_database = [
  [['winter'],['vinter']],
  [['summer'],['sommer']],
  [['spring'],['vår']],
  [['autumn', 'fall'],['høst']],
  [['weather'],['vær']],

  [['rainy', 'rain'],['regn']],
  [['sunny', 'sun'],['sol']],
  [['foggy'],['tåkete']],
  [['raincoat'],['regnjakke']],
  [['umbrella'],['paraply']],

  [['hot'],['varmt']],
  [['cold'],['kaldt']]
]


let main_database = []

let prize_database = [
  'cat.PNG', 'fox.PNG', 'spiderman.PNG', 'superman.PNG', 'dog.PNG', 'cupcake.PNG', 'formel1.PNG',
  'pikachu.PNG', 'rose.PNG', 'boat.PNG', 'cookie.PNG', 'books.PNG', 'fotball.PNG', 'boat2.PNG', 'donaldduck.PNG',
  'eevee.PNG', 'mario.PNG', 'luigi.PNG', 'rosalina.PNG', 'wolf.PNG', 'pokemon.PNG', 'pokemon2.PNG', 'ironman.PNG',
  'fox2.PNG', 'crystal.PNG', 'frozen.PNG', 'bighero.PNG', 'treehouse.PNG', 'encanto.PNG', 'link.PNG', 'space.PNG',
  'flowers.JPG', 'coffee.JPG', 'owl.JPG', 'signs.PNG', 'dog2.JPG', 'elk.JPG', 'cat2.PNG', 'flower2.JPG', 'land.JPG',
  'coala.PNG', 'cat3.PNG', 'flower3.JPG', 'art.PNG', 'cat4.PNG', 'brave.PNG', 'mulan.PNG', 'owl2.PNG', 'heart.jpg',
  'chill.jpg', 'city.PNG', 'flower4.PNG', 'fotball2.jpg', 'animals.PNG', 'art2.PNG', 'balloon.JPG', 'dog3.PNG',
  'dinosaur.PNG', 'dog4.JPG'
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

//Subject? 0=FOOD; 1=BODY; 2=ANIMALS; 3=HOUSE;
var tema = 0

//Fra engelsk(0) eller norsk(1)?
var spraak = 0

var can_change = true

//Denne kjører når vi starter opp siden
function start_up(){
  //Sjekker hvilket tema vi er på og lager en ny database
  check_tema()

  //Printer ut info
  console.log("Mulige ord:", main_database.length)
  console.log("Mulige stickers:", prize_database.length)
  console.log("Game loaded!")
  console.log("---------------")

  change_img()
}

function check_tema(){
  if(tema == 0){//FOOD
    main_database = food_database.slice(0) //Kopierer ord_database
  }
  if(tema == 1){//BODY
    main_database = body_database.slice(0) //Kopierer ord_database
  }
  if(tema == 2){//ANIMAL
    main_database = animal_database.slice(0) //Kopierer ord_database
  }
  if(tema == 3){//HOUSE
    main_database = house_database.slice(0) //Kopierer ord_database
  }
  if(tema == 4){//UMBRELLA
    main_database = umbrella_database.slice(0) //Kopierer ord_database
  }
}

function change_img(){
  clicked = false
  current_word = Math.floor(Math.random()*main_database.length); //Lager et random tall for å velge random ord i databasen
  document.getElementById("oppg_img").src = "Bilder/spill_img/" + main_database[current_word][0][0]  + ".png" //Ny bildelink
  console.log("Nytt ord:", main_database[current_word])
  document.getElementById('svar_input').value = null
  clicked = false
  if(spraak == 0){
    document.getElementById('shown_word').innerHTML = main_database[current_word][1][0]
  }else{document.getElementById('shown_word').innerHTML = main_database[current_word][0][0]}
}


//Sjekker om svaret er riktig
function check_answer(){
  if(clicked == true){return}
  clicked = true
  var wrong = true
  var user_answer = document.getElementById('svar_input').value //Sjekker hva som står i Input Boksen
  user_answer = user_answer.toLowerCase() //Gjør om til små bokstaver
  for(i=0; i<main_database[current_word][spraak].length; i++){
    if(user_answer == main_database[current_word][spraak][i]){
      audio_rett.play()
      wrong = false
      document.activeElement.blur()
      remove_item_database()
      get_xp()
      break
    }
  }
  if(user_answer.toLowerCase() == '#getall'){
    juks()
    document.getElementById('svar_input').style.color = 'orange'
    wrong = false
    document.activeElement.blur()
    clicked = false
  }

  if(user_answer.toLowerCase() == '#easymode'){
    juks2()
    document.getElementById('svar_input').style.color = 'orange'
    wrong = false
    document.activeElement.blur()
    clicked = false
  }

  if(wrong == true){
    document.getElementById('svar_input').style.color = 'red'
    document.activeElement.blur()
    clicked = false
  }
}



//Fjerner bildet du akkurat hadde fra databasen slik at du ALLTID får et nytt bilde.
function remove_item_database(){
  //Fjerner ordet fra databasen
  main_database.splice(current_word, 1)

  //Resetter databasen hvis den er tom
  if(main_database.length == 0){
    console.log("Resetter database..")
    check_tema()
  }

  if(tema == 0){console.log(main_database.length + "/" + food_database.length + " ord igjen")}
  if(tema == 1){console.log(main_database.length + "/" + body_database.length + " ord igjen")}
  if(tema == 2){console.log(main_database.length + "/" + animal_database.length + " ord igjen")}
  if(tema == 3){console.log(main_database.length + "/" + house_database.length + " ord igjen")}

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
    clicked = false
    document.getElementById('oppg_img').style.visibility = 'hidden'
    document.getElementById('oppg_img').src = ''
    document.getElementById("svar_input").disabled = true;
    document.getElementById("check_btn").disabled = true;
    document.getElementById('shown_word').style.visibility = 'hidden'


    //Lager bilde variabel og setter på all info
    var img = document.createElement("img");
    img.setAttribute("class", 'gift_img');
    img.setAttribute("id", "gift_img");
    img.setAttribute("onclick", "open_gift()")


    //Get random gift-img fra array
    rand = Math.floor(Math.random()*gift_sprites.length);
    img.src = "Bilder/gaver/" + gift_sprites[rand]

    //Add the image
    document.getElementById("oppg_img_div").appendChild(img);

  }else{setTimeout(() => {change_img()}, timeout)}
}


function open_gift(){
  if(clicked == true){return}
  clicked = true
  audio_open.play()
  console.log("Opening gift..")

  setTimeout(() => {
    clear()
    var temp = document.getElementById("gift_img");
    document.getElementById("oppg_img_div").removeChild(temp);

    //Resetter språk bytte knapp
    document.getElementById("chg_btn").disabled = false;
    document.getElementById("chg_btn").style.backgroundColor = 'rgb(93, 174, 240)';
    can_change = true

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

//Resetter html ting før neste bilde kommer
function clear(){
  document.getElementById('oppg_img').style.visibility = 'visible'
  document.getElementById("svar_input").disabled = false;
  document.getElementById("check_btn").disabled = false;
  document.getElementById('svar_input').style.color = 'black'
  document.getElementById('shown_word').style.visibility = 'visible'
}

addEventListener('keyup', ({key}) =>{

  document.getElementById('svar_input').style.color = 'black'

  //Sjekker om vi trykker på enterknappen
  if(key == "Enter"){
    check_answer()
  }
})

function bytt_tema(id){
  tema = id
  start_up()
}

function bytt_spraak(){
  if(can_change == true){
    if(spraak == 0){
      document.getElementById('chg_btn').innerHTML = '<b>Svar på NORSK</b>'
      document.getElementById("chg_btn").disabled = true;
      document.getElementById("chg_btn").style.backgroundColor = 'grey';
      spraak = 1
    }
    else if(spraak == 1){
      document.getElementById('chg_btn').innerHTML = '<b>Svar på ENGELSK</b>'
      document.getElementById("chg_btn").disabled = true;
      document.getElementById("chg_btn").style.backgroundColor = 'grey';
      spraak = 0
    } 
    can_change = false
    if(spraak == 0){
      document.getElementById('shown_word').innerHTML = main_database[current_word][1][0]
    }else{document.getElementById('shown_word').innerHTML = main_database[current_word][0][0]}
  }
}


function juks(){
  temp_var = prize_database.length
  for(i=0; i < temp_var; i++){
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
  }
}

function juks2(){
  xp_gained = 100; //Hvor mye xp du får per level (bør kunne ganges opp til 100)
}