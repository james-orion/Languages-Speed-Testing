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

		System.out.println(numbers[1]);

	}
}