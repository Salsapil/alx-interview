#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;

    // Fetch character names in order
    const fetchCharacter = (index) => {
      if (index >= characters.length) return;

      request(characters[index], (err, res, characterBody) => {
        if (!err && res.statusCode === 200) {
          console.log(JSON.parse(characterBody).name);
          fetchCharacter(index + 1); // Recursive call to ensure order
        }
      });
    };

    fetchCharacter(0); // Start fetching from the first character
  } else {
    console.log('Error:', error);
  }
});
