#!/usr/bin/node
// a function that converts a number from base 10 to another base passed as argumen
exports.converter = function (base) { return num => num.toString(base); };
