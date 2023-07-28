

//Banen vi spiller på  -  [ID, Value]
let gameBoard = [
  [[0,0], [0,0], [0,0], [0,0]],
  [[0,0], [0,0], [0,0], [0,0]],
  [[0,0], [0,0], [0,0], [0,0]],
  [[0,0], [0,0], [0,0], [0,0]]
]

// Variables

var Rows = 4         // The number of rows in the game board
var Collums = 4      // The number of collums in the game row


var clicked = false  // This is so that we can only press one key at the time, and the key is only pressed once when pressed each time.

var id_var = 0       // This helps to give each Tile created a uniqe id.

var change = false  //Har banen forandret seg siden du trykket sist?


var score = 0       // The value for the score
var best_score = 0  // The value for the Best Score

var lost = false    // We lose if this becomes true.

var chance_4 = 10  // The chance for a new Tile to have the value 4 instead of 2. The chance is 1 in whatever this variable is.

let Tile_values = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192] //This contain all the values a tile can have. It is used in the Load function.



// This function starts up a new game
function startGame() {
  createChip()  // Created two Tiles.
  createChip()
  consoleView() // Prints the board in the Console.
}


// This function creates new Tiles.
function createChip(){

  var rand_row = Math.floor(Math.random() * Rows)       // Makes a ranom number from 0-3
  var rand_collum = Math.floor(Math.random() * Collums) // Makes a ranom number from 0-3
  var cc_row = 0                                        // Keeps track on which row we're checking
  var cc_collum = 0                                     // Keeps track on which collum we're checking
  var done = false                                      // If a Tile has been placed then this is true and the loop will finish without making more



  for(i=0; i<Rows + 1; i++){
    if(i+rand_row >= Rows){                          
      cc_row = i + rand_row-Rows                     
    }                                                
    else{                                            
      cc_row = i+rand_row                            
    }                                            // This function creates a random startpoint on our gameboard.                        
    for(ii=0; ii<Rows; ii++){                    // It checks it the play space is empty or if there is an Tile there.
      if(i > Rows-1 && ii > rand_collum-1){      // If its empty then a Tile is created in the location.
        break                                    // If its NOT empty then it checks the next collums and works
      }                                          // its way down the rows until it has looked at the whole board.    
      else if(i > 0){                            // This ensures that a Tile is created at a RANDOM location each time.
        cc_collum = ii
      }
      else if(ii+rand_collum >= Rows){
        break
      }
      else{
        cc_collum = ii + rand_collum
      }



      //Making a Tile
      if(gameBoard[cc_row][cc_collum][0] == 0 && done == false){

        var new_tile = document.createElement('p');  // Creates a new p-element, which is a Tile.
        var temp_id = "id" + id_var;                 // Creates an uniqe ID based on the id-var for the Tile.
        new_tile.id = temp_id                        // Adds the ID to the Tile.


        var rand_number = Math.floor(Math.random() * chance_4)  // Creates a random number based on the chance variable.
        var new_value = 2                                       // Gives the value 2 to the Tile.
        if(rand_number == 0){new_value = 4}                     // If the random number is 0 then the Tile value is changed to 4
        new_tile.textContent = new_value                        // Sets the value to the Tile.


        new_tile.className = ""                            // Resets the class of the Tile.
        var new_class = "t2"                               // Gives it the t2 class, which is the color.
        new_tile.classList.add('tile', new_class, "new");  // Adds 3 new classes to the Tile.


        new_tile.style.setProperty('--y', cc_row);                   // Gives the Tile a new x location on the board.
        new_tile.style.setProperty('--x', cc_collum);                // Gives the Tile a new y location on the board
        document.getElementById('gameboard').appendChild(new_tile);  // Finally creates the Tile and places in on the screen.

        gameBoard[cc_row][cc_collum][0] = temp_id       // Updates the gameboard array so the 
        gameBoard[cc_row][cc_collum][1] = new_value     // backend board is the same as the onscreen one.

        id_var += 1   // Increased the id variable so the next tile gets an unique one.
        done = true   // This stops the for loop from creating more Tile if it finds more avalible space

        console.log("New Tile being made at: [", cc_row, ",", cc_collum, "]")
      }
    }
  }


}

