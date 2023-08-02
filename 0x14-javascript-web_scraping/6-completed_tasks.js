#!/usr/bin/node
const request = require('request');
const MyFiles = process.argv.slice(2);
let data;
request('https://jsonplaceholder.typicode.com/todos' + MyFiles[0],
const dict = {};
request(MyFiles[0], function (error, response, body) {
  if (error) console.error('error:', error);
  else {
    data = JSON.parse(body);
    for (const i in data) {
      if (data[i].completed === true) {
        if (!(data[i].userId in dict)) { dict[data[i].userId] = 1; } else { dict[data[i].userId] += 1; }
      }
    }
    console.log(dict);
  }
});
