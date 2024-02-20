#!/usr/bin/node

//import the mode

const fs = require('fs');

//first arg of the file path
const file = process.argv[2];

//second arg is the string to write
const content = process.argv[3];

//write to file
fs.writeFile(file, content, 'utf-8', error => {
	if (error) {
		console.log(error);
	}
});
