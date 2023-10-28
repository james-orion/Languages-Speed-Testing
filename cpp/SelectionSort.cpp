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

    //Selection Sort the vector
    int swapIndex, i, minIndex;
    long temp;
    for (swapIndex = 0; swapIndex < numbers.size()-1; ++swapIndex) {
        // Loop through vector starting at swapIndex and keep track of min
        minIndex = swapIndex;
        for (i = swapIndex+1; i < numbers.size(); ++i) {
            if (numbers[i] < numbers[minIndex]) {
                // We have a new minimum
                minIndex = i;
            }
        }
        // Swap min value into swapIndex spot in vector
        temp = numbers[swapIndex];
        numbers[swapIndex] = numbers[minIndex];
        numbers[minIndex] = temp;
    }

    // print the first and last ten numbers from the vector to the console
    for(int i = 0; i < 10; i++) {
        cout << numbers[i] << ", ";
    }
    for(int j = numbers.size() - 10; j < numbers.size(); j++) {
        cout << numbers[j] << ", ";
    }
    return 0;
}