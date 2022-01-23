
var counter_completed = 0 //Teller hvor mange riktige du får. Når den er lik points_for_pkm får du pokeball
var math_completed = true //Er mattestykke ferdig? Denne låser Sjekk-knappen.
var pokeball_visible = false //Om det finnes en Pokeball på skjermen, denne låser knappene.
var current_diff = "add10" //Starter på Addisjon 1-10

pokemon_counter = 0 //Antall pokemon du har.
alle_pokemon = false //Hvis du har alle pokemonene i pokedexen så er denne true

var points_for_pkm = 5; //Hvor mange riktige du trenger før du får pokemon  - orginal: 5
var chance_shiny = 20;  //Sjanse for Shiny  - orginal: 20

badges_array = ['\\Bilder\\Badges\\Kanto\\box_0.png', '\\Bilder\\Badges\\Kanto\\box_1.png','\\Bilder\\Badges\\Kanto\\box_2.png',
                '\\Bilder\\Badges\\Kanto\\box_3.png','\\Bilder\\Badges\\Kanto\\box_4.png','\\Bilder\\Badges\\Kanto\\box_5.png',
                '\\Bilder\\Badges\\Kanto\\box_6.png','\\Bilder\\Badges\\Kanto\\box_7.png', '\\Bilder\\Badges\\Kanto\\box_8.png']