// This the logic for Tiles moving to the RIGHT.
function moveRight(){

  for(var j=0; j<6; j++){                                                    // The first loop runs 6 times. Loop 0-2 it moves the pieces one space each time.
    if(j != 3){                                                              // On the 3.loop it checks if two Tiles with equal values are next to each other.
      for(var i=0; i<Rows; i++){                                             // On loop 4,5 it moves the Tiles to the right twice.(Since merging creates space).
        for(var ii=0; ii<Collums; ii++){
          if(gameBoard[i][ii][0] != 0 && ii != Collums-1){         
            if(gameBoard[i][ii+1][0] == 0){                       
              var tile = document.getElementById(gameBoard[i][ii][0])       // This function works like this:
              tile.style.setProperty('--x', ii+1);                          // It starts at the top-left and sees it there is a Tile there.
              gameBoard[i][ii+1] = gameBoard[i][ii]                         // If there is then it checks if there is an empty space to its right.
              gameBoard[i][ii] = [0, 0]                                     // If it is then the Tile moves there and the gameboard-array is updates to match.
              change = true                                                 // The 'change' variable is now true, which means a new Tile will be automaticly 
            }                                                               // created when the moveRight func is done.
          }
        }
      }
    }

    if(j == 3){
      for(var i=0; i<Rows; i++){
        for(var ii=Collums-1; ii>-1; ii--){
          if(ii != 0 && gameBoard[i][ii][0] != 0){
            if(gameBoard[i][ii][1] == gameBoard[i][ii-1][1]){
              
              var tile1 = document.getElementById(gameBoard[i][ii-1][0])     // Checks whether or not two Tiles of equal value are next to each other.
              var tile2 = document.getElementById(gameBoard[i][ii][0])       // It starts at the top-right this time since the right most Tile is the 
                                                                             // one that will be replaced. It checks it the Tile to the LEFT is equal.
              tile1.style.setProperty('--x', ii)                             // If it is the same then the right most Tile is removed and the left is
              tile2.remove()                                                 // updated to a higher value and moved to the right.
              tile1.textContent = (gameBoard[i][ii][1] * 2)

              gameBoard[i][ii] = gameBoard[i][ii-1]
              gameBoard[i][ii][1] = gameBoard[i][ii][1]*2    // This part updates the gameboard-array info to match the new screen board.
              scoreLogic(gameBoard[i][ii][1]) 
              gameBoard[i][ii-1] = [0, 0]

              tile1.className = ""
              var new_class = "t" +  gameBoard[i][ii][1]  // Adds new class to the new Tile.
              tile1.classList.add('tile', new_class);

              change = true
             
            }
          }
        }
      }
    }
  }

}

