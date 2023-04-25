#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request.get(process.argv[2], function (err, response, body) {
  fs.createWriteStream(process.argv[3]);
});
