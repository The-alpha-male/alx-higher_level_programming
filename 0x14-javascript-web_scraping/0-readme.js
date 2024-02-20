#!/usr/bin/node

//import the module
const fs = require('fs');

// first arg is file path
const file = process.argv[2];

//read the files
fs.readFile(file, 'utf-8', (error, data) => {
	if (error) {
		console.error('Error reading the file:', error);
		return;
	}
	console.log(data);
});
