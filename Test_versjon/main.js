
var counter_completed = 0 //Teller hvor mange riktige du får. Når den er lik points_for_pkm får du pokeball
var math_completed = true //Er mattestykke ferdig? Denne låser Sjekk-knappen.
var pokeball_visible = false //Om det finnes en Pokeball på skjermen, denne låser knappene.
var current_diff = "add10" //Starter på Addisjon 1-10

pokemon_counter = 0 //Antall pokemon du har.
alle_pokemon = false //Hvis du har alle pokemonene i pokedexen så er denne true

reset_button = false

sprites_dir = "Sprites2"
//var audio_rett = new Audio('Bilder\\rett_svar.mp3');
//audio_rett.volume = 0.3;

var points_for_pkm = 5; //Hvor mange riktige du trenger før du får pokemon  - orginal: 5
var chance_shiny = 20;  //Sjanse for Shiny  - orginal: 20
var shiny_chance_list = [20, 10, 5, 3, 2, 1]
var reset_counter = 0

let badges_array_kanto = ['Bilder\\Badges\\Kanto\\box_0.png','Bilder\\Badges\\Kanto\\box_1.png','Bilder\\Badges\\Kanto\\box_2.png',
                          'Bilder\\Badges\\Kanto\\box_3.png','Bilder\\Badges\\Kanto\\box_4.png','Bilder\\Badges\\Kanto\\box_5.png',
                          'Bilder\\Badges\\Kanto\\box_6.png','Bilder\\Badges\\Kanto\\box_7.png','Bilder\\Badges\\Kanto\\box_8.png'
]

let badges_array_johto = ['Bilder\\Badges\\Johto\\box_0.png','Bilder\\Badges\\Johto\\box_1.png','Bilder\\Badges\\Johto\\box_2.png',
                          'Bilder\\Badges\\Johto\\box_3.png','Bilder\\Badges\\Johto\\box_4.png','Bilder\\Badges\\Johto\\box_5.png',
                          'Bilder\\Badges\\Johto\\box_6.png','Bilder\\Badges\\Johto\\box_7.png','Bilder\\Badges\\Johto\\box_8.png'
]

let badges_array_hoenn = ['Bilder\\Badges\\Hoenn\\box_0.png','Bilder\\Badges\\Hoenn\\box_1.png','Bilder\\Badges\\Hoenn\\box_2.png',
                          'Bilder\\Badges\\Hoenn\\box_3.png','Bilder\\Badges\\Hoenn\\box_4.png','Bilder\\Badges\\Hoenn\\box_5.png',
                          'Bilder\\Badges\\Hoenn\\box_6.png','Bilder\\Badges\\Hoenn\\box_7.png','Bilder\\Badges\\Hoenn\\box_8.png'
]


                
//Array med all pokemon Info!       //Pokedex Nr, Navn, Har du den?, Er den Shiny?
let pokedex_array_kanto = [  
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
[121, 'Starmie',0 ,0], [122, 'Mr.Mime',0 ,0], [123, 'Scyther',0 ,0], [124, 'Jynx',0 ,0], [125, 'Electabuzz',0 ,0], [126, 'Magmar',0 ,0],
[127, 'Pinsir',0 ,0], [128, 'Tauros',0 ,0], [129, 'Magikarp',0 ,0], [130, 'Gyarados',0 ,0], [131, 'Lapras',0 ,0], [132, 'Ditto',0 ,0],
[133, 'Eevee',0 ,0], [134, 'Vaporeon',0 ,0], [135, 'Jolteon',0 ,0], [136, 'Flareon',0 ,0], [137, 'Porygon',0 ,0], [138, 'Omanyte',0 ,0],
[139, 'Omastar',0 ,0], [140, 'Kabuto',0 ,0], [141, 'Kabutops',0 ,0], [142, 'Aerodactyl',0 ,0], [143, 'Snorlax',0 ,0], [144, 'Articuno',0 ,0],
[145, 'Zapdos',0 ,0], [146, 'Moltres',0 ,0], [147, 'Dratini',0 ,0], [148, 'Dragonair',0 ,0], [149, 'Dragonite',0 ,0], [150, 'Mewtwo',0 ,0],
[151, 'Mew',0 ,0]
]

