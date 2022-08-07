



function click_btn(){
  const nav_bar = document.getElementsByClassName('dropdown')[0]
  nav_bar.classList.toggle('active')
}

function big_dikt(x){
  document.getElementById('big_dikt').style.display = 'grid'
  document.getElementById('big_dikt_img').src = "Bilder/Dikt/" + x + ".jpg"
  
}

function hide_img(){
  document.getElementById('big_dikt').style.display = 'none'
}


function scroll_up(){
  window.scrollTo(0, 0)
  document.getElementById('big_dikt').style.display = 'none'
}