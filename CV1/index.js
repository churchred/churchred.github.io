



function load_page(){

  // Make all the boxes for the background grid
  const div_container = document.getElementById('grid');

  // Size of the grid (20x20)
  const grid_size = 400;

  // Make all the boxes(divs) and add them into the grid
  for (i = 0; i < grid_size; i++) {

    // Makes the new div
    box = document.createElement('div');

    // Adds class name
    box.className = ('grid-item');

    // Adds the div to the container
    div_container.append(box)
  }

}


// What happens if we click meny button
function click_btn(){
  const nav_bar = document.getElementsByClassName('banner-body')[0]
  nav_bar.classList.toggle('active')
  console.log("CLICKED")
}

