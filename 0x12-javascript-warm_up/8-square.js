#!/usr/bin/node
const val = process.argv;
if (parseInt(val[2])) {
  for (let x = 0; x < val[2]; x++) {
    let row = '';
    for (let y = 0; y < val[2]; y++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
