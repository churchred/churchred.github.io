//Laget av Kristoffer

var start_value = 0; //Start verdien
var end_value = 100; //Slutt verdien

var display_value = 0; //Verdien som vises midt på skjermen
var counter_value = 1; //Hvor mye vi teller med når vi teller

var counting_speed = 10; //Hvor fort den skal telle

var count_dir = "UP" //Hvilken vei teller vi?

var des_nr = 0 //Hvor mange tall bak komma skal vises?

var symbol = "" //Skal det stå noe etter tallet?

var btn_value = 'start' //start, stopp eller resett
var stopp = false

//Sjekker om veridene vi får er brukbare
function check_values(){
  start_value = parseFloat(document.getElementById('start_value').value)
  end_value = parseFloat(document.getElementById('end_value').value)

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

  let array = [check_decimal(counter_value), check_decimal(start_value), check_decimal(end_value)]
  array.sort()
  array.reverse()
  des_nr = array[0]

  display_value = start_value
  document.getElementById('counter').innerText = (make_space(display_value.toFixed(des_nr)) + symbol)

  console.log("----------------")
  console.log("Start:", start_value)
  console.log("End:", end_value)
  console.log("Speed:", counting_speed)
  console.log("Count by:", counter_value)
  console.log("Counting:", count_dir)
  console.log(array)
}

//Button press
function btn_press(){
  if(btn_value == 'start'){
    stopp = false
    document.getElementById('start_btn').innerText = 'STOPP'
    btn_value = 'stopp'
    dis_enable(true)
    counter()
  }
  else if(btn_value == 'resett'){
    display_value = start_value
    document.getElementById('counter').innerHTML = (display_value.toFixed(des_nr) + symbol)
    btn_value = 'start'
    document.getElementById('start_btn').innerText = 'START'
    dis_enable(false)
  }
  else if(btn_value == 'stopp'){
    stopp = true
    document.getElementById('start_btn').innerText = 'RESETT'
    btn_value = 'resett'
  }
}

//Teller opp
function counter(){
  if(stopp == true){
    return
  }
  if(count_dir == "UP"){
    display_value += counter_value
    if(display_value > end_value){display_value = end_value}
    
    document.getElementById('counter').innerHTML = (make_space(display_value.toFixed(des_nr)) + symbol)
    if(display_value < end_value){
      setTimeout(() => {counter()}, counting_speed)
    }
    if(display_value >= end_value){
      display_value = 0;
      btn_value = 'resett'
      document.getElementById('start_btn').innerText = 'RESETT'
    }
  }

  if(count_dir == "DOWN"){
    display_value -= counter_value
    if(display_value < end_value){display_value = end_value}
    document.getElementById('counter').innerHTML = (make_space(display_value.toFixed(des_nr)) + symbol)
    if(display_value > end_value){
      setTimeout(() => {counter()}, counting_speed)
    }
    if(display_value <= end_value){
      display_value = end_value;
      btn_value = 'resett'
      document.getElementById('start_btn').innerText = 'RESETT'
    }
  }

}

//sjekker hvor mange plasser bak komma
function check_decimal(num){
  var text = num.toString();
  var index = text.indexOf(".");
  return index == -1 ? 0 : (text.length - index - 1);
}

//Skrur av og på settings input boksene
function dis_enable(value){
  document.getElementById('start_value').disabled = value
  document.getElementById('end_value').disabled = value
  document.getElementById('speed').disabled = value
  document.getElementById('count_by').disabled = value
  document.getElementById('symbol').disabled = value
}

//Lager punktum eller mellomrom i store tall
function make_space(x){
  var parts = x.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, " ");
  return parts.join(".");
}


//Sjekker om keyboard blir trykket på
addEventListener('keyup', ({event}) =>{
  if(btn_value == 'start'){check_values()}
})