//Array med all pokemon Info!
let pokedex_array = [  //Pokedex Nr, Navn, Har du den?, Er den Shiny?
[1, 'Bulbasaur',0 ,0], [2, 'Ivysaur',0 ,0], [3, 'Venusaur',0 ,0], [4, 'Charmander',0 ,0], [5, 'Charmeleon',0 ,0], [6, 'Charizard',0 ,0],
[7, 'Squirtle',0 ,0], [8, 'Wartortle',0 ,0], [9, 'Blastoise',0 ,0], [10, 'Caterpie',0 ,0], [11, 'Metapod',0 ,0], [12, 'Butterfree',0 ,0],
[13, 'Weedle',0 ,0], [14, 'Kakuna',0 ,0], [15, 'Beedrill',0 ,0], [16, 'Pidgey',0 ,0], [17, 'Pidgeotto',0 ,0], [18, 'Pidgeot',0 ,0],
[19, 'Rattata',0 ,0], [20, 'Raticate',0 ,0], [21, 'Spearow',0 ,0], [22, 'Fearow',0 ,0], [23, 'Ekans',0 ,0], [24, 'Arbok',0 ,0],
[25, 'Pikachu',0 ,0], [26, 'Raichu',0 ,0], [27, 'Sandshrew',0 ,0], [28, 'Sandslash',0 ,0], [29, 'Nidoran♀',0 ,0], [30, 'Nidorina',0 ,0],
[31, 'Nidoqueen',0 ,0], [32, 'Nidoran♂',0 ,0], [33, 'Nidorino',0 ,0], [34, 'Nidoking',0 ,0], [35, 'Clefairy',0 ,0], [36, 'Clefable',0 ,0],
[37, 'Vulpix',0 ,0], [38, 'Ninetales',0 ,0], [39, 'Jigglypuff',0 ,0], [40, 'Wigglytuff',0 ,0], [41, 'Zubat',0 ,0], [42, 'Golbat',0 ,0],
[43, 'Oddish',0 ,0], [44, 'Gloom',0 ,0], [45, 'Vileplume',0 ,0], [46, 'Paras',0 ,0], [47, 'Parasect',0 ,0], [48, 'Venonat',0 ,0],
[49, 'Venomoth',0 ,0], [50, 'Diglett',0 ,0], [51, 'Dugtrio',0 ,0], [52, 'Meowth',0 ,0], [53, 'Persian',0 ,0], [54, 'Psyduck',0 ,0],
[55, 'Golduck',0 ,0], [56, 'Mankey',0 ,0], [57, 'Primeape',0 ,0], [58, 'Growlithe',0 ,0], [59, 'Arcanine',0 ,0], [60, 'Poliwag',0 ,0],
[61, 'Poliwhirl',0 ,0], [62, 'Poliwrath',0 ,0], [63, 'Abra',0 ,0], [64, 'Kadabra',0 ,0], [65, 'Alakazam',0 ,0], [66, 'Machop',0 ,0],
[67, 'Machoke',0 ,0], [68, 'Machamp',0 ,0], [69, 'Bellsprout',0 ,0], [70, 'Weepinbell',0 ,0], [71, 'Victreebel',0 ,0], [72, 'Tentacool',0 ,0],
[73, 'Tentacruel',0 ,0], [74, 'Geodude',0 ,0], [75, 'Graveler',0 ,0], [76, 'Golem',0 ,0], [77, 'Ponyta',0 ,0], [78, 'Rapidash',0 ,0],
[79, 'Slowpoke',0 ,0], [80, 'Slowbro',0 ,0], [81, 'Magnemite',0 ,0], [82, 'Magneton',0 ,0], [83, 'Farfetchd',0 ,0], [84, 'Doduo',0 ,0],
[85, 'Dodrio',0 ,0], [86, 'Seel',0 ,0], [87, 'Dewgong',0 ,0], [88, 'Grimer',0 ,0], [89, 'Muk',0 ,0], [90, 'Shellder',0 ,0],
[91, 'Cloyster',0 ,0], [92, 'Gastly',0 ,0], [93, 'Haunter',0 ,0], [94, 'Gengar',0 ,0], [95, 'Onix',0 ,0], [96, 'Drowzee',0 ,0],
[97, 'Hypno',0 ,0], [98, 'Krabby',0 ,0], [99, 'Kingler',0 ,0], [100, 'Voltorb',0 ,0], [101, 'Electrode',0 ,0], [102, 'Exeggcute',0 ,0],
[103, 'Exeggutor',0 ,0], [104, 'Cubone',0 ,0], [105, 'Marowak',0 ,0], [106, 'Hitmonlee',0 ,0], [107, 'Hitmonchan',0 ,0], [108, 'Lickitung',0 ,0],
[109, 'Koffing',0 ,0], [110, 'Weezing',0 ,0], [111, 'Rhyhorn',0 ,0], [112, 'Rhydon',0 ,0], [113, 'Chansey',0 ,0], [114, 'Tangela',0 ,0],
[115, 'Kangaskhan',0 ,0], [116, 'Horsea',0 ,0], [117, 'Seadra',0 ,0], [118, 'Goldeen',0 ,0], [119, 'Seaking',0 ,0], [120, 'Staryu',0 ,0],
[121, 'Starmie',0 ,0], [122, 'Mr. Mime',0 ,0], [123, 'Scyther',0 ,0], [124, 'Jynx',0 ,0], [125, 'Electabuzz',0 ,0], [126, 'Magmar',0 ,0],
[127, 'Pinsir',0 ,0], [128, 'Tauros',0 ,0], [129, 'Magikarp',0 ,0], [130, 'Gyarados',0 ,0], [131, 'Lapras',0 ,0], [132, 'Ditto',0 ,0],
[133, 'Eevee',0 ,0], [134, 'Vaporeon',0 ,0], [135, 'Jolteon',0 ,0], [136, 'Flareon',0 ,0], [137, 'Porygon',0 ,0], [138, 'Omanyte',0 ,0],
[139, 'Omastar',0 ,0], [140, 'Kabuto',0 ,0], [141, 'Kabutops',0 ,0], [142, 'Aerodactyl',0 ,0], [143, 'Snorlax',0 ,0], [144, 'Articuno',0 ,0],
[145, 'Zapdos',0 ,0], [146, 'Moltres',0 ,0], [147, 'Dratini',0 ,0], [148, 'Dragonair',0 ,0], [149, 'Dragonair',0 ,0], [150, 'Mewtwo',0 ,0],
[151, 'Mew',0 ,0]
]



