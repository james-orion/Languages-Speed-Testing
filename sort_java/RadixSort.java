import java.io.*;
import java.util.Scanner;

public class RadixSort {
	/**
	 * Private helper method to return the max value in the array
	*/
	private static long getMax(long[] nums, int num) {
		long max = nums[0];
		for (int i=0; i < num; i++) {
			if(nums[i] > max) {
				max = nums[i];
			}
		}
		return max;
	}

	/**
	 * Private helper method to counting sort the array based on the digit
	 */
	private static void countingSort(long[] nums, int num, long digit) {
		int[] output = new int[num];
		int[] count = new int[10];
		int i;

		//Store count of occurrences in count
		for(i = 0; i < num; i++) {
			count[(int)(nums[i] / digit) % 10] ++;
		}

		//Update count[i] to contain the actual position of the digit in output
		for (i = 1; i < 10; i++) {
			count[i] += count[i-1];
		}

		//Create the output array
		for(i = num - 1; i >= 0; i--) {
			output[count[(int)(nums[i] / digit) % 10] - 1] = nums[i];
			count[(int)(nums[i] / digit) % 10] --;
		}

		//Copy the output vector to nums so that nums is now sorted according to digit
		for(i = 0; i < num; i++) {
			nums[i] = output[i];
		}
	}

	public static void main(String args[]) throws IOException {
		int size;
		// Get command line input
		if(args.length > 0) {
			size = Integer.parseInt(args[0]);
		} else {
			size = 10000;
		}
		System.out.println("Looking for size: " + size);

		// Create an array of longs to store the numbers
		long[] numbers = new long[size];

		// Read size numbers from numbers.txt
		File nums = new File("numbers.txt");
		Scanner scan = new Scanner(nums);
		long n;
		for(int i=0; i<size; i++) {
			if(scan.hasNext()) {
				n = Long.parseLong(scan.nextLine());
				numbers[i] = n;
			}
		}

		//Radix Sort the array
		long largest = getMax(numbers, numbers.length);

		//Counting sort the vector using 10^i as digit where i is the current place value number
		int digit = 1;
		while (largest / digit > 0) {
			countingSort(numbers, numbers.length, digit);
			digit *= 10;
		}


		//Print the first and last ten numbers from the vector to the console
		for(int k = 0; k < 10; k++) {
			System.out.print(numbers[k] + ", ");
		} 
		System.out.println("...");
		for(int j = numbers.length - 10; j < numbers.length; j++) {
			System.out.print(numbers[j] + ", ");
		}
	}	
}