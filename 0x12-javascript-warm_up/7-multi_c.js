#!/usr/bin/node
const val = process.argv;
if (parseInt(val[2])) {
  for (let x = 0; x < val[2]; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
