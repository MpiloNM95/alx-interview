#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

function getMovieCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request.get(url, (error, response, body) => {
    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const charactersUrls = movieData.characters;
      const characters = [];

      for (const charUrl of charactersUrls) {
        request.get(charUrl, (error, response, body) => {
          if (response.statusCode === 200) {
            const characterData = JSON.parse(body);
            characters.push(characterData.name);
            if (characters.length === charactersUrls.length) {
              printCharacters(characters);
            }
          } else {
            console.log(`Error: ${response.statusCode}`);
          }
        });
      }
    } else {
      console.log(`Error: ${response.statusCode}`);
    }
  });
}

function printCharacters(characters) {
  for (const character of characters) {
    console.log(character);
  }
}

if (movieId) {
  getMovieCharacters(movieId);
} else {
  console.log('Usage: node star_wars_characters.js [Movie ID]');
}
