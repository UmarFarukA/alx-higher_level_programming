#!/usr/bin/node
const request = require('request');
url = 'https://swapi-api.alx-tools.com/api/films';
request.get(url, function (err, response, body) {
  if (!err) {
    const results = JSON.parse(body).results;
    const result = results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/');
    }
    console.log(result ? 
  }
});
