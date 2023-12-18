

//  Funksjon som styrer meny knappen som kommer opp når menyenpå banner sjules på liten skjerm.
function click_btn(){
  const nav_bar = document.getElementsByClassName('banner-body')[0]
  nav_bar.classList.toggle('active')
  console.log("CLICKED")
}


//  Liste hvor topplisten din blir laget fra. 
//  Denne listen får alt innholdet sitt fra
//  lagrings-data.
//  [i][0] = Id nummer(id_number_x), [i][1] = bildet/banner filnavn
//
let Main_list = []


//  Denne listen er VIKTIG
//  Skal du legge til nye sider for nye lister
//  er det er du gjør det!
//  Den nye siden på ha onload(Load(X)), Hvor X
//  er posisjonen i denne listen. Første er 0 etc.
//  0=Page Title, 1=img path, 2=navn på save list, 3=navn på length save list
//
let img_path = [
  ['Games', 'assets/Games/', 'game_list', 'game_length'], 
  ['Tv-series', 'assets/Series/', 'tv_list', 'tv_length'],
  ['Movies', 'assets/Movies/', 'movie_list', 'movie_length'],
  ['Books', 'assets/Books/', 'book_list', 'book_length'],
  ['Survival Games', 'assets/Games/', 'survival_list', 'survival_length'],
  ['Unusual Games', 'assets/Games/', 'unusual_list', 'unusual_length'],
  ['Puzzle Games', 'assets/Games/', 'puzzle_list', 'puzzle_length'],
  ['Best of Leverage', 'assets/LeverageEpisodes/', 'leverage_list', 'leverage_length'],
  ['Logic Games', 'assets/Games/', 'logic_list', 'logic_length'],
  ['Coop Games', 'assets/Games/', 'coop_list', 'coop_length']
]


//  Denne holder styr på hvor lang en liste er. 
list_length = Main_list.length


//  Er Edit-mode av eller på?
var edit = false

//  Hvilken topp-liste ser vi på nå? Altså hvor er vi?
var curr_loc = ''

//  Hvor mange ganger har trykker på reset-knappen.
var reset_click = 0




//  Laster inn og lager en Div til alle elementene i topplista di. 
//  Bygger altså topplista basert på array. Topplisten som bygges 
//  er baser på hvilke save-data du henter. Hver liste har sin egen 
//  save-data.
//
function LoadList(){
  
  for(i=0; i<Main_list.length; i++){

    console.log(i+1 + ":  " + Main_list[i][1])  //  Printer ut navn på item som blir laget

    // Lager Hoved div som alt info skal inn i etterpå
    var new_div = document.createElement('div');
    new_div.className = 'item';
    new_div.id = 'id_number_' + i
    Main_list[i][0] = ('id_number_' + i)
    document.getElementById('top_list').appendChild(new_div);
    
    //Lager input felt. Dette er feltet hvor plass-nummer står.
    var new_div_h1 = document.createElement('input');
    new_div_h1.id = 'input_id' + i
    new_div_h1.type = 'number'
    new_div_h1.className = 'item_number'
    new_div_h1.value = i+1 
    document.getElementById(new_div.id).appendChild(new_div_h1)


    //Lager Knappen til input-nummer-feletet.
    var enter_btn = document.createElement('button');
    enter_btn.id = 'enter_btn' + i
    enter_btn.className = 'enter_btn'
    enter_btn.innerHTML = 'Move';
    document.getElementById(new_div.id).appendChild(enter_btn)


    //Lager bildet som skal vises på banner
    var new_div_img = document.createElement("img");
    new_div_img.src = img_path[curr_loc][1] + Main_list[i][1]
    document.getElementById(new_div.id).appendChild(new_div_img);  

    //Lager Button div som edit-knappene skal inn  i.
    var new_div_button_div = document.createElement('div');
    new_div_button_div.className = 'button_div';
    document.getElementById(new_div.id).appendChild(new_div_button_div);

    //Lager Knapper til Button div
    var new_div_button_1 = document.createElement('button');
    new_div_button_1.id = 'btn' + i
    new_div_button_1.className = 'up_btn'
    new_div_button_1.innerHTML = '&#x2191;'; //  HTML kode som blir til en "Up arrow"
    new_div_button_div.appendChild(new_div_button_1);

    var new_div_button_2 = document.createElement('button');
    new_div_button_2.id = 'btn' + i
    new_div_button_2.className = 'down_btn'
    new_div_button_2.innerHTML = '&#8595;'; //  HTML kode som blir til en "Up arrow"
    new_div_button_div.appendChild(new_div_button_2);

    var new_div_button_3 = document.createElement('button');
    new_div_button_3.id = 'btn' + i
    new_div_button_3.className = 'del_btn'
    new_div_button_3.innerHTML = 'x';  //  x er det som vises i delte knappen.
    new_div_button_div.appendChild(new_div_button_3);
    
  }


  //  Dette fikser problemet med at verticale bilder blir registrert som horizontale
  //  Henter ut alle bilder inne i topplisten.
  var pics = document.getElementById('top_list_div').querySelectorAll("img");
  var pic;

  
  //  Går igjennom hvert bilde og ser om det er lastet inn eller ikke.
  //  Er det ikke loaded så lager det en eventlistener som sjekker
  //  når den blir loaded. Bilder som er loaded blir så sjekket
  //  om de er horizontald eller vertikald og får deretter
  //  rikitg css class tag basert på svaret.
  //
  for (i = 0; i < pics.length; i++) {
    pic = pics[i];
    if (pic.complete) {
      // The image is already loaded, call handler
      checkImage(pic);
    } else {
      // The image is not loaded yet, set load event handler
      pic.addEventListener("load", function() {
        checkImage(this);
      })
    }
  }
  


  //  Her lager vi en eventlistener som sjekker hva du trykker
  //  på innenfor topplisten. Deretter sjekker den hva som ble
  //  trykket på av knapper.
  //
  const menu = document.getElementById("top_list");

  menu.addEventListener('click', function(e) {
    const tgt = e.target
    const tgt_nr = myGeeks(tgt.id)

    if (tgt.classList.contains('up_btn')) Switch(tgt_nr, -1);
    if (tgt.classList.contains('down_btn')) Switch(tgt_nr, 1);
    if (tgt.classList.contains('del_btn')) Delete(tgt_nr);
    if (tgt.classList.contains('enter_btn')) Move(tgt_nr);
  })
}



