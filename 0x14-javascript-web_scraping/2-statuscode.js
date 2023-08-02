#!/usr/bin/node
const request = require('request');
const MyFiles = process.argv.slice(2);
request(MyFiles[0], function (error, response, body) {
  if (error) console.error('error:', error);
  console.log('code:', response.statusCode);
});
