#!/usr/bin/node
const request = require('request');
const url = 'http https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(url, function (err, response, data) {
  const characters = JSON.parse(body).characters;
  characters.forEach((character) => {
    request(character, function (err, response, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
  });
});