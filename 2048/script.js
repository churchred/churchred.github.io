

//Banen vi spiller på  -  [ID, Value]
let gameBoard = [
  [[0,0], [0,0], [0,0], [0,0]],
  [[0,0], [0,0], [0,0], [0,0]],
  [[0,0], [0,0], [0,0], [0,0]],
  [[0,0], [0,0], [0,0], [0,0]]
]

// Number of Rows
var number_of_rows = 4
var number_of_collums = 4

// Variablene som holder styr på om knappene er trykket på eller ikke
const keys = {
  right: {
    pressed: false
  },
  left: {
    pressed: false
  },
  up: {
    pressed: false
  },
  down: {
    pressed: false
  }
}

//Har du trykket på knapp? Blir true i keydown og false i keyup
var clicked = false

//Holder styr på ID til alle tiles som blir laget.
var id_var = 0

//Har banen forandret seg siden du trykket sist?
var change = false

//Holder styr på poeng
var score = 0
var best_score = 0

// Har vi tapt?
var lost = false


// Sjanse for at det lages en brikke med tallet 4 istedet for 2
// funskjonen tar et tall mellom 0 og dette variablet. Blir tallet 0 så lages en Tile med 4 istedet for 2.
var number_four_chance = 10

let Tile_values = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]

// Blir kjørt når siden starter opp 
function startGame() {
  createChip()
  createChip()
  consoleView()
}


// Logikken for å lage nye brikker
// Velger et random sted inne i lista også jobber seg bortover/nedover 
// til den har funnet en ledig plass. Deretter setter den en tile der.
function createChip(){

  var rand_row = Math.floor(Math.random() * number_of_rows)    // Lager tall fra 0-3
  var rand_collum = Math.floor(Math.random() * number_of_rows) // Lager tall fra 0-3 
  var maxIndx = number_of_rows
  var row = 0
  var collum = 0
  var done = false

  for(i=0; i<maxIndx + 1; i++){
    if(i+rand_row >= maxIndx){
      row = i + rand_row-maxIndx
    }
    else{
        row = i+rand_row
    }

    for(ii=0; ii<maxIndx; ii++){
      if(i > maxIndx-1 && ii > rand_collum-1){
        break
      }
      else if(i > 0){
        collum = ii
      }
      else if(ii+rand_collum >= maxIndx){
        break
      }
      else{
          collum = ii + rand_collum
      }
      //Her lages tingen
      if(gameBoard[row][collum][0] == 0 && done == false){

        var new_tile = document.createElement('p');
        var temp_id = "id" + id_var;
        new_tile.id = temp_id

        new_tile.className = ""
        var new_class = "t2" 
        new_tile.classList.add('tile', new_class, "new");   // add multiple classes

        var rand_number = Math.floor(Math.random() * number_four_chance)
        var new_value = 2
        if(rand_number == 0){new_value = 4}
        new_tile.textContent = new_value

        new_tile.style.setProperty('--y', row);
        new_tile.style.setProperty('--x', collum);
        document.getElementById('gameboard').appendChild(new_tile);
        gameBoard[row][collum][0] = temp_id
        gameBoard[row][collum][1] = new_value

        id_var += 1
        done = true
        console.log("New Tile being made at: [", row, ",", collum, "]")
      }
    }
  }


}

// Logikk for bevegelse mot høyre
function moveRight(){

  //Beveger alt så langt bort vi kan
  for(var j=0; j<6; j++){
    if(j != 3){
      for(var i=0; i<number_of_rows; i++){
        for(var ii=0; ii<number_of_rows; ii++){
          if(gameBoard[i][ii][0] != 0 && ii != number_of_rows-1){
            if(gameBoard[i][ii+1][0] == 0){
              var tile = document.getElementById(gameBoard[i][ii][0])
              tile.style.setProperty('--x', ii+1);
              gameBoard[i][ii+1] = gameBoard[i][ii]
              gameBoard[i][ii] = [0, 0]
              change = true
            }
          }
        }
      }
    }

    //Sjekker om vi må legge sammen 2 like tall
    if(j == 3){
      for(var i=0; i<number_of_rows; i++){
        for(var ii=number_of_rows-1; ii>-1; ii--){
          if(ii != 0 && gameBoard[i][ii][0] != 0){
            if(gameBoard[i][ii][1] == gameBoard[i][ii-1][1]){
              
              var tile1 = document.getElementById(gameBoard[i][ii-1][0])
              var tile2 = document.getElementById(gameBoard[i][ii][0])
              
              tile1.style.setProperty('--x', ii)
              tile2.remove()
              tile1.textContent = (gameBoard[i][ii][1] * 2)

              gameBoard[i][ii] = gameBoard[i][ii-1]
              gameBoard[i][ii][1] = gameBoard[i][ii][1]*2
              scoreLogic(gameBoard[i][ii][1])
              gameBoard[i][ii-1] = [0, 0]

              tile1.className = ""
              var new_class = "t" +  gameBoard[i][ii][1] 
              tile1.classList.add('tile', new_class);

              change = true
             
            }
          }
        }
      }
    }
  }

}

