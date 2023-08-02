#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const MyFiles = process.argv.slice(2);
request(MyFiles[0], function (error, response, body) {
  if (error) console.error('error:', error);
  else {
    fs.writeFile(MyFiles[1], body, function (err) {
      if (err) console.log(err);
    });
  }
});
