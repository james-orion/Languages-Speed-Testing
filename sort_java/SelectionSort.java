import java.io.*;
import java.util.Scanner;

public class SelectionSort {
	public static void main(String[] args) throws IOException {
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

		System.out.println("Looking for size: " + size);

		//Selection Sort algorithm
		int swapIndex, i, minIndex;
		long temp;
		for(swapIndex = 0; swapIndex < numbers.length - 1; swapIndex++) {
			// Loop through the array starting at swapIndex and keep track of min
			minIndex = swapIndex;
			for(i = swapIndex+1; i < numbers.length; i++) {
				if(numbers[i] < numbers[minIndex]) {
					// We have a new minimum
					minIndex = i;
				}
			}
			//Swap min value into swapIndex spot in vector
			temp = numbers[swapIndex];
			numbers[swapIndex] = numbers[minIndex];
			numbers[minIndex] = temp;
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