let pokedex_array_johto = [
[152,'Chikorita',0 ,0], [153,'Bayleef',0 ,0], [154,'Meganium',0 ,0], [155,'Cyndaquil',0 ,0], [156,'Quilava',0 ,0], [157,'Typhlosion',0 ,0], 
[158,'Totodile',0 ,0], [159,'Croconaw',0 ,0], [160,'Feraligatr',0 ,0], [161,'Sentret',0 ,0], [162,'Furret',0 ,0], [163,'Hoothoot',0 ,0], 
[164,'Noctowl',0 ,0], [165,'Ledyba',0 ,0], [166,'Ledian',0 ,0], [167,'Spinarak',0 ,0], [168,'Ariados',0 ,0], [169,'Crobat',0 ,0], 
[170,'Chinchou',0 ,0], [171,'Lanturn',0 ,0], [172,'Pichu',0 ,0], [173,'Cleffa',0 ,0], [174,'Igglybuff',0 ,0], [175,'Togepi',0 ,0], 
[176,'Togetic',0 ,0], [177,'Natu',0 ,0], [178,'Xatu',0 ,0], [179,'Mareep',0 ,0], [180,'Flaaffy',0 ,0], [181,'Ampharos',0 ,0], 
[182,'Bellossom',0 ,0], [183,'Marill',0 ,0], [184,'Azumarill',0 ,0], [185,'Sudowoodo',0 ,0], [186,'Politoed',0 ,0], [187,'Hoppip',0 ,0], 
[188,'Skiploom',0 ,0], [189,'Jumpluff',0 ,0], [190,'Aipom',0 ,0], [191,'Sunkern',0 ,0], [192,'Sunflora',0 ,0], [193,'	Yanma',0 ,0], 
[194,'Wooper',0 ,0], [195,'Quagsire',0 ,0], [196,'Espeon',0 ,0], [197,'Umbreon',0 ,0], [198,'Murkrow',0 ,0], [199,'Slowking',0 ,0], 
[200,'Misdreavus',0 ,0], [201,'Unown',0 ,0], [202,'Wobbuffet',0 ,0], [203,'Girafarig',0 ,0], [204,'Pineco',0 ,0], [205,'Forretress',0 ,0], 
[206,'Dunsparce',0 ,0], [207,'Gligar',0 ,0], [208,'Steelix',0 ,0], [209,'Snubbull',0 ,0], [210,'Granbull',0 ,0], [211,'Qwilfish',0 ,0], 
[212,'Scizor',0 ,0], [213,'Shuckle',0 ,0], [214,'Heracross',0 ,0], [215,'Sneasel',0 ,0], [216,'Teddiursa',0 ,0], [217,'Ursaring',0 ,0], 
[218,'Slugma',0 ,0], [219,'Magcargo',0 ,0], [220,'Swinub',0 ,0], [221,'Piloswine',0 ,0], [222,'Corsola',0 ,0], [223,'Remoraid',0 ,0], 
[224,'Octillery',0 ,0], [225,'Delibird',0 ,0], [226,'Mantine',0 ,0], [227,'Skarmory',0 ,0], [228,'Houndour',0 ,0], [229,'Houndoom',0 ,0], 
[230,'Kingdra',0 ,0], [231,'Phanpy',0 ,0], [232,'Donphan',0 ,0], [233,'Porygon2',0 ,0], [234,'Stantler',0 ,0], [235,'Smeargle',0 ,0],
[236,'Tyrogue',0 ,0], [237,'Hitmontop',0 ,0], [238,'Smoochum',0 ,0], [239,'Elekid',0 ,0], [240,'Magby',0 ,0], [241,'Miltank',0 ,0],
[242,'Blissey',0 ,0], [243,'Raikou',0 ,0], [244,'Entei',0 ,0], [245,'Suicune',0 ,0], [246,'Larvitar',0 ,0], [247,'Pupitar',0 ,0],
[248,'Tyranitar',0 ,0], [249,'Lugia',0 ,0], [250,'Ho_oh',0 ,0], [251,'Celebi',0 ,0]
]

