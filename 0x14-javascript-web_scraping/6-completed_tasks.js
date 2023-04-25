#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (err, response, body) {
  if (!err) {
    const todos = JSON.parse(body);
    let completedTasks = {};
    todos.forEach((todo) => {
      if (todo.completed && completedTasks[todo.userId] === undefined) {
        completedTasks[userId] = 1;
      } else {
        completedTasks[todo.userId] += 1;
      }
    });
    console.log(completedTasks);
  }
});
