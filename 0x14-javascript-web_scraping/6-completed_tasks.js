#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Request failed: ${error.message}`);
    return;
  }

  if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const completedTasks = tasks.reduce((result, task) => {
      if (task.completed) {
        result[task.userId] = (result[task.userId] || 0) + 1;
      }
      return result;
    }, {});

    console.log(completedTasks);
  } else {
    console.error(`Failed to retrieve tasks data. Status code: ${response.statusCode}`);
  }
});