let pokedex_array_hoenn = [
[252,'Treecko',0 ,0], [253,'Grovyle',0 ,0], [254,'Sceptile',0 ,0], [255,'Torchic',0 ,0], [256,'Combusken',0 ,0], [257,'Blaziken',0 ,0], 
[258,'Mudkip',0 ,0], [259,'Marshtomp',0 ,0], [260,'Swampert',0 ,0], [261,'Poochyena',0 ,0], [262,'Mightyena',0 ,0], [263,'Zigzagoon',0 ,0], 
[264,'Linoone',0 ,0], [265,'Wurmple',0 ,0], [266,'Silcoon',0 ,0], [267,'Beautifly',0 ,0], [268,'Cascoon',0 ,0], [269,'Dustox',0 ,0], 
[270,'Lotad',0 ,0], [271,'Lombre',0 ,0], [272,'Ludicolo',0 ,0], [273,'Seedot',0 ,0], [274,'Nuzleaf',0 ,0], [275,'Shiftry',0 ,0], 
[276,'Taillow',0 ,0], [277,'Swellow',0 ,0], [278,'Wingull',0 ,0], [279,'Pelipper',0 ,0], [280,'Ralts',0 ,0], [281,'Kirlia',0 ,0], 
[282,'Gardevoir',0 ,0], [283,'Surskit',0 ,0], [284,'Masquerain',0 ,0], [285,'Shroomish',0 ,0], [286,'Breloom',0 ,0], [287,'Slakoth',0 ,0], 
[288,'Vigoroth',0 ,0], [289,'Slaking',0 ,0], [290,'Nincada',0 ,0], [291,'Ninjask',0 ,0], [292,'Shedinja',0 ,0], [293,'Whismur',0 ,0], 
[294,'Loudred',0 ,0], [295,'Exploud',0 ,0], [296,'Makuhita',0 ,0], [297,'Hariyama',0 ,0], [298,'Azurill',0 ,0], [299,'Nosepass',0 ,0], 
[300,'Skitty',0 ,0], [301,'Delcatty',0 ,0], [302,'Sableye',0 ,0], [303,'Mawile',0 ,0], [304,'Aron',0 ,0], [305,'Lairon',0 ,0], 
[306,'Aggron',0 ,0], [307,'Meditite',0 ,0], [308,'Medicham',0 ,0], [309,'Electrike',0 ,0], [310,'Manectric',0 ,0], [311,'Plusle',0 ,0], 
[312,'Minun',0 ,0], [313,'Volbeat',0 ,0], [314,'Illumise',0 ,0], [315,'Roselia',0 ,0], [316,'Gulpin',0 ,0], [317,'Swalot',0 ,0], 
[318,'Carvanha',0 ,0], [319,'Sharpedo',0 ,0], [320,'Wailmer',0 ,0], [321,'Wailord',0 ,0], [322,'Numel',0 ,0], [323,'Camerupt',0 ,0], 
[324,'Torkoal',0 ,0], [325,'Spoink',0 ,0], [326,'Grumpig',0 ,0], [327,'Spinda',0 ,0], [328,'Trapinch',0 ,0], [329,'Vibrava',0 ,0], 
[330,'Flygon',0 ,0], [331,'Cacnea',0 ,0], [332,'Cacturne',0 ,0], [333,'Swablu',0 ,0], [334,'Altaria',0 ,0], [335,'Zangoose',0 ,0], 
[336,'Seviper',0 ,0], [337,'Lunatone',0 ,0], [338,'Solrock',0 ,0], [339,'Barboach',0 ,0], [340,'Whiscash',0 ,0], [341,'Corphish',0 ,0], 
[342,'Crawdaunt',0 ,0], [343,'Baltoy',0 ,0], [344,'Claydol',0 ,0], [345,'Lileep',0 ,0], [346,'Cradily',0 ,0], [347,'Anorith',0 ,0], 
[348,'Armaldo',0 ,0], [349,'Feebas',0 ,0], [350,'Milotic',0 ,0], [351,'Castform',0 ,0], [352,'Kecleon',0 ,0], [353,'Shuppet',0 ,0], 
[354,'Banette',0 ,0], [355,'Duskull',0 ,0], [356,'Dusclops',0 ,0], [357,'Tropius',0 ,0], [358,'Chimecho',0 ,0], [359,'Absol',0 ,0], 
[360,'Wynaut',0 ,0], [361,'Snorunt',0 ,0], [362,'Glalie',0 ,0], [363,'Spheal',0 ,0], [364,'Sealeo',0 ,0], [365,'Walrein',0 ,0], 
[366,'Clamperl',0 ,0], [367,'Huntail',0 ,0], [368,'Gorebyss',0 ,0], [369,'Relicanth',0 ,0], [370,'Luvdisc',0 ,0], [371,'Bagon',0 ,0], 
[372,'Shelgon',0 ,0], [373,'Salamence',0 ,0], [374,'Beldum',0 ,0], [375,'Metang',0 ,0], [376,'Metagross',0 ,0], [377,'Regirock',0 ,0], 
[378,'Regice',0 ,0], [379,'Registeel',0 ,0], [380,'Latias',0 ,0], [381,'Latios',0 ,0], [382,'Kyogre',0 ,0], [383,'Groudon',0 ,0],
[384,'Rayquaza',0 ,0], [385,'Jirachi',0 ,0], [386,'Deoxys',0 ,0]
]

let pokedex_array = pokedex_array_kanto
let badges_array = badges_array_kanto

