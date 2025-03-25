const Cashout = document.getElementById("cash-out");
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


function checkCashout(){
  if (Cashout.value === ""){
    showError(Cashout, "Cashout is requierd");
  }
  else {
    showSuccess(Cashout);
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
  
  checkCashout();
  checkNotes();
  if (Cashout.value === "" || Notes.value === ""){
    e.preventDefault();
  } else{
    form.submit();
  }
})

