

//Antall terninger
let dice_array = []
var min_dice_count = 1
var max_dice_count = 6

//Antall sider på terning
var dice_sides = [[4, '4_sides'], [6, '6_sides'], [8, '8_sides'], [10, '10_sides'], [12, '12_sides'], [20, '20_sides']]
var dice_sides_nr = 1 //6

//Farge variabler
let dice_color = ['Blue', 'Green', 'Grey', 'Orange', 'Purple', 'Red', 'White', 'Yellow']
var dice_color_nr = 5 //Red

//Lyd Variabler
var sound = new Audio('Bilder/dice.mp3');
sound.volume = 0.5;

//Pre-loader alle røde terninger
load_all_img()

function load(){
  add_dice()
}

function add_dice(){
  if(dice_array.length == max_dice_count){return}
  //Lager bilde variabel
  var img = document.createElement("img");

  //Setter Class
  img.setAttribute("class", 'dice_img');

  //Setter Id
  var temp_id = "id" + dice_array.length
  img.setAttribute("id", temp_id);

  //Bilde Source
  img.src = 'Bilder/dice/' + dice_sides[dice_sides_nr][1] + '/' + dice_color[dice_color_nr] + '/1.png'

  //Legger inn i Array
  dice_array.push(img)

  //Add the image
  document.getElementById("dice_div").appendChild(img);

  console.log("Make Dice")
}

function change_dice(nr){
  dice_sides_nr = nr
  for(i=0; i<dice_array.length; i++){
    var path = 'Bilder/dice/' + dice_sides[dice_sides_nr][1] + '/' + dice_color[dice_color_nr] + '/' + 1 + '.png'
    document.getElementById(dice_array[i].id).src = path
  }
}

function change_color(col){
  dice_color_nr = col
  for(i=0; i<dice_array.length; i++){
    var path = 'Bilder/dice/' + dice_sides[dice_sides_nr][1] + '/' + dice_color[dice_color_nr] + '/' + 1 + '.png'
    document.getElementById(dice_array[i].id).src = path
  }
}

function remove_dice(){
  if(dice_array.length == min_dice_count){return}
  var temp = document.getElementById(dice_array[dice_array.length-1].id)
  document.getElementById("dice_div").removeChild(temp);
  dice_array.splice(dice_array.length-1, 1)
}


function roll_dice(){
  sound.play()

  //Gjør om Terning verdi
  for(i=0; i<dice_array.length; i++){
    var rand = Math.floor(Math.random()*dice_sides[dice_sides_nr][0]+1);
    var path = 'Bilder/dice/' + dice_sides[dice_sides_nr][1] + '/' + dice_color[dice_color_nr] + '/' + rand + '.png'
    document.getElementById(dice_array[i].id).src = path
  }

  //Rister Terningene
  dice = document.getElementById('dice_div')
  dice.classList.add("shake");
  setTimeout(() => {dice.classList.remove("shake")}, 300)
}


function show_menu_col(){
  var content = document.getElementById('col_menu');
  
  //Gjør Div usynlig
  if (content.style.maxHeight){
    content.style.maxHeight = null;
    content.style.border = null
  }else{ //Gjør Div synlig
    content.style.maxHeight = content.scrollHeight + "px";
    content.style.borderBottom = '3px black solid'
  } 

  //Fjerner annen meny
  var old = document.getElementById('dice_menu')
  if(old.style.maxHeight){
    old.style.maxHeight = null;
    old.style.border = null
  }
}

function show_menu_dice(){
  var content = document.getElementById('dice_menu');
  //Gjør Div usynlig
  if (content.style.maxHeight){
    content.style.maxHeight = null;
    content.style.border = null
  }else{ //Gjør Div synlig
    content.style.maxHeight = content.scrollHeight + "px";
    content.style.borderBottom = '3px black solid'
  } 

  //Fjerner annen meny
  var old = document.getElementById('col_menu')
  if(old.style.maxHeight){
    old.style.maxHeight = null;
    old.style.border = null
  }
}

