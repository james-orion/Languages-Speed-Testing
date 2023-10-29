
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
	
		//Bubble sort algorithm 
		let i, numPasses = 0, temp
		let swapped = true;
		while (swapped) {
			swapped = false;
			for (i = 0; i + 1 < nums.length - numPasses ; i++) {
				if(parseInt(nums[i]) > parseInt(nums[i + 1])) {
					//Swap nums[i] and nums[i + 1]
					temp = await nums[i];
					nums[i] = await nums[i+1];
					nums[i+1] = await temp;
					// Update swapped
					swapped = await true;
				}
			}
			await numPasses ++;
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


