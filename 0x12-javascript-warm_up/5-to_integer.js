#!/usr/bin/node
const val = process.argv;
console.log(Number.parseInt(val[2]) ? `My number: ${val[2]}` : 'Not a number');
