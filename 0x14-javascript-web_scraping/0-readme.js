#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[1], 'utf8', function (err, data){
  console.log(err || data);
});
