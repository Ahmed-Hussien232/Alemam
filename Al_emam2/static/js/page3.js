const printingtype = document.getElementById("printing-type");
const papersize = document.getElementById("paper-size");
const paperprice = document.getElementById("paper-price");
const papernumber = document.getElementById("paper-number");
const copynumber = document.getElementById("copy-number")
const other = document.getElementById("other");
const pay = document.getElementById("pay");
const form = document.getElementById("form");
const totalPriceElement = document.getElementById("total-price")


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

function checkPrintingtype(){
  if (printingtype.value === "أختر نوع الطباعة"){
    showError(printingtype, "printing-type is requierd");
  }
  else {
    showSuccess(printingtype);
  }
}

function checkPapersize(){
  if (papersize.value === "حجم الورقة"){
    showError(papersize, "paper-size is requierd");
  }
  else {
    showSuccess(papersize);
  }
}

function checkPaperprice(){
  if (paperprice.value === ""){
    showError(paperprice, "paper-price is requierd");
  }
  else {
    showSuccess(paperprice);
  }
}

function checkpapernumber(){
  if(papernumber.value ===""){
    showError(papernumber, "paper-number is requierd");
  }
  else {
    showSuccess(papernumber);
  }
}

function checkcopynumber(){
  if(copynumber.value ===""){
    showError(copynumber, "copy-number is requierd");
  }
  else {
    showSuccess(copynumber);
  }
}

function checkother(){
  if(other.value ===""){
    showError(other, "It's requierd");
  }
  else {
    showSuccess(other);
  }
}


function checkpay(){
  if(pay.value ==="طريقة الدفع"){
    showError(pay, "pay is requierd");
  }
  else {
    showSuccess(pay);
  }
}



function calculateTotal() {
    const price = parseFloat(paperprice.value) || 0;
    const paperNum = parseInt(papernumber.value) || 0;
    const copyNum = parseInt(copynumber.value) || 0;
    const extra = parseFloat(other.value) || 0;

    if (price <= 0 || paperNum <= 0 || copyNum <= 0) {
        totalPriceElement.innerText = "0 جنيه"; 
        return;
    }
    
    const total = (price * paperNum * copyNum) + extra;
    totalPriceElement.innerText = total.toFixed(1) + " جنيه";
}

// تحديث الحساب عند تغيير القيم
paperprice.addEventListener("input", calculateTotal);
papernumber.addEventListener("input", calculateTotal);
copynumber.addEventListener("input", calculateTotal);
other.addEventListener("input", calculateTotal);




form.addEventListener("submit", function(e){
 
  checkPrintingtype();
  checkPapersize();
  checkPaperprice();
  checkpapernumber();
  checkcopynumber();
  checkother();
  checkpay();
  

  if (printingtype.value === "أختر نوع الطباعة " || papersize.value === "حجم الورقة" || paperprice.value === "" || papernumber.value ==="" || copynumber.value ==="" || other.value ==="" || pay.value ==="طريقة الدفع"){
    e.preventDefault();
  } else{
    form.submit();
  }
})



