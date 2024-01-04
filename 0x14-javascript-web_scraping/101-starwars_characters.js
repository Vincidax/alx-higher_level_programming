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
      const characterUrls = movieData.characters;

      // Function to fetch and print character name for a given URL
      const printCharacterName = async (characterUrl) => {
        const characterResponse = await new Promise((resolve) => {
          request(characterUrl, (err, res, characterBody) => {
            resolve(characterBody);
          });
        });

        const characterData = JSON.parse(characterResponse);
        console.log(characterData.name);
      };

      // Using async/await to ensure characters are printed in order
      (async () => {
        for (const characterUrl of characterUrls) {
          await printCharacterName(characterUrl);
        }
      })();
    } else {
      throw new Error(`Failed to retrieve movie data. Status code: ${response.statusCode}`);
    }
  } catch (parseError) {
    console.error(`Error: ${parseError.message}`);
  }
});