//-----------------------------Testing "for-loop"-------------------------------

function load_all_pokemon_in_order(){
  for(i = 0; i < pokedex_array.length; i++){
    path = 'Bilder' + "\\" + 'Sprites' + "\\" + pokedex_array[i][0] + ".png"
    var img = document.createElement("img");
    img.src = path 
    var class_name = "pkmn_img";
    img.setAttribute("class", class_name);
    img.setAttribute("id", i);
    pokedex_array[i][3] = 1
    pokemon_counter += 1
    document.getElementById("antall pokemon").innerHTML = ("&nbsp" + pokemon_counter + "/" + "151")
    console.log("Added:", pokedex_array[i][1], "Pokedex:", pokemon_counter, "/", pokedex_array.length)
    if(pokemon_counter == pokedex_array.length){alle_pokemon = true;}
    document.getElementById("pokemon_box").appendChild(img);}
}

function load_all_pokemon_normal_way(x){
  for(i=0; i < pokedex_array.length; i++){
    add_pokemon()}
}

//----------------------------------------------------------------------------

//Cookie Saving
function cookie_save(){
  //localStorage.setItem("points", points)
  for(i = 0; i<pokedex_array.length; i++){
    localStorage.setItem(pokedex_array[i][0]+"_got", pokedex_array[i][2])
    localStorage.setItem(pokedex_array[i][0]+"_shiny", pokedex_array[i][3])
  } 
}

//Cookie Loading
function cookie_load(){
  console.log("Game Loaded!")
  //console.log(localStorage)
  var array = [];
  try{
    if(localStorage.length > 5){
      for(i = 0; i<pokedex_array.length; i++){
        pokedex_array[i][2] = localStorage.getItem(pokedex_array[i][0]+"_got")
        pokedex_array[i][3] = localStorage.getItem(pokedex_array[i][0]+"_shiny")
        if(pokedex_array[i][2] == 1){load_spesific_pokemon(i);}
      }
      
    }
  }
  catch(error_msg){
    console.log(error_msg)
  }
  badges_check()
}

function load_spesific_pokemon(y){
  if(pokedex_array[y][3] == 0){var path = 'Bilder' + "\\" + 'Sprites' + "\\" + pokedex_array[y][0] + ".png"}
  if(pokedex_array[y][3] == 1){var path = 'Bilder' + "\\" + 'Sprites' + "\\" + pokedex_array[y][0] + "s" + ".png"}
  var img = document.createElement("img");

  img.src = path 
  
  if(pokedex_array[y][3] == 0){var class_name = "pkmn_img";}
  if(pokedex_array[y][3] == 1){var class_name = "pkmn_img_shiny";}
  
  img.setAttribute("class", class_name);
  img.setAttribute("id", y);

  pokemon_counter += 1
  document.getElementById("antall pokemon").innerHTML = ("&nbsp" + pokemon_counter + "/" + "151")
  //console.log("Added:", pokedex_array[y][1], "Pokedex:", pokemon_counter, "/", pokedex_array.length)

  if(pokemon_counter == pokedex_array.length){alle_pokemon = true;}

  //Add image
  document.getElementById("pokemon_box").appendChild(img);
}