// Logikk for bevegelse mot venstre
function moveLeft(){
  //Beveger alt så langt bort vi kan
  for(var j=0; j<6; j++){
    if(j != 3){
      for(var i=0; i<number_of_rows; i++){
        for(var ii=number_of_rows-1; ii>-1; ii--){
          if(gameBoard[i][ii][0] != 0 && ii != 0){
            if(gameBoard[i][ii-1][0] == 0){
              var tile = document.getElementById(gameBoard[i][ii][0])
              tile.style.setProperty('--x', ii-1);
              gameBoard[i][ii-1] = gameBoard[i][ii]
              gameBoard[i][ii] = [0, 0]
              change = true
            }
          }
        }
      }
    }

    //Sjekker om vi må legge sammen 2 like tall
    if(j == 3){
      for(var i=0; i<number_of_rows; i++){
        for(var ii=0; ii<number_of_rows; ii++){
          if(ii != number_of_rows-1 && gameBoard[i][ii][0] != 0){
            if(gameBoard[i][ii][1] == gameBoard[i][ii+1][1]){
              
              var tile1 = document.getElementById(gameBoard[i][ii+1][0])
              var tile2 = document.getElementById(gameBoard[i][ii][0])
              
              tile1.style.setProperty('--x', ii)
              tile2.remove()
              tile1.textContent = (gameBoard[i][ii][1] * 2)

              gameBoard[i][ii] = gameBoard[i][ii+1]
              gameBoard[i][ii][1] = gameBoard[i][ii][1]*2
              scoreLogic(gameBoard[i][ii][1])
              gameBoard[i][ii+1] = [0, 0]

              tile1.className = ""
              var new_class = "t" +  gameBoard[i][ii][1] 
              tile1.classList.add('tile', new_class);
             
              change = true
            }
          }
        }
      }
    }
  }
}

// Logikk for bevegelse mot opp
function moveUp(){
  for(var j=0; j<6; j++){
    if(j != 3){
      for(var i=number_of_rows-1; i>-1; i--){
        for(var ii=0; ii<number_of_rows; ii++){
          if(i != 0 && gameBoard[i][ii][0] != 0){
            if(gameBoard[i-1][ii][1] == 0){
              var tile = document.getElementById(gameBoard[i][ii][0])
              tile.style.setProperty('--y', i-1);
              gameBoard[i-1][ii] = gameBoard[i][ii]
              gameBoard[i][ii] = [0,0]
              change = true
            }
          }
        }
      }
    }
    
    
    //Sjekker om vi må legge sammen 2 like tall
    if(j == 3){
      for(var i=0; i<4; i++){
        for(var ii=0; ii<number_of_rows; ii++){
          if(i != number_of_rows-1 && gameBoard[i][ii][0] != 0){
            if(gameBoard[i][ii][1] == gameBoard[i+1][ii][1]){
              var tile1 = document.getElementById(gameBoard[i][ii][0])
              var tile2 = document.getElementById(gameBoard[i+1][ii][0])
              
              tile2.style.setProperty('--y', i)
              tile1.remove()
              tile2.textContent = (gameBoard[i][ii][1] * 2)


              gameBoard[i][ii] = gameBoard[i+1][ii]
              gameBoard[i][ii][1] = gameBoard[i][ii][1]*2
              scoreLogic(gameBoard[i][ii][1])
              gameBoard[i+1][ii] = [0, 0]

              tile2.className = ""
              var new_class = "t" +  gameBoard[i][ii][1] 
              tile2.classList.add('tile', new_class);
              change = true
            }
          }
        }
      }
    }
  }
}