// This is the logic for Tiles moving to the LEFT
function moveLeft(){
   
  for(var j=0; j<6; j++){                                                
    if(j != 3){                                                          
      for(var i=0; i<Rows; i++){                                                                                 
        for(var ii=Collums-1; ii>-1; ii--){                              // The first loop runs 6 times. Loop 0-2 it moves the pieces one space each time.
          if(gameBoard[i][ii][0] != 0 && ii != 0){                       // On the 3.loop it checks if two Tiles with equal values are next to each other.           
            if(gameBoard[i][ii-1][0] == 0){                              // On loop 4,5 it moves the Tiles to the right twice.(Since merging creates space).
              var tile = document.getElementById(gameBoard[i][ii][0])    
              tile.style.setProperty('--x', ii-1);                       // This function works like this: 
              gameBoard[i][ii-1] = gameBoard[i][ii]                      // It starts at the top-right and sees it there is a Tile there.
              gameBoard[i][ii] = [0, 0]                                  // If there is then it checks if there is an empty space to its left.
              change = true                                              // If there is then the Tile moves there and the gameboard-array is updates to match.
            }                                                            // The 'change' variable is now true, which means a new Tile will be automaticly
          }                                                              // created when the moveRight func is done. 
        }
      }
    }

    if(j == 3){
      for(var i=0; i<Rows; i++){
        for(var ii=0; ii<Collums; ii++){
          if(ii != Collums-1 && gameBoard[i][ii][0] != 0){
            if(gameBoard[i][ii][1] == gameBoard[i][ii+1][1]){                  // Checks whether or not two Tiles of equal value are next to each other.
                                                                               // It starts at the top-left since the left-most Tile is the 
              var tile1 = document.getElementById(gameBoard[i][ii+1][0])       // one that will be replaced. It checks it the Tile to the RIGHT is equal.
              var tile2 = document.getElementById(gameBoard[i][ii][0])         // If it is the same then the left most Tile is removed and the right is
                                                                               // updated to a higher value and moved to the right.
              tile1.style.setProperty('--x', ii)
              tile2.remove()
              tile1.textContent = (gameBoard[i][ii][1] * 2)

              gameBoard[i][ii] = gameBoard[i][ii+1]
              gameBoard[i][ii][1] = gameBoard[i][ii][1]*2      // This part updates the gameboard-array info to match the new screen board.
              scoreLogic(gameBoard[i][ii][1])
              gameBoard[i][ii+1] = [0, 0]

              tile1.className = ""
              var new_class = "t" +  gameBoard[i][ii][1]       // Adds new class to the new Tile.
              tile1.classList.add('tile', new_class);
             
              change = true
            }
          }
        }
      }
    }
  }
}


// This is the logic for Tiles moving UP
function moveUp(){
  for(var j=0; j<6; j++){                                                 // The first loop runs 6 times. Loop 0-2 it moves the pieces one space each time.
    if(j != 3){                                                           // On the 3.loop it checks if two Tiles with equal values are under/above each other.  
      for(var i=Rows-1; i>-1; i--){                                       // On loop 4,5 it moves the Tiles up twice.(Since merging creates space).
        for(var ii=0; ii<Collums; ii++){
          if(i != 0 && gameBoard[i][ii][0] != 0){                         // This function works like this:  
            if(gameBoard[i-1][ii][1] == 0){                               // It starts at the bottom-right and sees it there is a Tile there.
              var tile = document.getElementById(gameBoard[i][ii][0])     // If there is then it checks if there is an empty space on the row right above.
              tile.style.setProperty('--y', i-1);                         // If there is then the Tile moves there and the gameboard-array is updates to match.
              gameBoard[i-1][ii] = gameBoard[i][ii]                       // The 'change' variable is now true, which means a new Tile will be automaticly
              gameBoard[i][ii] = [0,0]                                    // created when the moveUp func is done. 
              change = true
            }
          }
        }
      }
    }
    
    if(j == 3){                                                        
      for(var i=0; i<4; i++){
        for(var ii=0; ii<Collums; ii++){
          if(i != Rows-1 && gameBoard[i][ii][0] != 0){
            if(gameBoard[i][ii][1] == gameBoard[i+1][ii][1]){
              var tile1 = document.getElementById(gameBoard[i][ii][0])     // Checks whether or not two Tiles of equal value are under/above each other.
              var tile2 = document.getElementById(gameBoard[i+1][ii][0])   // It starts at the top-left since the top-most Tile is the 
                                                                           // one that will be replaced. It checks it the Tile under it is equal.
              tile2.style.setProperty('--y', i)                            // If it is the same then the top-most Tile is removed and the one underneath is
              tile1.remove()                                               // updated to a higher value and moved up.
              tile2.textContent = (gameBoard[i][ii][1] * 2)


              gameBoard[i][ii] = gameBoard[i+1][ii]
              gameBoard[i][ii][1] = gameBoard[i][ii][1]*2       // This part updates the gameboard-array info to match the new screen board.
              scoreLogic(gameBoard[i][ii][1])                   
              gameBoard[i+1][ii] = [0, 0]

              tile2.className = ""
              var new_class = "t" +  gameBoard[i][ii][1]        // Adds new class to the new Tile.
              tile2.classList.add('tile', new_class);
              change = true
            }
          }
        }
      }
    }
  }
}