function badges_check(){
  //console.log(document.getElementById("badges_box"))
  if(pokemon_counter >= 0){
    var badge_number = 0;
    var img = document.createElement("img");
    var path = badges_array[badge_number] 
  }
  if(pokemon_counter >= 10){
    var badge_number = 1;
    var img = document.createElement("img");
    var path = badges_array[badge_number] 
  }
  if(pokemon_counter >= 25){
    var badge_number = 2;
    var img = document.createElement("img");
    var path = badges_array[badge_number] 
  }
  if(pokemon_counter >= 50){
    var badge_number = 3;
    var img = document.createElement("img");
    var path = badges_array[badge_number] 
  }
  if(pokemon_counter >= 75){
    var badge_number = 4;
    var img = document.createElement("img");
    var path = badges_array[badge_number] 
  }
  if(pokemon_counter >= 100){
    var badge_number = 5;
    var img = document.createElement("img");
    var path = badges_array[badge_number] 
  }
  if(pokemon_counter >= 120){
    var badge_number = 6;
    var img = document.createElement("img");
    var path = badges_array[badge_number] 
  }
  if(pokemon_counter >= 140){
    var badge_number = 7;
    var img = document.createElement("img");
    var path = badges_array[badge_number] 
  }
  if(pokemon_counter >= 151){
    var badge_number = 8;
    var img = document.createElement("img");
    var path = badges_array[badge_number] 
  }

  document.getElementById("badges_box").innerHTML = ""
  img.src = path
  var class_name = "badges_number_img";
  img.setAttribute("class", class_name);
  img.setAttribute("id", "Badges")
  document.getElementById("badges_box").appendChild(img);

  if(alle_pokemon == true){
    var img = document.createElement("img");
    img.src = "Bilder\\Badges\\league_trophy.png"
    var class_name = "trophy";
    img.setAttribute("class", class_name);
    img.setAttribute("id", "trophy")
    document.getElementById("badges_box").appendChild(img);
  }

}

function poeng_func(){ //Holder styr på poengene dine
  if(alle_pokemon == false){
    var lys = ""
    for(i=0; i<counter_completed; i++){
      lys = "poeng_" + (i+1)
      document.getElementById(lys).style.background = "#5da06e";
    }
    if (counter_completed == 0){
      for(i=0; i<5; i++){
        lys = "poeng_" + (i+1)
        document.getElementById(lys).style.background = "#fb6868";
      }
    }
  } 
}

function change_diff(e){
  current_diff = e
  console.log(current_diff)

  if (e == "add10"){
    document.getElementById("fortegn").innerHTML = "+";
    document.getElementById("v_grad").innerHTML = "Pluss"
  }
  else if (e == "add20"){
    document.getElementById("fortegn").innerHTML = "+";
    document.getElementById("v_grad").innerHTML = "Pluss"
  }
  else if (e == "sub10"){
    document.getElementById("fortegn").innerHTML = "-";
    document.getElementById("v_grad").innerHTML = "Minus"
  }
  else if (e == "sub20"){
    document.getElementById("fortegn").innerHTML = "-";
    document.getElementById("v_grad").innerHTML = "Minus"
  }
  else if (e == "multi1"){
    document.getElementById("fortegn").innerHTML = "*";
    document.getElementById("v_grad").innerHTML = "Ganging"
  }
  else if (e == "multi2"){
    document.getElementById("fortegn").innerHTML = "*";
    document.getElementById("v_grad").innerHTML = "Ganging"
  }
  else if (e == "div1"){
    document.getElementById("fortegn").innerHTML = ":";
    document.getElementById("v_grad").innerHTML = "Deling"
  }
  else if (e == "div2"){
    document.getElementById("fortegn").innerHTML = ":";
    document.getElementById("v_grad").innerHTML = "Deling"
  }
  
  lag_regnestykke()
}

