var slider_number = 0
var images = [];

maks_antall_bilder = 10 //Maks antall bilder eller videoer som kan loades om et spill/serie/film
info_page = false //Hvis denne er false vil det ikke skje noe når du trykker på tingene dine i topp lista.

top_list = []      //Denne blir til en av de 3 TOPP_LIST basert på hva vi skal se.
media_name = ""    //Hva har vi med å gjøre? Spill, serie, eller film?
media_object = ""  //Hvilken serie/spill/film skal vi ha info om?
media_path = ""    //Hvor finner vi mappa med bilder?

file_types = [".png", ".jpg", ".mp4"]


TOP_LIST_GAMES = [ //name, release date, developer, genre, summary, review
  ["Dragon Age", 
  "3. November 2009", 
  "Bioware", 
  "Fantasy, RPG", 
  "Set in the kingdom of Ferelden, the player is put in the role of a warrior, mage, or rogue coming from an elven, human, or dwarven background. The player is recruited into the Grey Wardens, an ancient order that stands against monstrous forces known as 'Darkspawn', and is tasked with defeating the Archdemon that leads them.",
  "review"],

  ["Mass Effect", 
  "14. May 2021", 
  "Bioware", 
  "Sci-fi, TPS", 
  "We follow Commander Shepard, a soldier in Earth's Systems Alliance space force. After an Earth colony discovers a new artifact left behind by an ancient civilisation, it is attacked by an unknown vessel, and the Council names Shepard its first human SPECTRE, to investigate the incident.",
  "review"],

  ["Persona 5 Royal", 
  "31. October 2019", 
  "Atlus", 
  "JRPG", 
  "It takes place in modern-day Tokyo and follows a high school student who transfers to a new school. He and other students awaken to special powers. They explore the Metaverse, a supernatural realm born from humanity's subconscious desires, to steal malevolent intent from the hearts of adults.",
  "review"],

  ["Last of Us",  
  "14. June 2013", 
  "Naughty Dog", 
  "Action-Adventure", 
  "The world changed as a mutated fungus started turning humans into mindless, cannibalistic creatures. Now 20 years later the world in in ruins and we follow the story of Joel, a smuggler tasked with escorting a teenage girl, Ellie, across a post-apocalyptic United States.",
  "review"],

  ["Red Dead Redemption 2", 
  "26. October 2018", 
  "Rockstar Games", 
  "Action-adventure, TPS", 
  "After a robbery goes badly wrong in the western town of Blackwater, Arthur Morgan and the Van der Linde gang are forced to flee. With federal agents and the best bounty hunters in the nation massing on their heels, the gang must rob, steal and fight their way across the rugged heartland of America in order to survive.",
  "review"],

  ["Witcher 3", 
  "18. May 2015", 
  "CD Projekt RED", 
  "Action-adventure, RPG", 
  "summary",
  "review"],

  ["Skyrim", 
  "11. November 2011", 
  "Bethesda Game Studios", 
  "Fantasy, RPG", 
  "Set it the world of Tamriel. We follow the the Dragonborn, on their quest to defeat Alduin the World-Eater, a dragon who is prophesied to destroy the world.",
  "review"],

  ["Portal 2", 
  "18. April 2011", 
  "Valve Corporation", 
  "FPS, Puzzle-platorm", 
  "summary",
  "review"],

  ["Stardew Valley", 
  "26. February 2016", 
  "Eric Barone", 
  "Farming Simulator, RPG", 
  "summary",
  "review"],

  ["Breath of The Wild", 
  "03. March 2017", 
  "Nintendo Entertainment", 
  "Action-adventure, &nbsp&nbsp Third-person", 
  "summary",
  "review"],

]

