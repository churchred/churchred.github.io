

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
}


function change_page2(nr){
  console.log(nr)
}