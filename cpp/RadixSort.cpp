#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;


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
    
    //Finds the largest number and it's number of digits
    int largest = numbers[0];
    for(int i=1; i<numbers.size(); i++) {
        if (numbers[i] > largest) {
            largest = number[i];
        }
    }
    int numDigits, count;
    if(largest == 0) {
        count = 1;
    }
    while (largest!=0) {
        largest = largest / 10;
        count ++;
    }
    numDigits = count;

    //Sort the vector
    int iteration, i, digit, bucket, item;
    vector<vector<int>> buckets(10);
    for (iteration = 0; iteration < numDigits; ++iteration) {
        // Copy everything from numbers into buckets
        for (i = 0; i < numbers.size(); ++i) {
            digit = (numbers[i] / int(pow(10, iteration)) % 10);
            buckets[digit].push_back(numbers[i]);
        }
        // Copy everything from buckets back into numbers
        i = 0;
        for (bucket = 0; bucket < buckets.size(); ++bucket) {
            for (item = 0; item < buckets[bucket].size(); ++item) {
                numbers[i] = buckets[bucket][item];
                i++;
            }
            buckets[bucket].clear();
        }
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
