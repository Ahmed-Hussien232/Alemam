const username = document.getElementById("username");
const password = document.getElementById("password");
const password2 = document.getElementById("password2");
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

function checkUsername(){
  if (username.value === ""){
    showError(username, "username is requierd");
  }
  else {
    showSuccess(username);
  }
}

function checkPassword(){
  if (password.value === ""){
    showError(password, "password is requierd");
  }
  else {
    showSuccess(password);
  }
}

function checkPassword2(){
  if (password2.value === ""){
    showError(password2, "confirming password is requierd");
  }
  else {
    showSuccess(password2);
  }
}

function checkPassword2Match(){
  if(password.value !== password2.value){
    showError(password2, "passwords don't match");
  }
}

form.addEventListener("submit", function(e){
  checkUsername() ;
  checkPassword() ;
  checkPassword2() ;
  checkPassword2Match();
  
  if (username.value === "" || password.value === "" || password2.value === "" || password.value !== password2.value){
    e.preventDefault();
  } else{
    form.submit();
  }

})