#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

/**
 * Helper method to return the max number in the vector
 */
int getMax(vector<long> nums, int num);

/**
 * Helper method to counting sort the vector based on the digit, like in the python implementation
 */
void countingSort(vector<long> nums, int num, int digit);

int main(int argc, char* argv[]) {
    int size;
    // Get command line input
    if (argc > 1) {
        size = stoi(argv[1]);
    } else {
        size = 10000;
    }
    cout << "Looking for size: " << size << endl;
    
    // Declare a vector of longs to store the numbers
    vector<long> numbers;
    
    // Read size numbers from numbers.txt
    ifstream inFile;
    inFile.open("numbers.txt");
    long num;
    for(int i=0; i<size; ++i) {
        if(inFile) {
            inFile >> num;
            numbers.push_back(num);
        }
    }
    
    // Print the vector size (to make sure it matches the size printed above)
    cout << "The vector has a size of " << numbers.size() << endl;

    //Radix sorts the vector
    int largest = getMax(numbers, numbers.size());

    // Counting sort the vector using 10^i as digit where i is the current place value number
    int digit = 1;
    while (largest / digit > 0) {
        countingSort(numbers, numbers.size(), digit);
        digit *= 10;
    }

    // Print the first and last ten numbers from the vector to the console
    for(int i = 0; i < 10; i++) {
        cout << numbers[i] << ", ";
    }
    for(int j = numbers.size() - 10; j < numbers.size(); j++) {
        cout << numbers[j] << ", ";
    }


    return 0;
}

int getMax(vector<long> nums, int num) {
    int max = nums[0];
    for (int i = 1; i < num; i++) {
        if (nums[i] > max) {
            max = nums[i];
        }
    }
    return max;
}

void countingSort(vector<long> nums, int num, int digit) {
    vector<int> output(num);
    vector<int> count(10);
    int i;

    // Store count of occurrences in count
    for(i = 0; i < num; i++) {
        count[(nums[i] / digit) % 10] ++;
    }

    // Update count[i] to contain the actual position of the digit in output
    for (i = 1; i < 10; i++) {
        count[i] += count[i-1];
    }

    // Create the output vector
    for (i = num - 1; i >= 0; i--) {
        output[count[(nums[i] / digit) % 10] - 1] = nums[i];
        count[(nums[i] / digit) % 10] --;
    }

    // Copy the output vector to nums so that nums is now sorted according to digit
    for(i = 0; i < num; i++) {
        nums[i] = output[i];
    }
}