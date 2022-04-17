

dice_color = "red"

number_of_dice = 1

dice_sides = 6

var sound = new Audio('Bilder/dice.mp3');
sound.volume = 0.5;

function add_dice_btn(nr){
  if(number_of_dice != 0){remove_dice()}
  number_of_dice = nr
  add_dice(number_of_dice)
  change_btn_col()
}

function add_dice(nr){
  for(i=0; i<nr; i++){
    var img = document.createElement("img");
    img.setAttribute("class", 'dice_img');
    temp_id = "dice_img_" + (i+1)
    img.setAttribute("id", temp_id);
  
    //Get random gift-img fra array
    rand = Math.floor(Math.random()*dice_sides+1);
    

    if(dice_sides == 6){var source = "Bilder/dice/six_sides/"}
    if(dice_sides == 10){var source = "Bilder/dice/ten_sides/"}
    if(dice_sides == 12){var source = "Bilder/dice/twelve_sides/"}

    img.src = source + (rand) + ".png"
  
    //Add the image
    document.getElementById("dice_div").appendChild(img);
  }
}

function change_dice(nr){
  dice_sides = nr
  for(i=0; i<3; i++){
    temp_id = 'btn2_' + (i+1)
    document.getElementById(temp_id).style.backgroundColor = 'rgb(180, 255, 180)'
  }
  if(dice_sides == 6){document.getElementById('btn2_1').style.backgroundColor = 'rgb(18, 219, 18)'}
  if(dice_sides == 10){document.getElementById('btn2_2').style.backgroundColor = 'rgb(18, 219, 18)'}
  if(dice_sides == 12){document.getElementById('btn2_3').style.backgroundColor = 'rgb(18, 219, 18)'}
  add_dice_btn(number_of_dice)
}

function remove_dice(){
  for(i=0; i<number_of_dice; i++){
    temp_id = "dice_img_" + (i+1)
    temp_img = document.getElementById(temp_id)
    document.getElementById("dice_div").removeChild(temp_img);
  }
  number_of_dice = 0
}


function roll_dice(){
  sound.play()
  nr = number_of_dice
  if(number_of_dice != 0){remove_dice()}
  number_of_dice = nr
  add_dice(number_of_dice)
  for(i=0; i<number_of_dice; i++){
    temp_id = "dice_img_" + (i+1)
    die = document.getElementById(temp_id)
    die.style.animation = 'MoveUpDown 1s linear', 'shake 1s linear'
  }
}


function change_btn_col(){
  for(i=0; i<6; i++){
    temp_id = 'btn_' + (i+1)
    document.getElementById(temp_id).style.backgroundColor = 'rgb(180, 255, 180)'
  }
  if(number_of_dice == 1){document.getElementById('btn_1').style.backgroundColor = 'rgb(18, 219, 18)'}
  if(number_of_dice == 2){document.getElementById('btn_2').style.backgroundColor = 'rgb(18, 219, 18)'}
  if(number_of_dice == 3){document.getElementById('btn_3').style.backgroundColor = 'rgb(18, 219, 18)'}
  if(number_of_dice == 4){document.getElementById('btn_4').style.backgroundColor = 'rgb(18, 219, 18)'}
  if(number_of_dice == 5){document.getElementById('btn_5').style.backgroundColor = 'rgb(18, 219, 18)'}
  if(number_of_dice == 6){document.getElementById('btn_6').style.backgroundColor = 'rgb(18, 219, 18)'}
}