function add_pokemon(){
  
  var temp_array = []
  //console.log(temp_array)
  for(i=0; i < pokedex_array.length; i++){
      if(pokedex_array[i][2] == 0){
        temp_array.push(pokedex_array[i])
      }
  }
  
  rand= Math.floor(Math.random()*temp_array.length); //Denne finner et random tall.

  //Shiny or no Shiny? Vi bruker random tall til å lage path.
  shinycalc = Math.floor(Math.random()*chance_shiny);
  if(shinycalc == 1){path = 'Bilder' + "\\" + 'Sprites' + "\\" + temp_array[rand][0] + "s" + ".png", console.log("A shiny!")}
  if(shinycalc != 1){path = 'Bilder' + "\\" + 'Sprites' + "\\" + temp_array[rand][0] + ".png"}

  var img = document.createElement("img");
  img.src = path 

  //optionally set a css class on the image
  if(shinycalc == 1) {var class_name = "pkmn_img_shiny"; temp_array[rand][3] = 1;} 
  if(shinycalc != 1) {var class_name = "pkmn_img";}

  img.setAttribute("class", class_name);
  img.setAttribute("id", rand);

  temp_array[rand][2] = 1

  //console.log("Added:", temp_array[rand][1], "Pokedex:", pokemon_counter, "/", pokedex_array.length)

  pokemon_counter += 1
  if(pokemon_counter == pokedex_array.length){alle_pokemon = true;}


  for(i=0; i < temp_array.length; i++){    //Gjør om på Pokedex array til å matche forandringene i temp_array
    if(temp_array[i][2] == 1){
      for(y=0; y < pokedex_array.length; y++){
        if(temp_array[i][0] == pokedex_array[y][0]){
          pokedex_array[y] = temp_array[i]
        }
      } 
    }
  }

  console.log(temp_array.length + "/" + pokedex_array.length)

  //Add image
  document.getElementById("pokemon_box").appendChild(img);
  document.getElementById("antall pokemon").innerHTML = ("&nbsp" + pokemon_counter + "/" + "151")
  cookie_save()
  badges_check()
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
    
    //Lag GANGE regnestykke innen for 1-5 gangetabellen.
    if(current_diff == "multi1"){
      n1 = Math.floor(Math.random()*5+1);
      n2 = Math.floor(Math.random()*10+1);
    }

    //Lag GANGE regnestykke innen for 1-10 gangetabellen.
    if(current_diff == "multi2"){
      n1 = Math.floor(Math.random()*10+1);
      n2 = Math.floor(Math.random()*10+1);
    }

    //Lag DELE regnestykke innen for 1-5 gangetabellen.
    if(current_diff == "div1"){
      n1 = Math.floor(Math.random()*5+1);
      n2 = Math.floor(Math.random()*10+1);
      n1 = n1*n2
    }

    //Lag DELE regnestykke innen for 1-5 gangetabellen.
    if(current_diff == "div2"){
      n1 = Math.floor(Math.random()*10+1);
      n2 = Math.floor(Math.random()*10+1);
      n1 = n1*n2
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
  
   //Sjekker Minus regnestykker
   if(current_diff == "sub10" || current_diff == "sub20"){
    adds= Number(n1) - Number(n2);}

    //Sjekker Pluss regnestykker
   if(current_diff == "add10" || current_diff == "add20"){
      adds= Number(n1) + Number(n2);}
  
   //Sjekker Gange regnestykker
   if(current_diff == "multi1" || current_diff == "multi2"){
     adds= (Number(n1) * Number(n2));}

   //Sjekker Dele regnestykker
   if(current_diff == "div1" || current_diff == "div2"){
     adds= (Number(n1) / Number(n2));}


   //Sjekker om svaret er riktig
   if(user_input == adds){
      document.getElementById("show_answer").innerHTML = "Bra jobba! Svaret ditt er riktig!";
      counter_completed += 1
      math_completed = true;
      document.getElementById("btn").style.background = "gray";
      poeng_func()
      pokeball()}
    else{
      document.getElementById("show_answer").innerHTML = "Det er ikke riktig. Prøv igjen";}  
}
}

function pokeball(){
  if (alle_pokemon == false){
    if (counter_completed == points_for_pkm){
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
      //console.log("Pokeball added")
    }
  }
}

function open_pkball(){
  document.getElementById("main_game_box").style.height = "400px";
  document.getElementById("btn2").style.background = "#5da06e";
  pokeball_visible = false
  add_pokemon()
  var element = document.getElementById("pokeball_img");
  element.parentNode.removeChild(element);
  poeng_func() //Teller poeng
  lag_regnestykke()
}