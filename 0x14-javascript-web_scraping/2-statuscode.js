#!/usr/bin/node
const request = require('request');
request.get(process.argv[2]).on('res', function (res) {
  console.log(`code: ${res.statusCode}`);
});
