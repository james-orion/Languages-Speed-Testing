#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

/**
 * A method that handles the recursive calls to mergeSort
 */
void mergeSortRec(vector<int> &vec, int startIndex, int endIndex);

/**
 * A method that merge sorts a vector
 */
void mergeSort(vector<int> vec);


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

    //Calls the merge sort method on the vector
    mergeSort(numbers);

    // Print the first and last ten numbers from the vector to the console
    for(int i = 0; i < 10; i++) {
        cout << numbers[i] << ", ";
    }
    for(int j = numbers.size() - 10; j < numbers.size(); j++) {
        cout << numbers[j] << ", ";
    }


    return 0;
}


void mergeSortRec(vector<int> &vec, int startIndex, int endIndex) {
    // Recursive base case
    if (startIndex >= endIndex) {
        return;
    }

    // Recursive calls for the left and right halves
    int centerIndex = (startIndex + endIndex) / 2;
    mergeSortRec(vec, startIndex, centerIndex);
    mergeSortRec(vec, centerIndex + 1, endIndex);

    // Merge
    vector<int> temp;
    int leftIndex = startIndex;
    int rightIndex = centerIndex + 1;
    // While leftIndex and rightIndex are in bounds of their half
    while (leftIndex <= centerIndex && rightIndex <= endIndex) {
        if (vec[leftIndex] <= vec[rightIndex]) {
            temp.push_back(vec[leftIndex]);
            ++leftIndex;
        } else {
            temp.push_back(vec[rightIndex]);
            ++rightIndex;
        }
    }
    // Now one of the halves is empty and the other half has at least one element left to copy into temp
    while (leftIndex <= centerIndex) {
        temp.push_back(vec[leftIndex]);
        ++leftIndex;
    }
    while (rightIndex <= endIndex) {
        temp.push_back(vec[rightIndex]);
        ++rightIndex;
    }
    // Now everything between startIndex and endIndex is copied into temp
    // Copy everything from temp back into vec
    for (int i = 0; i < temp.size(); ++i) {
        vec[i + startIndex] = temp[i];
    }
}

void mergeSort(vector<int> vec) {
    mergeSortRec(vec, 0, vec.size() - 1);
}