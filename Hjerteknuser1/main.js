active = false


var counter = 1 //Hvilket bilde som byttes til
var timer = 5000 //Hvor lang intervallen mellom bilene er


//Automatisk bytte bilde i slideren
setInterval(function(){
  if(active==false){return}
  document.getElementById('radio' + counter).checked = true;
  counter++
  if(counter > 4){
    counter = 1
  }
}, timer);