// let arry1 = ["Apple", "Banana", "Orange"];
// console.log(arry1[0]);
// console.log(arry1[1]);
// console.log(arry1[2]);

// console.log();





// if else statement
// let gender = "male"

// if(gender == "female"){
//     console.log("Welcome ma'am");
// }else if (gender == "male"){
//     console.log("Welcome sir");
// }else {
//     console.log("Welcome");
// }

// Falsy value
/* 
1. false
2. 0,-0
3. "",'',`` 
null
undefined 
NaN- Not a number

Truthy Values
/* 
1. true
2. 1, -1 any number apart from 0
3. "0", "false", ""
4. [], {}
function(), {}
6. infinity 
*/

//Loops 
//for Loops
/* 
keyword(variable; condition;increment/decrement){
 code to be executed
}
*/
// for(let i = 0; i < 5; i++){
//     console.log(i);
// }

//while loop
/*
variable initialization
keyword(condition){
 code block
 increment/decrement
}
 */
// let i = 0
// while(a < 5){
//     console.log(i);
//     i++;
// }

//do while loop
// let j = 0

// do{
//  console.log(j);
//  j++;
// }while(j < 5);


// let day = 3;
// switch(day){
//     case 1:
//      console.log("Monday");
//     break
//     case 2:
//         console.log("Tuesday");
//     break
//     case 3:
//         console.log("Wednesday");
//     break
//     case 4:
//         console.log("Thursday");
//      break
//     case 5:
//         console.log("Friday");
//     break
//     case 6:
//         console.log("Saturday");
//     break
//     case 7:
//         console.log("Sunday");
//     break
//     default:
//         console.log("invalid day");
// }

// let day1 = "Monday"
// switch (day1) {
//     case "Wednesday":
//         console.log("Working day");
//         break;
//     default:
//         console.log("Weekend");
// }

// //Ways to name a function
// /* 
// 1st step*/
// function functionName(parameter) {
//     //code of block
// }
// // 2nd Step
// let functionName = function (parameter) {
//     //code of block
// }

// 3rd Step
// let functionName = (parameter) => {
//     //code of block
// }

//Function Declaration
//function greet(name){
  //  if (name) {
   //     console. log('Hello' + name);
   // } else{
   //     console.log('Hello Guest');
   // }
// }
// greet('Aisha'); //Prints 'Hello'


//Function Expression
//  let greet = function (name) {
//     if(name) {
//         console. log('Hello' + name);
//     } else{
//         console.log('Hello Guest');
//     }
   
// }
// greet('Aisha'); //Prints 'Hello Aisha'

//Arrow Function
// let greet = (name) => {
    //if(name) {
   //     console. log('Hello' + name);
   // } else{
  //      console.log('Hello Guest');
 //}
   
// }
// greet('Aisha'); //Prints 'Hello Aisha'

function multiply() {
    let Number1 = document.getElementById('Number1').value;
    let Number2 = document.getElementById('Number2').value;
    let result = document.getElementById('Display');

    let Num1 = Number(Number1);
    let Num2 = Number(Number2);
    let output = ""
    result.innerHTML = "";

    for (let a = 0; a <= Num2; a++) {
        let ans =  `${Num1} x ${a} = ${Num1 * a} <br>` ;
        result.innerHTML += ans;   
    }
}



