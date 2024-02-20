#!/usr/bin/node

//import the module
const request = require('request');

//first argument is the API URL
const ApiUrl = process.argv[2];

const dictionary = {};

//make HTTP GET request to API URL
request(ApiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    data.forEach(function (result) {
      if (result.completed === true) {
        const userid = result.userId;
        if (!(userid in dictionary)) {
          dictionary[userid] = 0;
        }
        dictionary[userid] += 1;
      }
    });
    console.log(dictionary);
  }
});
