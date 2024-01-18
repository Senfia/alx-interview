#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${API_URL}/films/${process.argv[2]}/`, async (err, _, body) => {
    if (err) {
      console.error('Error fetching film:', err);
      return;
    }

    try {
      const charactersURL = JSON.parse(body).characters;
      const charactersNamePromises = charactersURL.map(url => fetchCharacterName(url));

      const charactersNames = await Promise.all(charactersNamePromises);
      console.log(charactersNames.join('\n'));
    } catch (error) {
      console.error('Error fetching character names:', error);
    }
  });

  async function fetchCharacterName(url) {
    return new Promise((resolve, reject) => {
      request(url, (err, _, charactersReqBody) => {
        if (err) {
          reject(`Error fetching character details from ${url}: ${err}`);
        } else {
          resolve(JSON.parse(charactersReqBody).name);
        }
      });
    });
  }
} else {
  console.error('Usage: node script.js <film_id>');
}