// This is the logic for Tiles moving DOWN
function moveDown(){
  for(var j=0; j<6; j++){                                             // The first loop runs 6 times. Loop 0-2 it moves the pieces one space each time.  
    if(j != 3){                                                       // On the 3.loop it checks if two Tiles with equal values are over/under each other.
      for(var i=0; i<Rows; i++){                                      // On loop 4,5 it moves the Tiles down twice.(Since merging creates space).       
        for(var ii=0; ii<Collums; ii++){                                              
          if(i != Rows-1 && gameBoard[i][ii][0] != 0){                // This function works like this:                      
            if(gameBoard[i+1][ii][1] == 0){                           // It starts at the top-left and sees it there is a Tile there.             
              var tile = document.getElementById(gameBoard[i][ii][0]) // If there is then it checks if there is an empty space on the row right underneath.                
              tile.style.setProperty('--y', i+1);                     // If there is then the Tile moves there and the gameboard-array is updates to match.          
              gameBoard[i+1][ii] = gameBoard[i][ii]                   // The 'change' variable is now true, which means a new Tile will be automaticly                          
              gameBoard[i][ii] = [0,0]                                // created when the moveDown func is done.                            
              change = true                                                    
            }
          }
        }
      }
    }
    
    if(j == 3){
      for(var i=Rows-1; i>-1; i--){
        for(var ii=0; ii<Collums; ii++){                                  // Checks whether or not two Tiles of equal value are under/above each other.
          if(i != 0 && gameBoard[i][ii][0] != 0){                         // It starts at the bottom-left since the bottom-most Tile is the 
            if(gameBoard[i][ii][1] == gameBoard[i-1][ii][1]){             // one that will be replaced. It checks it the Tile above it is equal.             
              var tile1 = document.getElementById(gameBoard[i][ii][0])    // If it is the same then the bottom-most Tile is removed and the one above is
              var tile2 = document.getElementById(gameBoard[i-1][ii][0])  // updated to a higher value and moved down.
              
              tile2.style.setProperty('--y', i)
              tile1.remove()
              tile2.textContent = (gameBoard[i][ii][1] * 2)

              gameBoard[i][ii] = gameBoard[i-1][ii]
              gameBoard[i][ii][1] = gameBoard[i][ii][1]*2                 // This part updates the gameboard-array info to match the new screen board.
              scoreLogic(gameBoard[i][ii][1])
              gameBoard[i-1][ii] = [0, 0]

              tile2.className = ""
              var new_class = "t" +  gameBoard[i][ii][1]                 // Adds new class to the new Tile.
              tile2.classList.add('tile', new_class);
              change = true
            }
          }
        }
      }
    }
  }
}


// Prints the backend version of the gameboard into the Console.
function consoleView() {
  console.log("----------------------------------------------------")
  console.log("Game:")
  console.log(gameBoard[0][0][1], gameBoard[0][1][1], gameBoard[0][2][1], gameBoard[0][3][1], "   #   ", gameBoard[0][0][0], gameBoard[0][1][0], gameBoard[0][2][0], gameBoard[0][3][0])
  console.log(gameBoard[1][0][1], gameBoard[1][1][1], gameBoard[1][2][1], gameBoard[1][3][1], "   #   ", gameBoard[1][0][0], gameBoard[1][1][0], gameBoard[1][2][0], gameBoard[1][3][0])
  console.log(gameBoard[2][0][1], gameBoard[2][1][1], gameBoard[2][2][1], gameBoard[2][3][1], "   #   ", gameBoard[2][0][0], gameBoard[2][1][0], gameBoard[2][2][0], gameBoard[2][3][0])
  console.log(gameBoard[3][0][1], gameBoard[3][1][1], gameBoard[3][2][1], gameBoard[3][3][1], "   #   ", gameBoard[3][0][0], gameBoard[3][1][0], gameBoard[3][2][0], gameBoard[3][3][0])
}

