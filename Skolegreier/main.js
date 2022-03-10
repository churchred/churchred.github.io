//If you're looking at this you are cheating! Men igjen, hvis du ser på dette så fortjener du å finne passordet xD

var see_pass = false //om vi kan se passordet i input boksen eller ikke
var logged_in = false //Har du logget inn?

var password_needed = false //Skru av og på passord

var minutes_until_logout = 1 * 60 * 24 * 7 * 2 //Hvor lenge du er logget på før du blir logget ut (i minutter, derfor ganger jeg)
//minutes_until_logout = 10

let code = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

let username = [4, 12, 8, 11, 8, 4]
let password = [15, 0, 18, 18]

function maker(list){ //Noe jeg lagde kun for gøy... hjelper egentlig ikke xD
  var new_text = ''
  for(i=0; i<list.length; i++){
    new_text += code[list[i]]
  }
  return new_text
}

username = maker(username)
password = maker(password)

function make_pass_vis(){ //Gjør passord tekten i input boksen synlig eller usynlig
  var pass = document.getElementById('password_input')

  if(see_pass == false){
    see_pass = true;
    document.getElementById('see_btn').src = 'Bilder/eye.png'
    pass.type = "text"
  }
  else if(see_pass == true){
    see_pass = false;
    document.getElementById('see_btn').src = 'Bilder/eye_closed.png'
    pass.type = "password"
  }
  console.log("Password Visibility:", see_pass)
}


function check_pass(){ //Sjekker om brukernavn og passord stemmer
  var user_pass = document.getElementById("password_input").value;
  var user_name = document.getElementById("username_input").value;

  console.log("--------------------")
  console.log("Username:", user_name)
  console.log("Password:", user_pass)

  if(user_name == username && user_pass == password){
    document.getElementById("password_input").value = ''
    document.getElementById("username_input").value = ''

    localStorage.setItem('logged_in', true)
    const d = new Date();
    let time = d.getTime();
    time = get_time()
    console.log("----> Correct")
    console.log("Login time:", time)
    localStorage.setItem('logged_in_time', time)



    document.location.href = 'index.html';

  }else{console.log("----> WRONG")}
}

function get_time(){
  const d = new Date();
  let time = d.getTime(); //Millisekunder
  time = time/1000  //Sekunder
  time = time/60    //Minutter
  /*time = time/60  //Timer
  time = time/24    //Dager
  time = time/7*/   //Uker
  time = Math.floor(time)
  return time 
}

function check_if_log_out(){
  curr_time = get_time()
  old_time = localStorage.getItem("logged_in_time")
  console.log(minutes_until_logout - (curr_time - old_time))
  if(curr_time - old_time >= minutes_until_logout){
    localStorage.setItem('logged_in', false)
    document.location.href = '../../password.html';
  }
}


function load(){
  if(password_needed == true){
    console.log("Password:[ON]")
    logged_in = localStorage.getItem("logged_in")
    console.log("Logged in:", logged_in)


    if(logged_in == null){
      logged_in = false
    }

    if(logged_in == false){
      document.location.href = 'password.html';
    }

    check_if_log_out()
  }else{console.log("Password:[OFF]")}
}