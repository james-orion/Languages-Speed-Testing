
var size;
//Get command line input
var arguments = process.argv; 
if(arguments.length > 0) {
	size = parseInt(arguments[2]);
} else {
	size = 10000;
}
console.log("Looking for size: ", size);

//Create an array to store the numbers
var numbers = [];

//Code taken from 
const { open } = require('node:fs/promises');

//A function to get size numbers from the file
const getNums = async (numbers) => {
	try {
		let i = 0;

		const file = await open('numbers.txt');
	
		for await (const line of file.readLines()) {
			if (i < size) {
				numbers.push(line);
				i ++;
			}
		}
		return numbers;
	}
	catch (e) {
		//Display the error
		console.log(e);
	}	
}

//A function to print the first 10 and last 10 numbers from the file
const print = async (numbers) => {
	try {
		// Print the first and last ten numbers from the vector to the console
		for (let i = 0; i < 10; i ++) {
			console.log(numbers[i]);
		}
		console.log("...")
		for (let j = numbers.length - 10; j < numbers.length; j++) {
			console.log(numbers[j]);
		}
	}
	catch (e) {
		console.log (e);
	}
}

//A function to bubble sort the numbers
const sort = async (numbers) => {
	try {
		// Get the numbers from the file
		var nums = await getNums(numbers);
	
		//Selection sort algorithm 
		var i, swapIndex, min;
		var temp;

		for(swapIndex = 0; swapIndex < nums.length - 1; swapIndex++) {
			//Loop through the array starting at swapIndex and keeps track of the minimum
			min = await swapIndex;
			for (i = swapIndex + 1; i < nums.length; i++) {
				if(parseInt(nums[i]) < parseInt(nums[min])) {
					//We have a new minimum
					min = await i;
				}
			}
			//Swap min value into swapIndex spot in vector
			temp = await nums[swapIndex];
			nums[swapIndex] = await nums[min];
			nums[min] = await temp;
		}
		
		await print(nums);

		return nums;
	}
	catch (e) {
		console.log(e);
	}
}

// Calls the sort method
sort(numbers);