

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
  if(nr != 1){
    document.getElementById("portfolio").scroll(0,0)
  }
  if(nr != 2){
    document.getElementById("about").scroll(0,0)
  }
  
}


function change_page2(nr){
  console.log(nr)
}