// Logikk for bevegelse mot ned
function moveDown(){
  for(var j=0; j<6; j++){
    if(j != 3){
      for(var i=0; i<number_of_rows; i++){
        for(var ii=0; ii<number_of_rows; ii++){
          if(i != number_of_rows-1 && gameBoard[i][ii][0] != 0){
            if(gameBoard[i+1][ii][1] == 0){
              var tile = document.getElementById(gameBoard[i][ii][0])
              tile.style.setProperty('--y', i+1);
              gameBoard[i+1][ii] = gameBoard[i][ii]
              gameBoard[i][ii] = [0,0]
              change = true
            }
          }
        }
      }
    }
    
    
    //Sjekker om vi må legge sammen 2 like tall
    if(j == 3){
      for(var i=number_of_rows-1; i>-1; i--){
        for(var ii=0; ii<number_of_rows; ii++){
          if(i != 0 && gameBoard[i][ii][0] != 0){
            if(gameBoard[i][ii][1] == gameBoard[i-1][ii][1]){
              var tile1 = document.getElementById(gameBoard[i][ii][0])
              var tile2 = document.getElementById(gameBoard[i-1][ii][0])
              
              tile2.style.setProperty('--y', i)
              tile1.remove()
              tile2.textContent = (gameBoard[i][ii][1] * 2)

              gameBoard[i][ii] = gameBoard[i-1][ii]
              gameBoard[i][ii][1] = gameBoard[i][ii][1]*2
              scoreLogic(gameBoard[i][ii][1])
              gameBoard[i-1][ii] = [0, 0]

              tile2.className = ""
              var new_class = "t" +  gameBoard[i][ii][1] 
              tile2.classList.add('tile', new_class);
              change = true
            }
          }
        }
      }
    }
  }
}


// Printer banen i konsollen
function consoleView() {
  console.log("----------------------------------------------------")
  console.log("Game:")
  console.log(gameBoard[0][0][1], gameBoard[0][1][1], gameBoard[0][2][1], gameBoard[0][3][1])
  console.log(gameBoard[1][0][1], gameBoard[1][1][1], gameBoard[1][2][1], gameBoard[1][3][1])
  console.log(gameBoard[2][0][1], gameBoard[2][1][1], gameBoard[2][2][1], gameBoard[2][3][1])
  console.log(gameBoard[3][0][1], gameBoard[3][1][1], gameBoard[3][2][1], gameBoard[3][3][1])
}

//Bygger banen første gang du launcher den
function buildBoard(){

  //Lager nye elementer og dytter inn på html
  for(var i=0; i<4; i++){
    for(var ii=0; ii<4; ii++){
      if(gameBoard[i][ii][1] != 0){
        var new_tile = document.createElement('p');
        var temp_id = "id" + id_var;
        new_tile.id = temp_id
        new_tile.className = ""
        var new_class = "t" + gameBoard[i][ii][1] 
        new_tile.classList.add('tile', new_class);   // add multiple classes
        new_tile.textContent = gameBoard[i][ii][1]
        new_tile.style.setProperty('--y', i);
        new_tile.style.setProperty('--x', ii);
        document.getElementById('gameboard').appendChild(new_tile);
        gameBoard[i][ii][0] = temp_id
        id_var += 1
      }
    }
  }

}

// Forandring av Score
function scoreLogic(x){
  score += x
  document.getElementById("score").textContent = "Score: " + score
  if(score > best_score){
    best_score = score
    document.getElementById("best_score").textContent = "Best: " + best_score
  }
}


//Hva som skjer nå du beveger på Tiles
function onMove(){
  if(change == true){
    createChip()
    /*console.clear();*/
    consoleView()
    change = false
    save()
  }
}