//  Denne funksjonen får tilsendt en string med bokstaver
//  og tall. Den sender tilbake kun  tallene fra  stringen.
//
function myGeeks(str) {
 
  // Using match with regEx
  let matches = str.match(/(\d+)/);
   
  // Display output if number extracted
  if (matches) {
    console.log(matches[0]);
    return matches[0]
}
}


//  Sjekker om et bilde sin bredde er større enn sin høyde.
//  Altså er bildet vertikalt eller horizontalt?
//  Bildet får deretter et class navn basert på svaret.
//
function checkImage(img) {
  if (img.naturalHeight > img.naturalWidth) {
    img.classList.add("vertical_img")
  } else {
    img.classList.add("horizontal_img")
  }
}

//  Bytter plass på to elementer i en array.
//  Brukes når noe skal flyttes opp eller ned 
//  i topp-lista.
//
function Switch(nr, dir){

  nr = parseInt(nr)     //  Id på bildet som skal flyttes. Id matcher Array index.
  dir = parseInt(dir)   //  Denner er enten 1 eller -1. Skal den opp i lista eller ned?

  console.log(Main_list[nr][1] + '   flyttes fra index   ' + nr + ' --> ' + (nr+dir))

  var old_index = nr;
  var new_index = (nr + dir)


 
  if(new_index >= Main_list.length || new_index < 0){   //  Sjekker hvor den blir sendt, slik at du IKKE kan flytte første
    console.log("Kan ikke flyttes lenger opp/ned")      //  elementet opp og siste elementet ned.
    return
  }

  //  Bytter plass på 2 elementer i en liste.
  const temp = Main_list[old_index];            //  Lagrer verdi en i et nytt variabe, temp.
  Main_list[old_index] = Main_list[new_index];  //  Verdi 1 blir overskrevet av Verdi 2.
  Main_list[new_index] = temp;                  //  Verdi 2 blir overskrevet av temp. 
 

  // Sletter toppliste div
  const menu = document.getElementById("top_list");
  menu.remove();

  // Lager en ny om tom toppliste div.
  var new_main_div = document.createElement('div');
  new_main_div.className = 'top_list'
  new_main_div.id = 'top_list'
  document.getElementById('top_list_div').appendChild(new_main_div);

  // Lagrer ny array/lista lokalt
  Save()

  // Bygger ut toppliste på nytt basert på ny liste
  LoadList()

}

