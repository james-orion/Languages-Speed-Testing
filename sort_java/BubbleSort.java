import java.io.*;
import java.util.Scanner;

public class BubbleSort {
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

		// Bubble sort algorithm
		int numPasses = 0, i;
		long temp;
		boolean haveSwapped = true;
		while(haveSwapped) {
			haveSwapped = false;
			for(i = 0; i+1 < numbers.length - numPasses; i++) {
				//Compare items at indices i and i+1 and swap if necessary
				if (numbers[i] > numbers[i+1]) {
					temp = numbers[i];
					numbers[i] = numbers[i+1];
					numbers[i+1] = temp;
					//Update haveSwapped
					haveSwapped = true;
				}
			}
			++numPasses;
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