// Sjekker om vi har tapt? Kan Tiles bevege seg?
function checkLose(){
  lost = true
  for(i=0; i<number_of_rows; i++){
    for(ii=0; ii<number_of_rows; ii++){
      if(ii != 0 && gameBoard[i][ii][1] == gameBoard[i][ii-1][1]){lost = false} // Er det en lik Tile til venstre for blokken?
      if(ii != number_of_rows-1 && gameBoard[i][ii][1] == gameBoard[i][ii+1][1]){lost = false} // Er det en lik Tile til høyre for blokken?
      if(i != number_of_rows-1 && gameBoard[i][ii][1] == gameBoard[i+1][ii][1]){lost = false} // Er det en lik Tile under for blokken?
      if(i != 0 && gameBoard[i][ii][1] == gameBoard[i-1][ii][1]){lost = false} // Er det en lik Tile over for blokken?

      if(ii != 0 && gameBoard[i][ii-1][1] == 0){lost = false} // Er det en ledig plass til venstre for blokken?
      if(ii != number_of_rows-1 && gameBoard[i][ii+1][1] == 0){lost = false} // Er det en ledig plass til høyre for blokken?
      if(i != number_of_rows-1 && gameBoard[i+1][ii][1] == 0){lost = false} // Er det en ledig plass over blokken?
      if(i != 0 && gameBoard[i-1][ii][1] == 0){lost = false} // Er det en ledig plass under blokken?
    }
  }

  //Hva skjer hvis vi taper?
  if(lost == true){
    console.log("You lost")
    document.getElementById("lost").style.display = "grid";
  }
}

//Hva som skjer når du trykker på reset
function reset(){
  localStorage.removeItem("2048_save")
  localStorage.removeItem("2048_score")
  location.reload();
}


// Save
function save(){
  localStorage.setItem("2048_save", gameBoard)
  localStorage.setItem("2048_score", score)
  localStorage.setItem("2048_best", best_score)
}

//Load 
function load(){
  

  score = localStorage.getItem("2048_score")
  score = parseInt(score)
  
  if(score == null || isNaN(score) == true){
    score = 0
  }

  best_score = localStorage.getItem("2048_best")
  console.log(best_score)
  best_score = parseInt(best_score)
  if(best_score == null || isNaN(best_score) == true){
    best_score = 0
  }
  document.getElementById("best_score").textContent = "Best: " + best_score
  scoreLogic(0)

  var temp_array = localStorage.getItem("2048_save", gameBoard)

  if(temp_array != null){
    temp_array = temp_array.split(",")

    var counter = 0
    for(i=0; i<number_of_rows; i++){
      for(ii=0; ii<number_of_collums; ii++){

        for(c=0; c<Tile_values.length; c++){
          if(temp_array[counter] == Tile_values[c].toString()){
            temp_array[counter] = parseInt(temp_array[counter])
          }
          if(temp_array[counter+1] == Tile_values[c].toString()){
            temp_array[counter+1] = parseInt(temp_array[counter+1])
          }
        }
  
        gameBoard[i][ii][0] = temp_array[counter]
        gameBoard[i][ii][1] = temp_array[counter+1]
        counter += 2
      }
    }
     buildBoard()
     consoleView()
  }else{
    console.log("No save-data found..")
    startGame()
  }
}

// KEYBOARD LOGIC - MOVEMENT
// Fremtid: left = 37   -   up = 38   -   right = 39   -   down = 40
addEventListener('keydown', ({key}) =>{
  if(clicked == false && lost == false){
    //Beveg mot høyre
    if(key == "d" && keys.right.pressed != true){
      keys.right.pressed = true
      moveRight()
    }
    //Beveg mot venstre
    if(key == "a" && keys.left.pressed != true){
      keys.left.pressed = true
      moveLeft()
    }
    //Beveg mot opp
    if(key == "w" && keys.up.pressed != true){
      keys.up.pressed = true
      moveUp()
    }
    //Beveg mot ned
    if(key == "s" && keys.down.pressed != true){
      keys.down.pressed = true
      moveDown()
    }
    clicked = true
    checkLose()
  }
})


addEventListener('keyup', ({key}) =>{
  if(lost == false){
    
    if(key == "d"){ // Beveg mot høyre
      keys.right.pressed = false
    }
    
    if(key == "a"){ // Beveg mot venstre
      keys.left.pressed = false
    }
   
    if(key == "w"){  // Beveg opp
      keys.up.pressed = false
    }
    
    if(key == "s"){ //Beveg ned
      keys.down.pressed = false
    }
    
    clicked = false // Vi kan nå trykke igjen

    if (change == true){ // Hvis banen har forandret seg på skjer dette
      onMove()
    }
  }
})