// Lagrer Data
function Save(){

  //  Lagrer basert på hvilken liste vi er inne 
  //  og ser på. Img_path array inneholder
  //  alle navn på det som brukes her.
  //  Dette gjør det enklere å lage nye save-lister
  //  fordi jeg ikke trenger å gjøre noe annet enn
  //  å legge til ny rad i img_path array.
  //
  localStorage.setItem(img_path[curr_loc][2], Main_list)
  list_length = Main_list.length
  localStorage.setItem(img_path[curr_loc][3], list_length)


  localStorage.setItem('edit', edit)
}

// laster lagringsdata in på Main_list
function Load(){

  var hash = window.location.hash;  //  Leser hashtag veriden på url.
  hash = hash.replace('#','');      //  Finner tallet bak hashtagen.

  curr_loc = hash[0]
  let temp_list = []
  var temp_len = 0

  console.log("Du ser på denne lista:  " + img_path[curr_loc][0])


  // Henter inn lagringsdata basert på hvilken liste vi skal se på
  temp_list = localStorage.getItem(img_path[curr_loc][2])
  temp_len = parseInt(localStorage.getItem(img_path[curr_loc][3]))

  //Lager Tittel på siden.
  document.getElementById('header').textContent = img_path[curr_loc][0]


  // console.log("List: " + temp_list)
  // console.log("Number of items: " + temp_len)

  //Denne kjøres hvis save-data for listen ikke finnes ennå. 
  if(temp_list == null){ 
    LoadList()  // Prøve å bygge siden
    Save()      // Og lagre data etterpå
  }

  else{
    temp_list = temp_list.split(",")  // Lager en liste basert på hvor komma er i lagringsdata
    var count = 0 
    let new_list = [] // Ny liste som vi skal bruke

    // Tar lagringsdata og bygger en liste som kan legges inn i Main_list. En rad om gangen.
    for(i=0; i<temp_len; i++){
      let new_row = [] 
      for(ii=0; ii<2; ii++){
        new_row.push(temp_list[count])
        count += 1
      }
      new_list.push(new_row)
    }

    Main_list = new_list.slice(0) // Oppdaterer main liste til å bli lik som den vi akkurat lagde.

    //  Sjekker om Edit-mode er på eller av.
    edit = localStorage.getItem('edit')
    if(edit == 'false'){edit = false}
    if(edit == 'true'){edit = true}

    console.log(Main_list)

    LoadList()
    EnableEditChange()
  }


}

// Resetter alt
function Reset(){
  if(reset_click == 0){document.getElementById('reset_btn').textContent = 'Are you sure?'}
  if(reset_click == 1){document.getElementById('reset_btn').textContent = 'Really?'}
  if(reset_click == 2){document.getElementById('reset_btn').textContent = 'Ok then, RESET'}
  if(reset_click == 3){
    localStorage.clear()
    location.reload()
  }
  reset_click += 1
}

// Viser eller gjemmer Add-new-game vinduet
function ShowHideAddScreen(x){
   var temp_file = document.getElementById('addnew')
   if(x == 0){ //Close
    temp_file.style.visibility = 'hidden'
   }

   if(x == 1){ // Open
    temp_file.style.visibility = 'visible'
   }
}

// Logikken for å legge til nytt spill
function AddNewGame(){
  // Initialize an empty array
  const inputArray = [];
  
  // Get the input elements
  const input1 = document.getElementById("input1");
  const input2 = document.getElementById("input2");

  // Get the values of the input elements
  var value1 = input1.value; // Hvor på topplista den skal ligge. Hvilken plass. Et tall.
  const value2 = input2.value; // Navnet på bilde-filen.
  var value3 = []
  
  if(value1 == ""){value1 = Main_list.length+1} //  Legges in bunn av lista hvis ikke noe annet blir spesifisert.
  if(value1 > Main_list.length){value1 = Main_list.length} // Kan ikke legges lenger ned enn lista er lang.
  else{value1 = value1-1}  // Gjør om plass i liste til index i Main_list

  value3 = value2.split("\\")  // Henter kun ut filnavnet fra bilde-fil-path
  var img_path = value3[(value3.length-1)]

  // Add the values to the array
  inputArray.push(('id_number_' + Main_list.length), img_path)
  
  // Send info to main array
  Main_list.splice(value1, 0, inputArray);

  // Close New-Game window again
  ShowHideAddScreen(0)

  Save()  // Lagre Main_list

  //Vent litt og reload hele siden slik at den kan bygges opp på nytt.
  setTimeout(function(){
    window.location.reload();
  });
}

