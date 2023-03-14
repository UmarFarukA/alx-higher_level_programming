#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let h = 0; h < this.height; h++) {
        let row = '';
        for (let w = 0; w < this.width; w++) {
          row += 'C';
        }
        console.log(row);
      }
    }
  }
};
