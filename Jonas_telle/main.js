//Laget av Kristoffer

var start_value = 0; //Start verdien
var end_value = 100; //Slutt verdien

var display_value = 0; //Verdien som vises midt på skjermen
var counter_value = 1; //Hvor mye vi teller med når vi teller

var counting_speed = 10; //Hvor fort den skal telle

var count_dir = "UP" //Hvilken vei teller vi?

var des_nr = 0 //Hvor mange tall bak komma skal vises?

var symbol = "" //Skal det stå noe etter tallet?

var done = false

//Sjekker om veridene vi får er brukbare
function check_values(){
  done = true
  start_value = parseInt(document.getElementById('start_value').value)
  end_value = parseInt(document.getElementById('end_value').value)
  counting_speed = parseInt(document.getElementById('speed').value)
  counter_value = parseFloat(document.getElementById('count_by').value)
  symbol = document.getElementById('symbol').value

  if(Number.isNaN(start_value) == true){
    start_value = 0
  }

  if(Number.isNaN(end_value) == true){
    end_value = 100
  }

  if(Number.isNaN(counting_speed) == true){
    counting_speed = 10
  }

  if(Number.isNaN(counter_value) == true){
    counter_value = 1
  }

  if(start_value>end_value){
    count_dir = "DOWN"
  }
  if(start_value<end_value){
    count_dir = "UP"
  }

  des_nr = check_decimal(counter_value)
  display_value = start_value
  document.getElementById('counter').innerText = (display_value.toFixed(des_nr) + symbol)

  console.log("----------------")
  console.log("Start:", start_value)
  console.log("End:", end_value)
  console.log("Speed:", counting_speed)
  console.log("Count by:", counter_value)
  console.log("Counting:", count_dir)
}


//Teller opp
function counter(){
  if(done == true){
    resett()
    return
  }
  if(count_dir == "UP"){
    display_value += counter_value
    if(display_value > end_value){display_value = end_value}
    document.getElementById('counter').innerHTML = (display_value.toFixed(des_nr) + symbol)
    if(display_value < end_value){
      setTimeout(() => {counter()}, counting_speed)
    }
    if(display_value >= end_value){
      display_value = 0;
      done = true
    }
  }

  if(count_dir == "DOWN"){
    display_value -= counter_value
    if(display_value < end_value){display_value = end_value}
    document.getElementById('counter').innerHTML = (display_value.toFixed(des_nr) + symbol)
    if(display_value > end_value){
      setTimeout(() => {counter()}, counting_speed)
    }
    if(display_value <= end_value){
      display_value = end_value;
      done = true
    }
  }

}


function resett(){
  done = false
  display_value = start_value
}

//sjekker hvor mange plasser bak komma
function check_decimal(num){
  var text = num.toString();
  var index = text.indexOf(".");
  return index == -1 ? 0 : (text.length - index - 1);
}


//Sjekker om keyboard blir trykket på
addEventListener('keyup', ({event}) =>{
  check_values()
})