#!/usr/bin/node
const request = require('request');
const response = request.get(process.argv[2]);
console.log(`code: ${response.statusCode}`);