function close_all_menu(){
  //Fjerner annen meny
  var old = document.getElementById('dice_menu')
  if(old.style.maxHeight){
    old.style.maxHeight = null;
    old.style.border = null
  }
  var old2 = document.getElementById('col_menu')
  if(old2.style.maxHeight){
    old2.style.maxHeight = null;
    old2.style.border = null
  }
}


function load_all_img(){
  console.log("Load all RED dice")
  //Load 4-sided dice red
  var four_red = new Image()
  four_red.src = 'Bilder/dice/4_sides/Red/1.png'
  var four_red = new Image()
  four_red.src = 'Bilder/dice/4_sides/Red/2.png'
  var four_red = new Image()
  four_red.src = 'Bilder/dice/4_sides/Red/3.png'
  var four_red = new Image()
  four_red.src = 'Bilder/dice/4_sides/Red/4.png'

  //Load 6-sided dice red
  var six_red = new Image()
  six_red.src = 'Bilder/dice/6_sides/Red/1.png'
  var six_red = new Image()
  six_red.src = 'Bilder/dice/6_sides/Red/2.png'
  var six_red = new Image()
  six_red.src = 'Bilder/dice/6_sides/Red/3.png'
  var six_red = new Image()
  six_red.src = 'Bilder/dice/6_sides/Red/4.png'
  var six_red = new Image()
  six_red.src = 'Bilder/dice/6_sides/Red/5.png'
  var six_red = new Image()
  six_red.src = 'Bilder/dice/6_sides/Red/6.png'

  //Load 8-sided dice red
  var atte_red = new Image()
  atte_red.src = 'Bilder/dice/8_sides/Red/1.png'
  var atte_red = new Image()
  atte_red.src = 'Bilder/dice/8_sides/Red/2.png'
  var atte_red = new Image()
  atte_red.src = 'Bilder/dice/8_sides/Red/3.png'
  var atte_red = new Image()
  atte_red.src = 'Bilder/dice/8_sides/Red/4.png'
  var atte_red = new Image()
  atte_red.src = 'Bilder/dice/8_sides/Red/5.png'
  var atte_red = new Image()
  atte_red.src = 'Bilder/dice/8_sides/Red/6.png'
  var atte_red = new Image()
  atte_red.src = 'Bilder/dice/8_sides/Red/7.png'
  var atte_red = new Image()
  atte_red.src = 'Bilder/dice/8_sides/Red/8.png'

  //Load 10-sided dice red
  var ten_red = new Image()
  ten_red.src = 'Bilder/dice/10_sides/Red/1.png'
  var ten_red = new Image()
  ten_red.src = 'Bilder/dice/10_sides/Red/2.png'
  var ten_red = new Image()
  ten_red.src = 'Bilder/dice/10_sides/Red/3.png'
  var ten_red = new Image()
  ten_red.src = 'Bilder/dice/10_sides/Red/4.png'
  var ten_red = new Image()
  ten_red.src = 'Bilder/dice/10_sides/Red/5.png'
  var ten_red = new Image()
  ten_red.src = 'Bilder/dice/10_sides/Red/6.png'
  var ten_red = new Image()
  ten_red.src = 'Bilder/dice/10_sides/Red/7.png'
  var ten_red = new Image()
  ten_red.src = 'Bilder/dice/10_sides/Red/8.png'
  var ten_red = new Image()
  ten_red.src = 'Bilder/dice/10_sides/Red/9.png'
  var ten_red = new Image()
  ten_red.src = 'Bilder/dice/10_sides/Red/10.png'

  //Load 12-sided dice red
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/12_sides/Red/1.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/12_sides/Red/2.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/12_sides/Red/3.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/12_sides/Red/4.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/12_sides/Red/5.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/12_sides/Red/6.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/12_sides/Red/7.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/12_sides/Red/8.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/12_sides/Red/9.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/12_sides/Red/10.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/12_sides/Red/11.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/12_sides/Red/12.png'

  //Load 20-sided dice red
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/1.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/2.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/3.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/4.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/5.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/6.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/7.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/8.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/9.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/10.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/11.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/12.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/13.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/14.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/15.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/16.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/17.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/18.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/19.png'
  var twelve_red = new Image()
  twelve_red.src = 'Bilder/dice/20_sides/Red/20.png'
}
