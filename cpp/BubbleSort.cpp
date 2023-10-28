#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
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
    
    // Bubble Sort the vector - code taken from CS 124 Project 4
    int numPasses = 0, i;
    long temp;
    bool haveSwapped = true;
    while (haveSwapped) {
        haveSwapped = false;
        for (i = 0; i+1 < numbers.size()-numPasses; ++i) {
            // Compare items at indices i and i+1 and swap if necessary
            if (numbers[i] > numbers[i+1]) {
                temp = numbers[i];
                numbers[i] = numbers[i+1];
                numbers[i+1] = temp;
                // Update haveSwapped
                haveSwapped = true;
            }
        }
        ++numPasses;
    }
    
    // Print the first and last ten numbers from the vector to the console
    for(int i = 0; i < 10; i++) {
        cout << numbers[i] << ", ";
    }
    cout << "..." << endl;
    for(int j = numbers.size() - 10; j < numbers.size(); j++) {
        cout << numbers[j] << ", ";
    }
    return 0;
}
