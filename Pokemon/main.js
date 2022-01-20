
var counter_completed = 0
var math_completed = true
var pokeball_visible = false
var current_diff = "add10"


function change_diff(e){
  current_diff = e
  console.log(current_diff)

  if (e == "add10"){
    document.getElementById("fortegn").innerHTML = "+";
  }
  else if (e == "add20"){
    document.getElementById("fortegn").innerHTML = "+";
  }
  else if (e == "sub10"){
    document.getElementById("fortegn").innerHTML = "-";
  }
  else if (e == "sub20"){
    document.getElementById("fortegn").innerHTML = "-";
  }
  lag_regnestykke()
}

function add_pokemon(){
  rand= Math.floor(Math.random()*151+1); //Denne finner et random tall.

  //Shiny or no Shiny? Vi bruker random tall til å lage path.
  shinycalc = Math.floor(Math.random()*20+1);
  if(shinycalc == 1){path = 'Bilder' + "\\" + 'Sprites' + "\\" + rand + "s" + ".png"} 
  if(shinycalc != 1){path = 'Bilder' + "\\" + 'Sprites' + "\\" + rand + ".png"}

  var img = document.createElement("img");
  img.src = path 
  //img.height = 150; 
  //img.width = 150;

  //optionally set a css class on the image
  var class_name = "pkmn_img";
  img.setAttribute("class", class_name);

  //Add image
  document.getElementById("pokemon_box").appendChild(img);
}

//Lager 2 tilfeldige tall(0-20) til mattestykket
function lag_regnestykke(){
  if (pokeball_visible == false){
    let n1 = 0
    let n2 = 0
    math_completed = false
    document.getElementById("btn").style.background = "#fb6868";

    //Lag regnestykke men tall mellom 1-10
    if(current_diff == "add10"){
      n1 = Math.floor(Math.random()*11);
      n2 = Math.floor(Math.random()*(11-n1));
      //Gjør om det ene tallet i regnestykket slik at svaret ALDRI blir over 10.
      if(n1+n2 > 10){
        for (let i = 0; n1+n2 > 10; i++) {
          n1 = Math.floor(Math.random()*10+1);
        }
      }
    }

    //Lag regnestykke men tall mellom 1-20
    if(current_diff == "add20"){
      n1 = Math.floor(Math.random()*21);
      n2 = Math.floor(Math.random()*(21-n1));
      //Gjør om det ene tallet i regnestykket slik at svaret ALDRI blir over 10.
      if(n1+n2 > 20){
        for (let i = 0; n1+n2 > 20; i++){
          n1 = Math.floor(Math.random()*10+1);
        }
      }
    }

    //Lag MINUS regnestykke men tall mellom 1-10
    if(current_diff == "sub10"){
      n1 = Math.floor(Math.random()*10+1);
      n2 = Math.floor(Math.random()*10+1);
      //Flytter slik at n1 alltid er større enn n2
      if(n1 < n2){
        [n1, n2] = [n2, n1]
      }
    }

    //Lag MINUS regnestykke men tall mellom 1-20
    if(current_diff == "sub20"){
      n1 = Math.floor(Math.random()*20+1);
      n2 = Math.floor(Math.random()*20+1);
      //Flytter slik at n1 alltid er større enn n2
      if(n1 < n2){
        [n1, n2] = [n2, n1]
        }
    }

    document.getElementById("show_answer").innerHTML = " "; //Fjerner at det står "Bra jobba" fra forrige stykke
    document.getElementById("intext").value = n1;  //Gjør om til nytt nummer i boks 1
    document.getElementById("intext1").value = n2; //Gjør om til nytt nummer i boks 2
    document.getElementById("intext2").value = ""; //Fjerner forrige svar fra boksen
  }
}

function sjekk_svar(){
  if (pokeball_visible == false && math_completed == false){
   var n1 = document.getElementById("intext").value; 
   var n2 = document.getElementById("intext1").value;
   var user_input = document.getElementById("intext2").value;
  
   if(current_diff == "sub10" || current_diff == "sub20"){
    //adds variabel er summen av regnestykket
    adds= Number(n1) - Number(n2);}

   if(current_diff == "add10" || current_diff == "add20"){
      //adds variabel er summen av regnestykket
      adds= Number(n1) + Number(n2);}

   //Sjekker om svaret er riktig
   if(user_input == adds){
      document.getElementById("show_answer").innerHTML = "Bra jobba! Svaret ditt er riktig!";
      counter_completed += 1
      math_completed = true;
      document.getElementById("btn").style.background = "gray";
      pokeball();}
    else{
      document.getElementById("show_answer").innerHTML = "Riktig svar er: " + adds + " . Prøv igjen";}  
}
}

function pokeball(){
  if (counter_completed == 5){
    pokeball_visible = true
    counter_completed = 0;}

  if(pokeball_visible == true){
    document.getElementById("main_game_box").style.height = "500px"
    document.getElementById("btn").style.background = "gray";
    document.getElementById("btn2").style.background = "gray";

    //Lag en pokeball
    var img = document.createElement("img");
    img.src = "Bilder\\pokeball.png" 
    //Set a css class on the image
    var class_name = "pkmn_ball";
    img.setAttribute("class", class_name);
    img.setAttribute("id", "pokeball_img");
    img.setAttribute("onclick", "open_pkball()")
    //Add image
    document.getElementById("pkball").appendChild(img);
    console.log("Pokeball added")
  }
}
function open_pkball(){
  document.getElementById("main_game_box").style.height = "400px";
  document.getElementById("btn2").style.background = "#5da06e";
  pokeball_visible = false
  add_pokemon()
  var element = document.getElementById("pokeball_img");
  element.parentNode.removeChild(element);
  console.log("You opened a Pokeball")
}