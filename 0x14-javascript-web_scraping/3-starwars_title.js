#!/usr/bin/node
const request = require('request');
const MyFiles = process.argv.slice(2);
let data;
request('https://swapi-api.alx-tools.com/api/films/:id' + MyFiles[0],
  function (error, response, body) {
    if (error) console.error('error:', error);
    else {
      data = JSON.parse(body);
      console.log(data.title);
    }
  });
