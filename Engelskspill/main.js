
//[Engelsk - Norsk]
let ord_database = [
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
  [['candy', 'sweets', 'lollies'],['godteri']],

  [['arm'],['arm']],
  [['leg'],['ben']],
  [['head'],['hode']],
  [['nose'],['nese']],
  [['teeth'],['tenner']],
  [['foot'],['fot']],
  [['feet'],['føtter']],
  [['hair'],['hår']],

  [['dog'],['hund']],
  [['cat'],['katt']],
  [['horse'],['hest']],
  [['sheep'],['sau']],
  [['fish'],['fisk']],
  [['moose'],['elg']],
  [['chicken'],['høne']],
  [['cow'],['ku']],
  [['elephant'],['elefant']],
  [['fox'],['rev']],
  [['lion'],['løve']],

  [['house'],['hus']],
  [['bathroom'],['bad']],
  [['kitchen'],['kjøkken']],
  [['window'],['vindu']],
  [['grass'],['gress']],

  [['chair'],['stol']],
  [['books'],['bøker']],
  [['table'],['bord']],
  [['door'],['dør']]
]


let temp_database = ord_database.slice(0) //Kopierer ord_database


let prize_database = [
  'cat.PNG', 'fox.PNG', 'spiderman.PNG', 'superman.PNG', 'dog.PNG', 'cupcake.PNG', 'formel1.PNG',
  'pikachu.PNG', 'rose.PNG', 'boat.PNG', 'cookie.PNG', 'books.PNG', 'fotball.PNG', 'boat2.PNG', 'donaldduck.PNG',
  'eevee.PNG', 'mario.PNG', 'luigi.PNG', 'rosalina.PNG', 'wolf.PNG', 'pokemon.PNG', 'pokemon2.PNG', 'ironman.PNG',
  'fox2.PNG', 'crystal.PNG', 'frozen.PNG', 'bighero.PNG', 'treehouse.PNG', 'encanto.PNG', 'link.PNG', 'space.PNG'
]

console.log("Mulige ord:", ord_database.length)
console.log("Mulige stickers:", prize_database.length)
console.log("Game loaded!")
console.log("---------------")

const max_antall_stamps = prize_database.length

clicked = false

let current_word = []

//Fra engelsk(0) eller norsk(1)?
var spraak = 0


var can_change = true //Kan vi bytte språk?

var audio_rett = new Audio('Bilder/lyder/correct.mp3');
audio_rett.volume = 0.5;

var audio_open = new Audio('Bilder/lyder/gift_open.mp3');
audio_open.volume = 0.5;

var max_xp = 100; //Hvor mye xp før du får levlet opp MÅ være 100
var curr_xp = 0; //Current xp
var xp_gained = 20; //Hvor mye xp du får per level (bør kunne ganges opp til 100)
var timeout = 1500
var timeout_gift_open = 1000


let gift_sprites = ['gift1.png', 'gift2.png', 'gift3.png', 'gift4.png']

//Sjekker om svaret er riktig
function check_answer(){
  if(clicked == false){
    clicked = true
    var wrong = true
    var user_answer = document.getElementById('svar_input').value //Sjekker hva som står i Input Boksen
    user_answer = user_answer.toLowerCase() //Gjør om til små bokstaver
    for(i=0; i<temp_database[current_word][spraak].length; i++){
      if(user_answer == temp_database[current_word][spraak][i]){
        audio_rett.play()
        wrong = false
        document.activeElement.blur()
        remove_item_database()
        get_xp()
        break
      }
    }
    if(wrong == true){
      document.getElementById('svar_input').style.color = 'red'
      clicked = false
    }
  }
}

