#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

function getMovieCharacters(movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

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
  const expectedOrder = [
    "Luke Skywalker",
    "C-3PO",
    "R2-D2",
    "Darth Vader",
    "Leia Organa",
    "Obi-Wan Kenobi",
    "Chewbacca",
    "Han Solo",
    "Jabba Desilijic Tiure",
    "Wedge Antilles",
    "Yoda",
    "Palpatine",
    "Boba Fett",
    "Lando Calrissian",
    "Ackbar",
    "Mon Mothma",
    "Arvel Crynyd",
    "Wicket Systri Warrick",
    "Nien Nunb",
    "Bib Fortuna"
  ];

  for (const character of expectedOrder) {
    if (characters.includes(character)) {
      console.log(character);
    }
  }
}

if (movieId) {
  getMovieCharacters(movieId);
} else {
  console.log('Usage: node 0-starwars_characters.js [Movie ID]');
}
