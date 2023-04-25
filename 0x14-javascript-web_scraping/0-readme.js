#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[1], 'utf-8', function (err, data)
  console.log(data || err);
});
