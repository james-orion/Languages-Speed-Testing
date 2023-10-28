import java.io.*;
import java.util.Scanner;

public class BubbleSort {
	public static void main(String args[]) {
		int size;
		// Get command line input
		if(args.length > 0) {
			size = args[0];
		} else {
			size = 10000;
		}
		System.out.println("Looking for size: " + size);

		// Create an array of longs to store the numbers
		long[] numbers = new long[size];

		// Read size numbers from numbers.txt
		File nums = new File("numbers.txt");
		Scanner scan = new Scanner(nums);
		long num;
		for(int i=0; i<size; i++) {
			if(scan.hasNext()) {
				num = scan.nextLine();
				numbers[i] = num;
			}
		}

		System.out.println(numbers[1]);

	}
}