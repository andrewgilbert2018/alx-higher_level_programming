#!/usr/bin/node
// a script that print a message depending of the number of arguments passed
const count = process.argv.length;
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
