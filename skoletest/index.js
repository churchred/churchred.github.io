
// List of students
const studentDatabase = [
  "Ole Andersen",
  "Liv Olsen",
  "Jarle Peterson",
  "Anna Johansen",
  "Mikkel Berg",
  "Sofie Nilsen",
  "Emil Jensen",
  "Lena Kristiansen",
  "William Hansen",
  "Ida Sørensen",
  "Noah Jacobsen",
  "Emma Larsen",
  "Lucas Pedersen",
  "Nora Madsen",
  "Felix Mortensen",
  "Ella Iversen",
  "Oliver Skjold",
  "Sophie Lund",
  "Jakob Møller",
  "Thea Christiansen"
]

const approveDatabase = [
  ["Ole Halvorsen", "08:30 - 14:00 (Hele Dagen)", "Ole skal til legen i dag. Blir hjemme."],
  ["Liv Andersen", "10:00 - 12:00 (2 timer)", "Liv skal til tannlegen. Henter henne"],
  ["Jonas Kirkerød", "08:30 - 14:00 (Hele Dagen)", "Vi skal på sverige tur. Tar en tidlig helg!"]
]

// Logic for login page
function logIn(){

  // Gets the value from the input fields
  // Password-field is currently not in use
  username = document.getElementById("username").value
  password = document.getElementById("pass").value

  // If username is "lærer" go to the teacher page
  if (username.toLowerCase() == "lærer"){window.location.href = `teacher.html`;}

  // If username is "elev" go to the student page
  else if(username.toLowerCase() == "elev"){window.location.href = `student.html`;}

  // If username is "foresatt" go to the student page
  else if(username.toLowerCase() == "foresatt"){window.location.href = `parent.html`;}
  
}

// Logic for going to new page
// Exists to make html more readable
function new_page(url){
  window.location.href = url;
}

// Logic for making password input field visible or hidden
function show_password(){

  // Makes variables containng the "eye"-button and password field
  button = document.getElementById("eye")
  passwordField = document.getElementById("pass")

  // If the eye is closed(password is hidden), we change it to open and make input text visible
  // If not then we do the opisite
  if(button.src.endsWith("assets/eye_closed.png")){
    button.src = "assets/eye.png"
    passwordField.type = "text"; 
  } else{
    button.src = "assets/eye_closed.png" 
    passwordField.type = "password";
  }
}


function toggleGone(id) {
  // Get the element by its ID
  const element = document.getElementById(id);
  
  // Check if the element exists to avoid errors
  if (element) {
      // If the element has no class, add the "gone" class
      if (element.classList.length === 0) {
          element.classList.add("gone");
      } else {
          // If the element already has any class, toggle the "gone" class
          element.classList.toggle("gone");
      }
  } else {
      console.error("Element not found with id:", id);
  }
}



// Makes all the student names into clickable div elements for absent page
function build_student_list(nr){

  let list

  if (nr == 1){
    list = studentDatabase.slice(0);
  }
  else if (nr == 2){
    list = studentDatabase.slice(0, 4);
  }
  else if (nr == 3){
    list = studentDatabase.slice(4);
  }

  for(let i=0; i<list.length; i++){

    // Create main container div
    const elevDiv = document.createElement("div");
    let temp_id = "elev_" + String(i)
    console.log(temp_id)
    elevDiv.id = temp_id;
    elevDiv.onclick = function() { toggleGone(temp_id); };

    // Create and append img element
    const img = document.createElement("img");
    img.src = "assets/profile_icon-2.png";
    elevDiv.appendChild(img);

    // Create and append p element for name
    const namePara = document.createElement("p");
    namePara.className = "absent-navn";
    namePara.textContent = list[i];
    elevDiv.appendChild(namePara);

    // Create and append p element for status
    const statusPara = document.createElement("p");
    statusPara.className = "absent-status";
    elevDiv.appendChild(statusPara);

    // Append the completed elevDiv to the "page" div
    document.getElementById("absent-wrapper").appendChild(elevDiv);
  }
}



// Fucntion for setting the correct time
function check_time(){

  // Gets current time in this format: 11:18:48 AM
  d = new Date().toLocaleTimeString();

  // We dont need all of it, only hours and seconds
  d = d.split(":")
  d = d[0] + ":" + d[1]

  // Change html text of clock to current time
  document.getElementById('clock').innerText = d
}

// Function for setting current date
function check_date(){

    // Array of weekday and month names in Norwegian
    const weekdays = ["Søndag", "Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag"];
    const months = ["januar", "februar", "mars", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "desember"];
    
    // Get the current date
    const date = new Date();
    
    // Extract day, weekday, month, and year components
    const day = date.getDate();
    const weekday = weekdays[date.getDay()];
    const month = months[date.getMonth()];
    const year = date.getFullYear();

    // Set new date in this format: Mandag 07. januar 2025
    document.getElementById('date').innerText = weekday + " " + day + ". " + month + " " + year;
}

// 
function set_time(){
  check_time()
  check_date()
}




// Function to create and append items based on the approveDatabase array
function populateApproveItems() {
  const approveWrapper = document.getElementById('approve');
  
  approveDatabase.forEach((item, index) => {
    // Destructure the item array for better readability
    const [name, time, description] = item;

    // Create the main div
    const approveItem = document.createElement('div');
    approveItem.className = 'approve-item';
    approveItem.id = index + 1;
    

    // Create the inner elements
    const nameHeading = document.createElement('h2');
    nameHeading.textContent = name;

    const timeHeading = document.createElement('h3');
    timeHeading.textContent = `Fra ${time}`;

    const descriptionParagraph = document.createElement('p');
    descriptionParagraph.textContent = description;

    const buttonContainer = document.createElement('div');
    
    const approveButton = document.createElement('button');
    approveButton.setAttribute('onclick', `removeItem(${index + 1})`);
    approveButton.className = 'yes';
    approveButton.textContent = 'Godkjenn';

    const rejectButton = document.createElement('button');
    rejectButton.className = 'no';
    rejectButton.setAttribute('onclick', `removeItem(${index + 1})`);
    rejectButton.textContent = 'Ikke godkjenn';

    // Append buttons to the button container
    buttonContainer.appendChild(approveButton);
    buttonContainer.appendChild(rejectButton);

    // Append all elements to the main approveItem div
    approveItem.appendChild(nameHeading);
    approveItem.appendChild(timeHeading);
    approveItem.appendChild(descriptionParagraph);
    approveItem.appendChild(buttonContainer);

    // Append approveItem to the approveWrapper section
    approveWrapper.appendChild(approveItem);
  });
}

// Function to remove an item by ID
function removeItem(id) {
  const itemToRemove = document.getElementById(id);
  if (itemToRemove) {
    itemToRemove.remove();
  }
}