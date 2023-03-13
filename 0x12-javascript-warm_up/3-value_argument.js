#!/usr/bin/node
const val = process.argv;
console.log(typeof val[2] === 'undefined' ? 'No argument' : val[2]);
