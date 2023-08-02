#!/usr/bin/node
const request = require('request');
const MyFiles = process.argv.slice(2);
let data;
let counter = 0;
request(MyFiles[0], function (error, response, body) {
  if (error) console.error('error:', error);
  else {
    data = JSON.parse(body);
    for (const i in data.results) {
      if (data.results[i].characters.filter(x => x.includes('18')).length > 0) { counter++; }
    }
    console.log(counter);
  }
});
