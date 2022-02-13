const  numberButtons = document.querySelectorAll('[data-number]')
const operationButtons = document.querySelectorAll('[data-operation]')
const equalsButton = document.querySelector('[data-equals]')
const deleteButtons = document.querySelector('[data-delete]')
const allclearButtons = document.querySelector('[data-allclear]')
let curOpTextElement= document.querySelector ("[data-current-operand]");    // These two lines define the property variables. We will use them in the function below with the "this" keyword.
let  prevOpTextElement = document.querySelector("[data-previous-operand]"); 
let resultBox = document.getElementById("answer");


let operation;
let answer;
let currentoperand="";
let previousoperand="";


function clearNumbers(){
    currentoperand = ""
    previousoperand =""
    operation = ""
    console.log("user used all clear action ");
    prevOpTextElement.textContent=previousoperand;
    curOpTextElement.textContent=currentoperand;
    resultBox.textContent="";
}

function appendNumber(number){
    currentoperand = parseInt (number,10);
    curOpTextElement.textContent=currentoperand;
    console.log(currentoperand);
}
function chooseOperation(userOperation){
    previousoperand=currentoperand
    prevOpTextElement.textContent=previousoperand;
    operation=userOperation;
    currentoperand = "";
    curOpTextElement.textContent=currentoperand;
    console.log("user choice,",operation)
}
function compute(){ 
    console.log("perform the computation");
    switch(operation){
        case "*":answer=previousoperand*currentoperand;
            break;
        case"/":answer=previousoperand/currentoperand;
            break;
        case"+":answer=previousoperand+currentoperand;
            break;
        case"-":answer=previousoperand-currentoperand;
            break;
    }
    resultBox.textContent = answer;
    console.log(previousoperand, operation, currentoperand, "=", answer);
}
    


numberButtons.forEach(button => {
    button.addEventListener("click", () => {
        appendNumber(button.innerText)
    });
    
});
operationButtons.forEach(button => {
    button.addEventListener("click", () => {
        chooseOperation(button.innerText)
    });
    
});
equalsButton.addEventListener("click",compute);
allclearButtons.addEventListener("click",clearNumbers);