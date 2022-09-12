// JavaScript (ECMAScript)
// Author: Fábio Campos


// Get type of variable
var variable = -1.99;
console.log(typeof(variable));
//Output


// Conversion variable type
console.log(Number("123"))     // to number
console.log(String(123))       // to string
console.log(Boolean("false"))  // to bool


// Breaking out of a Loop
for(let i=0;i<11; i=i+1){
    console.log("Now, i = "+i);
    if(i===2){
        break;
    }
}


// Jump interations in the Loop
for(let i=0;i<11; i=i+1){
    if(i%2===0){
        continue;
    }
    console.log("Now, i = "+i);
}

// Sort list