var current_region = "Kanto"
var max_pokemon = 151;
var travel_buttons = false

var goto_johto = false
var goto_hoenn = false

//Switch Region!

function switch_region(sent_region){
  //TIL KANTO
  if(sent_region == "Kanto" && current_region != "Kanto"){
    console.log("Traveling to ", sent_region)
    clear_pokedex_img(sent_region) //Fjerner pkmn bildene i pokedexen
    current_region = "Kanto"
    badges_array = badges_array_kanto
    document.getElementById("kanto_btn").style.background = "rgb(135, 156, 121)";
    document.getElementById("johto_btn").style.background = "rgb(163, 159, 159)";
    document.getElementById("hoenn_btn").style.background = "rgb(163, 159, 159)";
    document.getElementById("pokedex_box").style.background = "#fb6868"
    pokedex_array = pokedex_array_kanto
    pokemon_counter = 0
    max_pokemon = 151
    lag_regnestykke()
    cookie_load()
    counter_completed = 0
    poeng_func() //Resetter lysene
  }

  //TIL JOHTO
  if(sent_region == "Johto" && current_region != "Johto" && goto_johto == true){
    console.log("Traveling to ", sent_region)
    clear_pokedex_img(sent_region)
    current_region = "Johto"
    badges_array = badges_array_johto
    document.getElementById("kanto_btn").style.background = "rgb(163, 159, 159)";
    document.getElementById("johto_btn").style.background = "rgb(135, 156, 121)";
    document.getElementById("hoenn_btn").style.background = "rgb(163, 159, 159)";
    document.getElementById("pokedex_box").style.background = "#0080FF"
    pokedex_array = pokedex_array_johto
    pokemon_counter = 0
    max_pokemon = 100
    lag_regnestykke()
    cookie_load()
    counter_completed = 0
    poeng_func() //Resetter lysene
  }

  //TIL HOENN
  if(sent_region == "Hoenn" && current_region != "Hoenn" && goto_hoenn == true){
    console.log("Traveling to ", sent_region)
    clear_pokedex_img(sent_region) 
    current_region = "Hoenn"
    badges_array = badges_array_hoenn
    document.getElementById("kanto_btn").style.background = "rgb(163, 159, 159)";
    document.getElementById("johto_btn").style.background = "rgb(163, 159, 159)";
    document.getElementById("hoenn_btn").style.background = "rgb(135, 156, 121)";
    document.getElementById("pokedex_box").style.background = "#FF9933"
    pokedex_array = pokedex_array_hoenn
    pokemon_counter = 0
    max_pokemon = 135
    lag_regnestykke()
    cookie_load()
    counter_completed = 0
    poeng_func() //Resetter lysene
  }

  if(goto_hoenn == false){document.getElementById("hoenn_btn").style.background = "rgb(66, 64, 64)";}
}

function check_unlock_buttons(){
  if(current_region == "Kanto" && pokemon_counter == pokedex_array_kanto.length){
    console.log("Unlocked Johto")
    document.getElementById("johto_btn").style.background = "rgb(163, 159, 159)";
    goto_johto = true
    localStorage.setItem("goto_johto:", true)
  }

  if(current_region == "Johto" && pokemon_counter == pokedex_array_johto.length){
    console.log("Unlocked Hoenn")
    document.getElementById("hoenn_btn").style.background = "rgb(163, 159, 159)";
    localStorage.setItem("goto_hoenn:", true)
    goto_hoenn = true
  }

  if(goto_hoenn == true && current_region == "Kanto"){document.getElementById("hoenn_btn").style.background = "rgb(163, 159, 159)";}
}

function clear_pokedex_img(sent_region){
    for(i=0; i < pokedex_array.length; i++){
      if(pokedex_array[i][2] == 1){
        var elemt_delete_path = 'block' + pokedex_array[i][0];
        var elemt_delete = document.getElementById(elemt_delete_path);
        elemt_delete.remove()
        //console.log("Deleting: ", pokedex_array_kanto[i][1], "(", elemt_delete, ")")
      }
    }
}


//-----------------------------Testing "for-loop"-------------------------------