// This function builds the board based on how the backend gameboard-array looks. This is used when the game loads
function buildBoard(){
  for(var i=0; i<Rows; i++){
    for(var ii=0; ii<Collums; ii++){
      if(gameBoard[i][ii][1] != 0){
        
        var new_tile = document.createElement('p');      // Creates a new p-element, which is the new Tile.

        var temp_id = "id" + id_var;  // Creates an unique id based on the id-var 
        new_tile.id = temp_id         

        new_tile.className = ""                          // Reset classes
        var new_class = "t" + gameBoard[i][ii][1]        // Creates new class based on the value present in the gameboard-array
        new_tile.classList.add('tile', new_class);       // Adds the new classes

        new_tile.textContent = gameBoard[i][ii][1]       // Updates the number on the Tile based on the value in the gameboard-array
        new_tile.style.setProperty('--y', i);            // Sets the Tiles y-position
        new_tile.style.setProperty('--x', ii);           // Sets the Tiles x-position

        document.getElementById('gameboard').appendChild(new_tile);   // Creates and places the new Tile onto the screen
        gameBoard[i][ii][0] = temp_id                                 // Updates the id of the Tile in the backend.
        id_var += 1                                                   // Increase the id-var so the next Tile-id is unique.
      }
    }
  }

}

// Logic for changing the score.
function scoreLogic(x){

  score += x    //Increases the score var value by the amount sent. It is sent when two Tiles merge.
  
  document.getElementById("score").textContent = "Score: " + score  // Updates the on-screen value to match
  
  if(score > best_score){                                                      // If the score value is higher than the best-score value 
    best_score = score                                                         // then the current score becomes the best score. 
    document.getElementById("best_score").textContent = "Best: " + best_score  // Updates the on-screen value to match 
  }
}


// What happens whenever a Tile is moved.
function onMove(){

  if(change == true){ // This var is true if something has been moved on the board.
    createChip()      // It creates a new Tile
    consoleView()     // Prints the backend gameboard on the console.
    change = false 
    save()            // Saves the game
  }
}

// This function checks if we have lost the game. 
// More spesifically it checks wether or not it is 
// posible to move a Tile at all.
function checkLose(){
  lost = true
  for(i=0; i<Rows; i++){
    for(ii=0; ii<Collums; ii++){
      if(ii != 0 && gameBoard[i][ii][1] == gameBoard[i][ii-1][1]){lost = false} // Er det en lik Tile til venstre for blokken?
      if(ii != Rows-1 && gameBoard[i][ii][1] == gameBoard[i][ii+1][1]){lost = false} // Er det en lik Tile til høyre for blokken?
      if(i != Rows-1 && gameBoard[i][ii][1] == gameBoard[i+1][ii][1]){lost = false} // Er det en lik Tile under for blokken?
      if(i != 0 && gameBoard[i][ii][1] == gameBoard[i-1][ii][1]){lost = false} // Er det en lik Tile over for blokken?

      if(ii != 0 && gameBoard[i][ii-1][1] == 0){lost = false} // Er det en ledig plass til venstre for blokken?
      if(ii != Rows-1 && gameBoard[i][ii+1][1] == 0){lost = false} // Er det en ledig plass til høyre for blokken?
      if(i != Rows-1 && gameBoard[i+1][ii][1] == 0){lost = false} // Er det en ledig plass over blokken?
      if(i != 0 && gameBoard[i-1][ii][1] == 0){lost = false} // Er det en ledig plass under blokken?
    }
  }

  if(lost == true){            // This runs if we lose.
    console.log("You lost")
    document.getElementById("lost").style.display = "grid";  // Gameover screen becomes visible on screen.
  }
}



// What happens when we reset the game.
function reset(){
  localStorage.removeItem("2048_save")    // We remove the gameboard save-data
  localStorage.removeItem("2048_score")   // We remove the score save-data
  location.reload();                      // Then we reload the page
}


// Logic for saving.
function save(){
  localStorage.setItem("2048_save", gameBoard)   // Saves the backend gameboard 
  localStorage.setItem("2048_score", score)      // Saves the current score
  localStorage.setItem("2048_best", best_score)  // Saves the best score
}

