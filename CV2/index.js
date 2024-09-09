
// Logic for changing page
function change_page(nr){

  const items = document.querySelectorAll('.page');

  items.forEach(item => {
    item.addEventListener('click', function() {

      // Remove 'active' class from all items
      items.forEach(i => i.classList.remove('active'));


      // Add 'active' class to the clicked item
      this.classList.add('active');
    });
  });

  // Scroll to top of div we are not in
  if(nr == 1){
    document.getElementById("portfolio").scroll(0,0)
  }
  if(nr == 2){
    document.getElementById("about").scroll(0,0)
  }
  
}

// Logic for animastion happening on load
function load_page(){
  
  document.getElementById("intro").classList.add('active');
  document.getElementById("site").classList.add('launched');
  

  // logic for seeing if a project div is within screen or not.
  // 
  const observer = new IntersectionObserver((entries) =>{
    entries.forEach((entry) =>{
      //console.log(entry)
      if (entry.isIntersecting){
        entry.target.classList.add('show');
      } else {entry.target.classList.remove('show');}
    })
  })
  
  const hiddenElements = document.querySelectorAll('.hidden');
  hiddenElements.forEach((el) => observer.observe(el))

  document.getElementById("portfolio").scroll(0,0)


  // Logic for video play on hover and reset/pause otherwise
  //
  //
  const videos = document.querySelectorAll('video');

  videos.forEach(video => {
    video.addEventListener('mouseenter', () => {
      video.play();
    });
    
    video.addEventListener('mouseleave', () => {
      video.pause();
      video.currentTime = 0;
    });
  });

}



