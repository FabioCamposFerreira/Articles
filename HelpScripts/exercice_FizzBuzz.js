// JavaScript (ECMAScript)
// Author: Fábio Campos
// Origin: Eloquent JavaScript
/*
Write a program that uses console.log to print all the numbers from 1 to 100,
with two exceptions. For numbers divisible by 3, print "Fizz" instead of the
number, and for numbers divisible by 5 (and not 3), print "Buzz" instead.
When you have that working, modify your program to print "FizzBuzz" for
numbers that are divisible by both 3 and 5 (and still print "Fizz" or "Buzz"
for numbers divisible by only one of those).
(This is actually an interview question that has been claimed to weed out
a significant percentage of programmer candidates. So if you solved it, your
labor market value just went up.)
*/

// first version
let counter = 0;
do{
    counter++;
    // divisible only by 3
    if(!(counter%3) && (counter%5)){
            console.log("Fizz");
            continue;
    }
    // divisible only by 5
    if ((counter%3) && !(counter%5)){
        console.log("Buzz");
        continue;
    }
    console.log(counter);
}while(counter<100)

// second version
counter = 0;
do{
    counter++;
    // divisible only by 3 and 5
    if(!(counter%3) && !(counter%5)){
        console.log("FizzBuzz");
    }
    // divisible only by 3
    if(!(counter%3) && (counter%5)){
            console.log("Fizz");
            continue;
    }
    // divisible only by 5
    if ((counter%3) && !(counter%5)){
        console.log("Buzz");
        continue;
    }
    console.log(counter);
}while(counter<100)