// Logic for loading.
function load(){
  score = localStorage.getItem("2048_score")   // Loads the current score variable
  score = parseInt(score)                      // Is loaded as String, so we convert it to Int 
  
  if(score == null || isNaN(score) == true){   // If there is no data loaded the we set the value to 0
    score = 0
  }

  best_score = localStorage.getItem("2048_best")       // Loads the current best-score variable    
  best_score = parseInt(best_score)                    // Is loaded as String, so we convert it to Int 
  if(best_score == null || isNaN(best_score) == true){ // If there is no data loaded the we set the value to 0
    best_score = 0
  }

  document.getElementById("best_score").textContent = "Best: " + best_score  // Updates the onscreen best-score value
  scoreLogic(0)                                                              // Runs the score function and increases the score by 0,
                                                                             // which is the same as just updating it to the current value

  var temp_array = localStorage.getItem("2048_save", gameBoard)  // Loads the gameboard values

  if(temp_array != null){                                        // As long as it isnt empty then we proceed.

    temp_array = temp_array.split(",")         // Is loaded as a String so we convert it to a List.

    var counter = 0
    for(i=0; i<Rows; i++){
      for(ii=0; ii<Collums; ii++){

        for(c=0; c<Tile_values.length; c++){
          if(temp_array[counter] == Tile_values[c].toString()){      // We run through the new list of numbers and
            temp_array[counter] = parseInt(temp_array[counter])      // load the values into their correct places
          }                                                          // in the gameboard-array.
          if(temp_array[counter+1] == Tile_values[c].toString()){
            temp_array[counter+1] = parseInt(temp_array[counter+1])
          }
        }
  
        gameBoard[i][ii][0] = temp_array[counter]
        gameBoard[i][ii][1] = temp_array[counter+1]
        counter += 2
      }
    }
     buildBoard()   // Build the board based on the current gameboard-array values.
     consoleView()  // Also print it on the console
  }else{
    console.log("No save-data found..") // If there is no save-data
    startGame()                         // then we start a new game
  }
}


// Logic for the buttons that appear when on mobile
function mobile_move(direction){
  if(clicked == false && lost == false){
    
    if(direction == "right"){   // Move right
      moveRight()
    }
    
    if(direction == "left"){   // Move left
      moveLeft()
    }
    
    if(direction == "up"){     // Move up
      moveUp()
    }
    
    if(direction == "down"){   // Move down
      moveDown()
    }

    clicked = true     // This is so we cant click more than one button at the time and so that pressing a button only runs these functions once.
    checkLose()        // After button press we check if we have lost the game.
  }
  
  clicked = false

  if (change == true){ 
    onMove()             // This runs if the board has been changed after we pressed the button.
  }
}

// Logic for keyboard presses
addEventListener('keydown', ({key}) =>{
  if(clicked == false && lost == false){
    
    if(key == "d" || key == "ArrowRight"){   // Move right
      moveRight()
    }
    
    if(key == "a" || key == "ArrowLeft"){   // Move left
      moveLeft()
    }
    
    if(key == "w" || key == "ArrowUp"){     // Move up
      moveUp()
    }
    
    if(key == "s" || key == "ArrowDown"){   // Move down
      moveDown()
    }

    clicked = true     // This is so we cant click more than one button at the time and so that pressing a button only runs these functions once.
    checkLose()        // After button press we check if we have lost the game.
  }
})


addEventListener('keyup', ({key}) =>{
  if(lost == false){
    
    if(key == "d" || key == "ArrowRight" ){    // Move right 
      clicked = false
    }
    
    if(key == "a" || key == "ArrowLeft" ){    // Move left
      clicked = false
    }                                                               // This resets the clicked variable when the button is no longer pressed.
   
    if(key == "w" || key == "ArrowUp" ){     // Move up
      clicked = false
    }
    
    if(key == "s" || key == "ArrowDown" ){    // Move down
      clicked = false
    }

    if (change == true){ 
      onMove()             // This runs if the board has been changed after we pressed the button.
    }
  }
})