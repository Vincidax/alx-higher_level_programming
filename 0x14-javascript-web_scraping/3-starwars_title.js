#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  try {
    if (error) {
      throw new Error(`Request failed: ${error.message}`);
    }

    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    } else {
      throw new Error(`Failed to retrieve movie data. Status code: ${response.statusCode}`);
    }
  } catch (parseError) {
    console.error(`Error parsing JSON: ${parseError.message}`);
  }
});
