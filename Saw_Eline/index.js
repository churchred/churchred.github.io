

let audio_lenght = 25

function makeSound(name){
  stopPlayers()
  showPlayer(name)
}


function stopPlayers(){
  var temp
  for(i=1; i<audio_lenght+1; i++){
    console.log(i)
    temp = document.getElementById((i.toString()))
    temp.pause()
    temp.style.display = 'none'
  }
}


function showPlayer(name){
  var player = document.getElementById(name)
  //player.style.display = 'block'
  player.currentTime = 0;
  player.play()
}