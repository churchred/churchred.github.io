



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


  // We make an observer to see if a project div is within the viewport or not
  // If it is we give it the show class, which will play an entry animation
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('show');
      } //else{entry.target.classList.remove('show');}
    });
  }, { 
    threshold: 0.3,  // Trigger when 40% of the element is in view
    root: null


  });
  
  const hiddenElements = document.querySelectorAll('.hidden');
  hiddenElements.forEach((el) => observer.observe(el))



  // Makes two eventlisteners. 
  // One to see if the mouse is within the video, 
  // and another to see if it leaves.
  const videos = document.querySelectorAll('video');
  
  videos.forEach(video => {

    video.currentTime = video.duration;

    video.addEventListener('mouseenter', () => {
      video.currentTime = 0;
      video.play();
    });
    
    video.addEventListener('mouseleave', () => {
      video.pause();
      video.currentTime = video.duration;
    });
  });


}


// What happens if we click meny button
function click_btn(){
  const nav_bar = document.getElementsByClassName('banner-body')[0]
  nav_bar.classList.toggle('active')
  console.log("CLICKED")
}

