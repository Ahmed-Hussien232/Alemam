const Cashin = document.getElementById("cash-in");
const Notes = document.getElementById("notes");
const form = document.getElementById("form");

function showError(input, message){
  const formControl = input.parentElement;
  formControl.className = "form-control error";
  const small = formControl.querySelector("small");
  small.innerText = message;
}

function showSuccess(input){
  const formControl = input.parentElement;
  formControl.className = "form-control success";
}


function checkCashin(){
  if (Cashin.value === ""){
    showError(Cashin, "Cash-in is requierd");
  }
  else {
    showSuccess(Cashin);
  }
}

function checkNotes(){
  if (Notes.value === ""){
    showError(Notes, "Notes is requierd");
  }
  else {
    showSuccess(Notes);
  }
}


form.addEventListener("submit", function(e){
  e.preventDefault();
  checkCashin();
  checkNotes();
})

