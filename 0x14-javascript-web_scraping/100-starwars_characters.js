#!/usr/bin/node
const request = require('request');
const MyFiles = process.argv.slice(2);
let data;
request('https://swapi-api.hbtn.io/api/films/' + MyFiles[0],
  function (error, response, body) {
    if (error) console.error('error:', error);
    else {
      data = JSON.parse(body);
      for (const i in data.characters) {
        let charname;
        request(data.characters[i], function (error, response, body) {
          if (error) console.error('error:', error);
          else {
            charname = JSON.parse(body);
            console.log(charname.name);
          }
        });
      }
    }
  });
