#!/usr/bin/node
// a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer
const num = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
