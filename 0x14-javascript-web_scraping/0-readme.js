#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

// Check if the file path argument is provided
if (!filePath) {
  console.error('Usage: ./0-readme.js <file-path>');
  process.exit(1);
}

// Read the content of the file in utf-8
fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
