function click_btn(){
  const nav_bar = document.getElementsByClassName('dropdown')[0]
  nav_bar.classList.toggle('active')
  console.log("Dropdown: Active")
}


function unclick_btn(){
  const nav_bar = document.getElementsByClassName('dropdown')[0]
  
  if(nav_bar.classList[1] == 'active'){
    nav_bar.classList.toggle('active')
    console.log("Dropdown: No longer active")
  }
}