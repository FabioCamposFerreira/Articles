// JavaScript (ECMAScript)
// Author: Fábio Campos


// The JavaScript values are numbers, strings, booleans and empty


// Numbers
var number = -1.99;
console.log("number = "+number);
number= 2.99e10;                              // Exponent notacion
console.log("number = "+number);
number = Infinity;
number = -Infinity;
number = NaN;                                 // "not a number"
console.log("number = "+number);
console.log("2+3 = "+(2+3));                  // Sum
console.log("2++ = "+(2++));                  // Equal to 2+1
console.log("number += "+(number+=10));       // Equal to number = number +10
console.log("2-3 = "+(2-3));                  // Diferen
console.log("2-- = "+(2--));                  // Equal to 211
console.log("number -= 10 = "+(number-=10));  // Equal to number = number -10
console.log("2*3 = "+(2*3));                  // Multiplication
console.log("number *= 10 = "+(number*=10));  // Equal to number = number * 10
console.log("2/3 = "+(2/3));                  // Division
console.log("number /= 10 = "+(number/=10));  // Equal to number = number / 10
console.log("4%3 = "+(4%3));                  // Rest of the division (modulo)
console.log("number %= 2 = "+(number%=2));    // Equal to number = number % 2


// Strings
var text = "This is a string!";
console.log("text = "+text);
console.log("Firts,"+text+", ok?");     // Concatenation
console.log("2+3 is equal to ${2+3}");  // template literals
console.log(text.length);               // Number of caracthers


// Booleans
var bool = true;
var bool = false;
console.log("bool = "+bool);
console.log("1 < 2 ="+ 1 < 2);                          // "is less than"
console.log("1 > 2 ="+ 1 > 2);                          // "is greater than"
console.log("1 >= 2 ="+ 1 >= 2);                        // greater than or equal to
console.log("1 <= 2 ="+ 1 <= 2);                        // less than or equal to
console.log("1 == \"2\" ="+ 1 == "2");                  // equal to
console.log("1 === \"2\" ="+ 1 === "2");                // equal to and same type
console.log("1 != \"1\" ="+ 1 != "1");                  // not equal to
console.log("1 !== \"1\" ="+ 1 !== "1");                // not equal to and not same type
console.log("true && false ="+ true && false);          // operator "and"
console.log("true || false ="+ true || false);          // operator "or"
console.log("!true ="+ !true);                          // operator "Not"
console.log("false ? 123 : 456 ="+ false ? 123 : 456);  // operator (conditional)

// Arrays