function load_all_pokemon_in_order(){
  for(i = 0; i < pokedex_array.length; i++){
    path = 'Bilder' + "\\" + sprites_dir + "\\" + pokedex_array[i][0] + ".png"
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

function remove_all_cookies(){
  console.log("RESET ALL")
  localStorage.clear();
  location.reload();
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
  document.getElementById("antall pokemon").innerHTML = ("&nbsp" + pokemon_counter + "/" + max_pokemon)
  var array = [];
  try{
    if(localStorage.length > 5){
      for(i = 0; i<pokedex_array.length; i++){
        pokedex_array[i][2] = localStorage.getItem(pokedex_array[i][0]+"_got")
        pokedex_array[i][3] = localStorage.getItem(pokedex_array[i][0]+"_shiny")
        if(pokedex_array[i][2] == null){pokedex_array[i][2] = 0}
        if(pokedex_array[i][3] == null){pokedex_array[i][3] = 0}
        if(pokedex_array[i][2] == 1){load_spesific_pokemon(i);}
      }
      
    }
  }
  catch(error_msg){
    console.log(error_msg)
  }
  
  if(pokemon_counter == pokedex_array.length){
    alle_pokemon = true;}
  if(pokemon_counter != pokedex_array.length){
    alle_pokemon = false;}
  

  console.log("Region:", current_region)
  goto_johto = localStorage.getItem("goto_johto:", goto_johto)
  goto_hoenn = localStorage.getItem("goto_hoenn:", goto_hoenn)
  if(goto_hoenn == null){goto_hoenn = false}
  if(goto_johto == null){goto_johto = false}
  if(goto_hoenn == 'false'){goto_hoenn = false}
  if(goto_johto == 'false'){goto_johto = false}
  if(goto_hoenn == "true"){goto_hoenn = true}
  if(goto_johto == "true"){goto_johto = true}
  check_unlock_buttons()
  badges_check()
  
  console.log("Johto button:", goto_johto,"  Hoenn button:", goto_hoenn)
  console.log(pokemon_counter + "/" + pokedex_array.length + " pkmn caught")
  
  if(reset_button == false || reset_button == null){check_if_finished()}

  reset_button = localStorage.getItem('reset_button')

  if(reset_button == true || reset_button == 'true'){document.getElementById('reset-1').style.visibility = "visible"}

  reset_counter = localStorage.getItem('reset_counter')
  if(reset_counter == null){reset_counter = 0}else{reset_counter = parseInt(reset_counter)}

  if(reset_counter > shiny_chance_list.length-1){chance_shiny = shiny_chance_list[shiny_chance_list.length-1]}
  else{chance_shiny = shiny_chance_list[reset_counter]}

  make_Stars() //Make reset stars!

  console.log("Number of resets:", reset_counter)
  console.log("Shiny chance: 1/", chance_shiny)

}

function load_spesific_pokemon(y){
  if(pokedex_array[y][3] == 0){var path = 'Bilder' + "\\" + sprites_dir + "\\" + pokedex_array[y][0] + ".png"}
  if(pokedex_array[y][3] == 1){var path = 'Bilder' + "\\" + sprites_dir + "\\" + pokedex_array[y][0] + "s" + ".png"}                                
  var img = document.createElement("img");

  img.src = path 
  
  if(pokedex_array[y][3] == 0){var class_name_img = "pkmn_img"; var class_name_div = "pkmn_block";}
  if(pokedex_array[y][3] == 1){var class_name_img = "pkmn_img"; var class_name_div = "pkmn_block_shiny";}
  
  img.setAttribute("class", class_name_img);
  img.setAttribute("id", y);

  pokemon_counter += 1
  document.getElementById("antall pokemon").innerHTML = ("&nbsp" + pokemon_counter + "/" + "151")
  //console.log("Added:", pokedex_array[y][1], "Pokedex:", pokemon_counter, "/", pokedex_array.length)

  if(pokemon_counter == pokedex_array.length){alle_pokemon = true;}

  //Lager en Div som bildet og tekst skal legges inn i
  var iDiv = document.createElement('div');
  var temp_id = 'block' + pokedex_array[y][0];
  iDiv.id = temp_id
  iDiv.className = class_name_div;
  document.getElementById('pokemon_box').appendChild(iDiv);

  //Add image
  document.getElementById(temp_id).appendChild(img);

  //Lager variabel for boksen som pokemon og navn skal inn i
  var theDiv = document.getElementById(temp_id);

  //Legger til pokemon navn
  var content = document.createTextNode(pokedex_array[y][1]);
  theDiv.appendChild(content);

  //Legger til pokedex nummer
  //var content2 = document.createTextNode("#" + temp_array[rand][0]);
  //theDiv.appendChild(content2);

  document.getElementById("antall pokemon").innerHTML = ("&nbsp" + pokemon_counter + "/" + max_pokemon)
}

function badges_check(){
  //console.log(badges_array[0])
  if(current_region == "Kanto"){
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
  }

  if(current_region == "Johto"){
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
    if(pokemon_counter >= 20){
      var badge_number = 2;
      var img = document.createElement("img");
      var path = badges_array[badge_number] 
    }
    if(pokemon_counter >= 40){
      var badge_number = 3;
      var img = document.createElement("img");
      var path = badges_array[badge_number] 
    }
    if(pokemon_counter >= 50){
      var badge_number = 4;
      var img = document.createElement("img");
      var path = badges_array[badge_number] 
    }
    if(pokemon_counter >= 60){
      var badge_number = 5;
      var img = document.createElement("img");
      var path = badges_array[badge_number] 
    }
    if(pokemon_counter >= 80){
      var badge_number = 6;
      var img = document.createElement("img");
      var path = badges_array[badge_number] 
    }
    if(pokemon_counter >= 90){
      var badge_number = 7;
      var img = document.createElement("img");
      var path = badges_array[badge_number] 
    }
    if(pokemon_counter >= 100){
      var badge_number = 8;
      var img = document.createElement("img");
      var path = badges_array[badge_number] 
    }
  }

  if(current_region == "Hoenn"){
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
    if(pokemon_counter >= 110){
      var badge_number = 6;
      var img = document.createElement("img");
      var path = badges_array[badge_number] 
    }
    if(pokemon_counter >= 125){
      var badge_number = 7;
      var img = document.createElement("img");
      var path = badges_array[badge_number] 
    }
    if(pokemon_counter >= 135){
      var badge_number = 8;
      var img = document.createElement("img");
      var path = badges_array[badge_number] 
    }
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
    document.getElementById("v_grad").innerHTML = "Pluss, nivå 1"
  }
  else if (e == "add20"){
    document.getElementById("fortegn").innerHTML = "+";
    document.getElementById("v_grad").innerHTML = "Pluss, nivå 2"
  }
  else if (e == "add3"){
    document.getElementById("fortegn").innerHTML = "+";
    document.getElementById("v_grad").innerHTML = "Pluss, nivå 3"
  }
  else if (e == "add4"){
    document.getElementById("fortegn").innerHTML = "+";
    document.getElementById("v_grad").innerHTML = "Pluss, nivå 4"
  }
  else if (e == "sub10"){
    document.getElementById("fortegn").innerHTML = "-";
    document.getElementById("v_grad").innerHTML = "Minus, nivå 1"
  }
  else if (e == "sub20"){
    document.getElementById("fortegn").innerHTML = "-";
    document.getElementById("v_grad").innerHTML = "Minus, nivå 2"
  }
  else if (e == "sub3"){
    document.getElementById("fortegn").innerHTML = "-";
    document.getElementById("v_grad").innerHTML = "Minus, nivå 3"
  }
  else if (e == "sub4"){
    document.getElementById("fortegn").innerHTML = "-";
    document.getElementById("v_grad").innerHTML = "Minus, nivå 4"
  }
  else if (e == "multi1"){
    document.getElementById("fortegn").innerHTML = "*";
    document.getElementById("v_grad").innerHTML = "Ganging 1-5"
  }
  else if (e == "multi2"){
    document.getElementById("fortegn").innerHTML = "*";
    document.getElementById("v_grad").innerHTML = "Ganging 1-10"
  }
  else if (e == "div1"){
    document.getElementById("fortegn").innerHTML = ":";
    document.getElementById("v_grad").innerHTML = "Deling I"
  }
  else if (e == "div2"){
    document.getElementById("fortegn").innerHTML = ":";
    document.getElementById("v_grad").innerHTML = "Deling II"
  }
  else if (e == "tiven2"){
    document.getElementById("fortegn").innerHTML = "+";
    document.getElementById("v_grad").innerHTML = "Pluss /m tiervenner"
  }
  
  lag_regnestykke(0)
}

function add_pokemon(){
  var temp_array = []
  //loader riktig pokedex inn i en temp_array
  if(current_region == "Kanto"){
    for(i=0; i < pokedex_array_kanto.length; i++){
        if(pokedex_array_kanto[i][2] == 0){
          temp_array.push(pokedex_array_kanto[i])
        }
    }
  }

  if(current_region == "Johto"){
    for(i=0; i < pokedex_array_johto.length; i++){
        if(pokedex_array_johto[i][2] == 0){
          temp_array.push(pokedex_array_johto[i])
        }
    }
  }

  if(current_region == "Hoenn"){
    for(i=0; i < pokedex_array_hoenn.length; i++){
        if(pokedex_array_hoenn[i][2] == 0){
          temp_array.push(pokedex_array_hoenn[i])
        }
    }
  }
  
  
  rand= Math.floor(Math.random()*temp_array.length); //Denne finner et random tall.

  //Shiny or no Shiny? Vi bruker random tall til å lage path.
  shinycalc = Math.floor(Math.random()*chance_shiny);
  if(shinycalc == 0){path = 'Bilder' + "\\" + sprites_dir + "\\" + temp_array[rand][0] + "s" + ".png", console.log("A shiny!")}
  if(shinycalc != 0){path = 'Bilder' + "\\" + sprites_dir + "\\" + temp_array[rand][0] + ".png"}

  var img = document.createElement("img");
  img.src = path 

  //optionally set a css class on the image
  if(shinycalc == 0) {var class_name_img = "pkmn_img"; var class_name_div = "pkmn_block_shiny"; temp_array[rand][3] = 1;} 
  if(shinycalc != 0) {var class_name_img = "pkmn_img"; var class_name_div = "pkmn_block";}

  img.setAttribute("class", class_name_img);
  img.setAttribute("id", rand);

  temp_array[rand][2] = 1

  //console.log("Added:", temp_array[rand][1], "Pokedex:", pokemon_counter, "/", pokedex_array.length)

  pokemon_counter += 1
  if(pokemon_counter == pokedex_array.length){alle_pokemon = true;}
  

  //Gjør om på Pokedex array til å matche forandringene i temp_array

  for(i=0; i < temp_array.length; i++){    
    if(temp_array[i][2] == 1){
      for(y=0; y < pokedex_array.length; y++){
        if(temp_array[i][0] == pokedex_array[y][0]){
          pokedex_array[y] = temp_array[i]
        }
      } 
    }
  }


  console.log(temp_array.length + "/" + pokedex_array.length + " pkmn left")

  //Lager en Div som bildet og tekst skal legges inn i
  var iDiv = document.createElement('div');
  var temp_id = 'block' + temp_array[rand][0];
  iDiv.id = temp_id
  iDiv.className = class_name_div;
  document.getElementById('pokemon_box').appendChild(iDiv);

  //Add image
  document.getElementById(temp_id).appendChild(img);

  //Lager variabel for boksen som pokemon og navn skal inn i
  var theDiv = document.getElementById(temp_id);

  //Legger til pokemon navn
  var content = document.createTextNode(temp_array[rand][1]);
  theDiv.appendChild(content);

  //Legger til pokedex nummer
  //var content2 = document.createTextNode("#" + temp_array[rand][0]);
  //theDiv.appendChild(content2);

  document.getElementById("antall pokemon").innerHTML = ("&nbsp" + pokemon_counter + "/" + max_pokemon)
  cookie_save()
  badges_check()
  check_unlock_buttons()
}

//Lager 2 tilfeldige tall(0-20) til mattestykket
function lag_regnestykke(ee){
  if (pokeball_visible == false && math_completed == true || ee == 0){
    let n1 = 0
    let n2 = 0
    math_completed = false
    document.getElementById("btn").style.background = "#fb6868";
    document.getElementById("btn2").style.background = "gray";

    //Lag regnestykke men tall mellom 1-10
    if(current_diff == "add10"){
      n1 = Math.floor(Math.random() * 5) + 2
      n2 = Math.floor(Math.random() * 5) + 2
    }

    //Lag regnestykke men tall mellom 1-20
    if(current_diff == "add20"){
      n1 = Math.floor(Math.random() * 12) + 3
      n2 = Math.floor(Math.random() * 7) + 3
    }

    if(current_diff == "add3"){
      n1 = Math.floor(Math.random() * 20) + 4
      n2 = Math.floor(Math.random() * 15) + 4
    }

    if(current_diff == "add4"){
      n1 = Math.floor(Math.random() * 80) + 5
      n2 = Math.floor(Math.random() * 25) + 5
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
    //Lag MINUS regnestykke level 3
    if(current_diff == "sub3"){
      n1 = Math.floor(Math.random()*40+6);
      n2 = Math.floor(Math.random()*40+6);
      //Flytter slik at n1 alltid er større enn n2
      if(n1 < n2){
        [n1, n2] = [n2, n1]
      }
    }

    //Lag MINUS regnestykke level 4
    if(current_diff == "sub4"){
      n1 = Math.floor(Math.random()*80+1);
      n2 = Math.floor(Math.random()*80+1);
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

    //Lager tall mellom 1-100 hvor enerne er tiervenner
    if(current_diff == "tiven2"){
      let ti_tall_1 = Math.floor(Math.random()*9+1);
      let ti_tall_2 = Math.floor(Math.random()*(10-ti_tall_1));
      ti_tall_1 *= 10
      ti_tall_2 *= 10
      
      let ener_tall_1 = Math.floor(Math.random()*9+1);
      let ener_tall_2 = 10 - ener_tall_1 

      n1 = ti_tall_1 + ener_tall_1 
      n2 = ti_tall_2 + ener_tall_2
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
   if(current_diff == "sub10" || current_diff == "sub20" || current_diff == "sub3" || current_diff == "sub4"){
    adds= Number(n1) - Number(n2);}

    //Sjekker Pluss regnestykker
   if(current_diff == "add10" || current_diff == "add20" || current_diff == "add3" || current_diff == "add4" || current_diff == "tiven2"){
      adds= Number(n1) + Number(n2);}
  
   //Sjekker Gange regnestykker
   if(current_diff == "multi1" || current_diff == "multi2"){
     adds= (Number(n1) * Number(n2));}

   //Sjekker Dele regnestykker
   if(current_diff == "div1" || current_diff == "div2"){
     adds= (Number(n1) / Number(n2));}


   //Sjekker om svaret er riktig
   if(user_input == adds){
      document.getElementById("show_answer").innerHTML = "Bra jobba!";
      //audio_rett.play();
      counter_completed += 1
      math_completed = true;
      document.getElementById("btn").style.background = "gray";
      document.getElementById("btn2").style.background = "#5da06e";
      poeng_func()
      pokeball()
      document.activeElement.blur();}
    else{
      document.getElementById("show_answer").innerHTML = "Prøv igjen";}  
}
}

function pokeball(){
  if (alle_pokemon == false){
    if (counter_completed == points_for_pkm){
      pokeball_visible = true
      counter_completed = 0;}

    if(pokeball_visible == true){
      document.getElementById("main_game_box").style.height = "520px"
      document.getElementById("btn").style.background = "gray";
      document.getElementById("btn2").style.background = "gray";

      //Lag en pokeball
      var img = document.createElement("img");
      if(reset_counter == 0){img.src = "Bilder\\pokeball.png"}
      if(reset_counter == 1){img.src = "Bilder\\greatball.png"}
      if(reset_counter == 2 || reset_counter == 3){img.src = "Bilder\\ultraball.png"}
      if(reset_counter >= 4){img.src = "Bilder\\masterball.png"}
      
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

function change_sprite(){
  clear_pokedex_img(current_region)
  pokemon_counter = 0
  if(sprites_dir == "Sprites1"){
    console.log("Changing to Animation!")
    sprites_dir = "Sprites2";
    document.getElementById("sprite_btn").src = "Bilder\\sprites_use_3d.png";
  }
  else if(sprites_dir == "Sprites2"){
    console.log("Changing to Sprites!")
    sprites_dir = "Sprites1"
    document.getElementById("sprite_btn").src = "Bilder\\sprites_use_pixel.png";
  }
  cookie_load()
}

function check_if_finished(){
  var temp_check = 0
  for(var i=0; i < pokedex_array_hoenn.length; i++){
    if(pokedex_array_hoenn[i][2] == 1){
      temp_check += 1
    }
  }
  if(temp_check == pokedex_array_hoenn.length){
    console.log("Finsihed is True")
    document.getElementById('reset-1').style.visibility = "visible"
    reset_button = true
    localStorage.setItem('reset_button', true)
  }
}

function resett_Spillet(e){
  console.log(e)
  if(e == 'reset-1'){
    document.getElementById('reset-1').style.backgroundColor = "gray"
    document.getElementById('reset-2').style.visibility = "visible"
    var temp_var = 0
    if(reset_counter >= shiny_chance_list.length-1){
      temp_var = shiny_chance_list.length-1
      document.getElementById('p_res').textContent = Math.floor(100 / shiny_chance_list[temp_var]) + "% " + " >> " + Math.floor(100 / shiny_chance_list[temp_var]) + "%"
    }else{
      temp_var = reset_counter
      document.getElementById('p_res').textContent = Math.floor(100 / shiny_chance_list[temp_var]) + "% " + " >> " + Math.floor(100 / shiny_chance_list[temp_var+1]) + "%"
    }

  }
  if(e == 'reset-2'){
    reset_counter += 1
    localStorage.clear();
    localStorage.setItem('reset_counter', reset_counter)
    location.reload();
  }
}


function make_Stars(){
  document.getElementById('star_div').innerHTML = ""
  for(i=0; i<reset_counter; i++){
    var img = document.createElement("img");
    img.width = 50
    img.height = 50
    img.src = "\\Bilder\\star.png"
    document.getElementById('star_div').appendChild(img);
  }
  console.log("Made ", reset_counter, " stars.")
}