//Bytter til nytt ord og bilde
function change_img(){
  clear()
  random_number = Math.floor(Math.random()*temp_database.length); //Lager et random tall for å velge random ord i databasen
  document.getElementById("oppg_img").src = "Bilder/spill_img/" + temp_database[random_number][0][0] + ".png" //Ny bildelink
  current_word = random_number
  console.log("Nytt ord:", temp_database[current_word][spraak])
  console.log("--------------")
  clicked = false
  if(spraak == 0){
    document.getElementById('shown_word').innerHTML = temp_database[current_word][1][0]
  }else{document.getElementById('shown_word').innerHTML = temp_database[current_word][0][0]}
  
}

//Resetter html ting før neste bilde kommer
function clear(){
  document.getElementById('oppg_img').style.visibility = 'visible'
  document.getElementById("svar_input").disabled = false;
  document.getElementById("check_btn").disabled = false;
  document.getElementById('svar_input').value = ''
  document.getElementById("oppg_img").src = ''
  document.getElementById('svar_input').style.color = 'black'
  document.getElementById('shown_word').style.visibility = 'visible'
}


//Fjerner bildet du akkurat hadde fra databasen slik at du ALLTID får et nytt bilde.
function remove_item_database(){
  temp_database.splice(current_word, 1)
  console.log("Words left: " + temp_database.length + "/" + ord_database.length)
  if(temp_database.length == 0){
    temp_database = ord_database.slice(0)
    console.log("Resetter ord-database..")
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
    console.log("No prizes left")
    setTimeout(() => {change_img()}, timeout)
  }
}

//Hva som skjer når du får en premie
function get_prize(){
  if(prize_database.length > 0){
    document.getElementById('oppg_img').style.visibility = 'hidden'
    document.getElementById('shown_word').style.visibility = 'hidden'
    document.getElementById("svar_input").disabled = true;
    document.getElementById("check_btn").disabled = true;

    //Make random stamp
    random_number = Math.floor(Math.random()*prize_database.length);


    //Lager bilde variabel og setter på all info
    var img = document.createElement("img");
    img.setAttribute("class", 'gift_img');
    img.setAttribute("id", "gift_img");
    img.setAttribute("onclick", "open_prize()")


    //Get random gift-img fra array
    rand = Math.floor(Math.random()*gift_sprites.length);
    img.src = "Bilder/gaver/" + gift_sprites[rand]

    //Add the image
    document.getElementById("right_side").appendChild(img);
  }else{setTimeout(() => {change_img()}, timeout)}
}

function open_prize(){
  audio_open.play()
  setTimeout(() => {
    clear()
    var temp = document.getElementById("gift_img");
    document.getElementById("right_side").removeChild(temp);
    
    //Resetter språk bytte knapp
    document.getElementById("chg_btn").disabled = false;
    document.getElementById("chg_btn").style.backgroundColor = 'rgb(236, 90, 90)';
    can_change = true

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

    document.getElementById(iDiv.id).scrollIntoView(false);
    change_img()}, timeout_gift_open)
}


addEventListener('keyup', ({key}) =>{
  document.getElementById('svar_input').style.color = 'black'
  //Sjekker om vi trykker på enterknappen
  if(key == "Enter"){
    check_answer()
  }

  //if(key == " "){
  //change_img()
  //}
})



function bytt_spraak(){
  if(can_change == true){
    if(spraak == 0){
      document.getElementById('chg_btn').innerHTML = '<b>Du må skrive på [NORSK]</b> </br> <i>Trykk her for å bytte til [ENGELSK]</i>'
      document.getElementById("chg_btn").disabled = true;
      document.getElementById("chg_btn").style.backgroundColor = 'grey';
      spraak = 1
    }
    else if(spraak == 1){
      document.getElementById('chg_btn').innerHTML = '<b>Du må skrive på [ENGELSK]</b> </br> <i>Trykk her for å bytte til [NORSK]</i>'
      document.getElementById("chg_btn").disabled = true;
      document.getElementById("chg_btn").style.backgroundColor = 'grey';
      spraak = 1
    } 
    can_change = false
    if(spraak == 0){
      document.getElementById('shown_word').innerHTML = temp_database[current_word][1][0]
    }else{document.getElementById('shown_word').innerHTML = temp_database[current_word][0][0]}
  }
}