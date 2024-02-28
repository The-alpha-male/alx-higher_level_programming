// select the element
const element = document.querySelector('header');

// check id element was found
if (element) {
	// set color
	element.style.color = '#FF0000';
} else {
	console.error('Heaser element not found');
}