TOP_LIST_SERIES = [ //name, release date, seasons, studio, summary, review
  ["Leverage",
    "7. December 2008", 
    "5", 
    "TNT", 
    "A crew of high-tech crooks attempt to steal from wealthy criminals and corrupt businessmen.Former insurance claims investigator Nathan Ford heads a team of former top-criminals. They handle 'unorthodox' cases of people unlikely to get their due through regular channels and legal procedures.",
    "review"],

  ["Arcane",
    "6. November 2021", 
    "1", 
    "Riot Games, Netflix", 
    "The origins of two iconic League champions, set in the utopian Piltover and the oppressed underground of Zaun.",
    "review"],

  ["Firefly",
    "20. September 2002", 
    "1 (and 1 movie)", 
    "Joss Whedon, FOX", 
    "Set 500 years in the future after a universal civil war, the crew of a small transport spaceship takes any job so long as it puts food on the table. The disparate men and women just want to survive and maybe have better lives",
    "review"], 

  ["The Mandalorian",
    "12. November 2019", 
    "2", 
    "Jon Favreau, Disney", 
    "After the defeat of the Empire at the hands of Rebel forces, a lone bounty hunter operating in the Outer Rim, away from the dominion of the New Republic, goes on many surprising and risky adventures.",
    "review"], 

  ["Game of Thrones",
    "17. April 2011", 
    "8", 
    "HBO", 
    "In the mythical continent of Westeros, nine families of higher nobility scramble bitterly to gain power over the seven kingdoms and the Iron throne. As Westeros becomes rife with political unrests, conflicts, treachery, murder and debauchery, an ancient enemy awakens and strike the sense of doom to the living folks of Westeros.",
    "review"],

  ["Buffy The Vampire Slayer",
    "10. March 1997", 
    "7", 
    "Joss Whedon", 
    "Buffy Summers tries to live a normal life in high school while embracing her responsibilities and destiny as a hunter of vampires and demons.",
    "review"],

  ["Breaking Bad",
    "dato", 
    "seasons", 
    "studio", 
    "summary",
    "review"],

  ["Person of Interest",
    "dato", 
    "seasons", 
    "studio", 
    "summary",
    "review"],

  ["Queens Gambit",
    "dato", 
    "seasons", 
    "studio", 
    "summary",
    "review"],

  ["Avatar",
    "dato", 
    "seasons", 
    "studio", 
    "summary",
    "review"],
]

TOP_LIST_FILMS = [ //name, release date, seasons, studio, summary, review
  ["None",
  "name",
  "release date",
  "season",
  "studio",
  "summary",
  "review"], 

  ["None",
  "name",
  "release date",
  "season",
  "studio",
  "summary",
  "review"], 
 
  ["None",
  "name",
  "release date",
  "season",
  "studio",
  "summary",
  "review"], 

  ["None",
  "name",
  "release date",
  "season",
  "studio",
  "summary",
  "review"], 

  ["None",
  "name",
  "release date",
  "season",
  "studio",
  "summary",
  "review"], 

  ["None",
  "name",
  "release date",
  "season",
  "studio",
  "summary",
  "review"], 

  ["None",
  "name",
  "release date",
  "season",
  "studio",
  "summary",
  "review"], 

  ["None",
  "name",
  "release date",
  "season",
  "studio",
  "summary",
  "review"], 

  ["None",
  "name",
  "release date",
  "season",
  "studio",
  "summary",
  "review"], 

  ["None",
  "name",
  "release date",
  "season",
  "studio",
  "summary",
  "review"]
]

NOT_IN_USE_TOP_ITEMS_LIST = [
  ["Tomb Raider",
    "",
    "",
    "",
    "",
    ""
  ],
]


//Går fra info til toppliste
function go_back(){
  document.location.href = "top.html";
}

//Hvilken toppliste velger du? Denne kalles fra Index
function choose_media(list_nr){
  localStorage.setItem("media_name", list_nr);
  document.location.href = "top.html";
}

//Loader cookie info om hvilken toppliste du valgte i index
function cookie_load(){
  var nr = 0
  var nr2 = 0
  nr = localStorage.getItem("media_name");
  nr2 = localStorage.getItem("list_nr");
  make_list(nr)
}

//LOAD TOPP LISTE
function topp_list_load(){
  cookie_load()

  //Change banners
  for(i=0; i<10; i++){
    var temp_id = ""
    temp_id = "top_" + (i+1)
    document.getElementById(temp_id).src = "Bilder/" + media_name + "/" + top_list[i][0] + "/" + "banner.png"
    //console.log("Bilder/" + media_name + "/" + top_list[i] + "/" + "banner.jpg")
  }

}

//Save and goto INFO OM OBJECT
function goto_info(number){
  if(top_list[number-1][0] == "None" || info_page == false){
    console.log("None avalibe!")
  }
  else{
    console.log(top_list[number-1][0])
    nr_list = localStorage.setItem("list_nr", number);
    document.location.href = "info.html";
  }
}

//Loader inn info når vi er på info.html
function load_info(){
  var nr = localStorage.getItem("list_nr");
  for(i=0; i<maks_antall_bilder; i++){
    for(ii = 0; ii<file_types.length; ii++){
      var temp = "Bilder/" + media_name + "/" + top_list[nr-1][0] + "/" + (i+1) + file_types[ii]
      images.push(temp)
    }
  }
  checkImage() 
  make_info_text(nr)
}

