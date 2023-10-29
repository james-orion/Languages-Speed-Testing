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

//Helper method to return the max value in the array
const getMax = async (nums, num) => {
	try {
		max = nums[0];
		for (let i = 0; i < num; i++) {
			if(parseInt(nums[i]) > parseInt(max)) {
				max = await nums[i];
			}
		}
		return max;

	} catch (e) {
		console.log(e);
	}
}

//Helper method to counting sort based on the digit
const countingSort = async (nums, num, digit) => {
	try {
		var output = await [num];
		var count = await [10];
		var i;

		//Store count of occurrences in count
		for(i = 0; i < num; i++) {
			await count[(parseInt(nums[i]) / digit) % 10] ++;
		}

		// Update count[i] to contain the actual position of the digit in output
		for(i = 1; i < 10; i++) {
			count[i] += await count[i-1];
		}

		//Create the output array
		for(i = num - 1; i >= 0; i--) {
			output[count[(parseInt(nums[i]) / digit) % 10] - 1] = await nums[i];
			await count[(parseInt(nums[i]) / digit) % 10] --;
		}

		//Copy the output array to nums so that nums is sorted according to digit
		for(i = 0; i < num; i++) {
			nums[i] = await output[i];
		}

		return nums;
	}
	catch(e) {
		console.log(e);
	}
}

//A function to bubble sort the numbers
const sort = async (numbers) => {
	try {
		// Get the numbers from the file
		var nums = await getNums(numbers);
	
		//Radix Sorts the vector
		var largest = await getMax(numbers, number.length);

		//Counting sorts the vector using 10^i as the digit where i is the current place value digit
		var digit = 1;
		var numsSorted;
		while (largest/digit > 0) {
			numsSorted = await countingSort(nums, nums.length, digit);
			digit *= await 10;
		}
		
		await print(numsSorted);

		return numsSorted;
	}
	catch (e) {
		console.log(e);
	}
}

// Calls the sort method
sort(numbers);