#!/usr/bin/node
// a script that prints the addition of 2 integers
function add (a, b) {
  return a + b;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
