#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, function (err, response, body) {
  if (!err) {
    const todos = JSON.parse(body);
    const completedTasks = {};
    todos.forEach((todo) => {
      if (todo.completed && completedTasks[todo.userId] === undefined) {
        completedTasks[todo.userId] = 1;
      } else if (todo.completed) {
        completedTasks[todo.userId] += 1;
      }
    });
    console.log(completedTasks);
  }
});