// Skru på Edit-mode
function EnableEdit(){
  if(edit == false){edit = true}
  else if(edit == true){edit = false}
  Save()
  EnableEditChange()
  console.log("Edit mode: " + edit)
}

// Edit mode
function EnableEditChange(){

  // Dette skjer hvis Edit-mode IKKE er på.
  //
  if(edit == false){
    var divsToHide = document.getElementsByClassName("button_div");
    var divsToHide2 = document.getElementsByClassName("enter_btn");
    document.getElementById('add_item_btn').style.visibility = 'hidden'
    document.getElementById('edit_btn').style.backgroundColor = 'transparent'
    for(var i = 0; i < divsToHide.length; i++){
        divsToHide[i].style.visibility = "hidden"; 
    }

    for(var i = 0; i < divsToHide2.length; i++){
      divsToHide2[i].style.visibility = "hidden"; 
      divsToHide2[i].style.position = "absolute"; 
    }

    for(i=0; i<Main_list.length; i++){
      var temp_info = 'input_id' + i
      document.getElementById(temp_info).disabled = true;
      document.getElementById(temp_info).style.color = 'white';
      document.getElementById(temp_info).style.backgroundColor = 'black';
      document.getElementById(temp_info).style.border = 'none';
    }
  }

  // Dette skjer hvis Edit-mode ER på.
  //
  else if(edit == true){
    var divsToHide = document.getElementsByClassName("button_div");
    var divsToHide2 = document.getElementsByClassName("enter_btn");
    document.getElementById('add_item_btn').style.visibility = 'visible'
    document.getElementById('edit_btn').style.backgroundColor = '#e46a70'
    for(var i = 0; i < divsToHide.length; i++){
        divsToHide[i].style.visibility = "visible"; 
    }

    for(var i = 0; i < divsToHide2.length; i++){
      divsToHide2[i].style.visibility = "visible"; 
      divsToHide2[i].style.position = "relative"; 
    }

    for(var i = 0; i < divsToHide.length; i++){
      divsToHide[i].style.visibility = "visible"; 
  }

    for(i=0; i<Main_list.length; i++){
      var temp_info = 'input_id' + i
      document.getElementById(temp_info).disabled = false;
      document.getElementById(temp_info).style.color = 'yellow';
      document.getElementById(temp_info).style.backgroundColor = '#5A5A5A';
      document.getElementById(temp_info).style.border = 'solid 2px black';
    }
  }

}


//  Sletting av et element i lista.
function Delete(x){
  console.log("DELETE", x)
  console.log(Main_list[x][1])
  Main_list.splice(x, 1);
  Save()
  location.reload()
}

//  Reload current url/page.
function reload(){
  location.reload()
}

//  Funskjonen som blir kalt når et element skal
//  flyttes på i lista til en nytt sted.
//  Denne finner all info som trengs og sender
//  det videre til neste funksjon som faktisk
//  hånterer byttet.
//
function Move(target){
  console.log("Trying to move: " + Main_list[target][1])
  var old_value = target;
  var new_value = document.getElementById('input_id' + target).value


  if(Number.isInteger(new_value) == false){
    console.log("Not valid input: " + new_value)
    document.getElementById('input_id' + target).value = (old_value+1)[1]
  }

  new_value -= 1
  
  if(Number.isInteger(new_value) == true){
    if(new_value >= Main_list.length){
      console.log("New value is too big")
      new_value = Main_list.length-1
    }
    if(new_value < 0){
      console.log("New value is too small")
      new_value = 0
    }
    if(old_value != new_value){
      console.log("From: " + old_value + " --> " + new_value)
      moveItem(old_value, new_value);
    }
  }
}

//  Denne funksjonen sender et item i en liste fra 
//  en plass/index til en annen uten å fjerne noe annet.
//
function moveItem(from, to) {
  // remove `from` item and store it
  var f = Main_list.splice(from, 1)[0];
  // insert stored item into position `to`
  Main_list.splice(to, 0, f);
  Save()
  location.reload()
}


//  Knappene nederst i høyre hjørne som sender oss helt opp 
//  til toppen av siden eller helt ned til bunn.
//
function MoveUpDown(dir){
  if(dir == 'up'){document.documentElement.scrollTop = 0;}
  if(dir == 'down'){window.scrollTo(0, document.body.scrollHeight);}
}