

// Global variables

array = ['NOK', 'EUR']
main_rate = 0

flags = [
  ['NOK', 'norsk.webp'],
  ['EUR', 'Euro.png'],
  ['USD', 'usa.webp'],
  ['SEK', 'sweeden.webp'],
  ['DKK', 'denmark.webp'],
  ['GBP', 'storbritania.webp']
]

// EUR -> NOK: 11.31
// NOK -> EUR: 0.0884

async function getData(from, to){

  site_url = 'https://api.exchangerate-api.com/v4/latest/' + from

  const response = await fetch(site_url)
  const data = await response.json()
  console.log(data)
  return data.rates[to]
}


// Skaffer valuta rate mellom to valutaer
function getRates(){
  // Henter info fra API om rates

  console.log("Getting rates for: " + array[0] + ' and ' + array[1])


  const promise = getData(array[0], array[1])
  promise.then(function(data){
    console.log("The rate for " + array[0] + ' to ' + array[1] + ': ' + data)
    main_rate = data
    console.log(main_rate)
  })
}

// Funksjonen som kjører når vi gjør om fra en verdi til en annen. Blir kalt fra input.keyup
function convert(from){

  var from_value = ''
  var to_value = ''
  var temp_rate = main_rate

  if(from == 1){
    from_value = 'value1'
    to_value = 'value2'
    console.log("Input value: Box 1")
  }

  if(from == 2){
    from_value = 'value2'
    to_value = 'value1'
    console.log("Input value: Box 2")
  }
  
  var first_value = removeZero(document.getElementById(from_value).value)
  var second_value = removeZero(document.getElementById(to_value).value)

  if(from == 2){temp_rate = (1 / main_rate)}

  second_value = first_value * temp_rate
  second_value = second_value.toFixed(2)

  document.getElementById(to_value).value = parseFloat(second_value)
  
}

// Fjerner 0 fra value hvis null er det første tallet
function removeZero(number){

    for(i=0; i<number.length; i++){
      if(number[0] == '0' && number.length != 1){number = number.substring(1)}
    }

  return number
}

// Oppdaterer hvilken valuta det er snakk om
function updatedropdown(){
  array[0] = document.getElementById('from_input1').value
  array[1] = document.getElementById('from_input2').value

  //console.log(array.fruits.indexOf("Apple"))

  document.getElementById('value1').value = 0
  document.getElementById('value2').value = 0

  switch_flags()

  getRates()
}


function switch_flags(){

  for(i=0; i<flags.length; i++){
    if(array[0] == flags[i][0]){
      document.getElementById('flag1').src = 'assets/Flags/' + flags[i][1]
    }
  }

  for(i=0; i<flags.length; i++){
    if(array[1] == flags[i][0]){
      document.getElementById('flag2').src = 'assets/Flags/' + flags[i][1]
    }
  }

}

getRates()

