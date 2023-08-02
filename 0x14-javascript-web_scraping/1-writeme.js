#!/usr/bin/node
const fs = require('fs');
const MyFiles = process.argv.slice(2);
fs.writeFile(MyFiles[0], MyFiles[1], function (err) {
  if (err) console.log('error', err);
});