//Sjekker om bildene in array finnes eller ikke. Sletter de som ikke finnes.
function checkImage() {
  temp_list = []
  for(i=0; i<images.length; i++){
    var http = new XMLHttpRequest();

    http.open('HEAD', images[i], false);
    http.send();

    if(http.status != 404){
      temp_list.push(images[i])
    }
  }
  images = temp_list
  //console.log(images)
}



//Lager tekst i info
function make_info_text(sent){
  if(media_name == "Games"){
    document.getElementById("txt_2").innerHTML = "<b><u> Developer </u></b>"
    document.getElementById("txt_3").innerHTML = "<b><u> Genre </u></b>"
  }
  document.getElementById("title_text").innerHTML = top_list[sent-1][0]
  document.getElementById("airdate_text").innerHTML = top_list[sent-1][1]
  document.getElementById("seasons_text").innerHTML = top_list[sent-1][2]
  document.getElementById("studio_text").innerHTML = top_list[sent-1][3]
  document.getElementById("summary_text").innerHTML = top_list[sent-1][4]
  document.getElementById("review_text").innerHTML = top_list[sent-1][5]

}

//Lager riktig liste
function make_list(list){
  if(list == 1){
    top_list = TOP_LIST_GAMES
    media_name = "Games"
  }
  else if(list == 2){
    top_list = TOP_LIST_SERIES
    media_name = "Series"
  }
  else if(list == 3){
    top_list = TOP_LIST_FILMS
    media_name = "Film"
  }
  console.log(media_name)
}

//NEXT SLIDE IN INFO PAGE
function change_slides_next(){
  if(slider_number < images.length - 1){
    slider_number++
  }else{
    slider_number = 0;
  }
  new_text = slider_number+1 + "/" + images.length
  document.getElementById("counter_text").innerHTML = new_text;

  if((images[slider_number].charAt(images[slider_number].length - 1) == "4")){
    console.log(new_text + " File: Video")
    document.getElementById("video_class").style.visibility = "visible";
    document.getElementById("video_class").src = images[slider_number];
  }else{
    console.log(new_text + " File: Image")
    document.image_name.src = images[slider_number];
    document.getElementById("video_class").style.visibility = "hidden";
    document.getElementById("video_class").pause();
  }


}

//PREVIOUS SLIDE IN INFO PAGE
function change_slides_prev(){

  if(slider_number > 0){
    slider_number--
  }else{
    slider_number = images.length-1;
  }

  new_text = slider_number+1 + "/" + images.length
  document.getElementById("counter_text").innerHTML = new_text;

  if((images[slider_number].charAt(images[slider_number].length - 1) == "4")){
    console.log(new_text + " File: Video")
    document.getElementById("video_class").style.visibility = "visible";
    document.getElementById("video_class").src = images[slider_number];
  }else{
    console.log(new_text + " File: Image")
    document.image_name.src = images[slider_number];
    document.getElementById("video_class").style.visibility = "hidden";
    document.getElementById("video_class").pause();
  } 
}

//LOAD INFO PAGE FOR FIRST TIME
function start_up(){
  cookie_load()
  load_info()
  var slider_number = 0
  new_text = slider_number+1 + "/" + images.length
  document.getElementById("counter_text").innerHTML = new_text;
  if((images[slider_number].charAt(images[slider_number].length - 1) == "4")){
    console.log(new_text + " File: Video")
    document.getElementById("video_class").style.visibility = "visible";
    document.getElementById("video_class").src = images[slider_number];
  }else{
    console.log(new_text + " File: Image")
    document.image_name.src = images[slider_number];
    document.getElementById("video_class").style.visibility = "hidden";
    document.getElementById("video_class").pause();
  } 
}




//OLD CODE. TESTING HOW TO CHECK IF FILES EXIST.
function checkImage_OLD() {
  temp_list = []
  for(i=0; i<images.length; i++){
    checkImage2(images[i])
  }
}

function checkImage2(path){
  let workedimages = images.slice()
  images.forEach(item => {
    let img = new Image()
    img.src = item
    img.onerror = () => workedimages.splice(workedimages.indexOf(item), 1)
    
  })
  images = workedimages
  console.log(images)
}
function img_success(img, path){
  img.onload = temp_list.push(path)
  console.log("Success!")
}

function img_fail(img,path){
  img.onerror = temp_list.splice(path,1)
  console.log("Fail")
}