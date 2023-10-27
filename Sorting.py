def bubble_sort(size):
    print("Looking for size " + str(size) +"\n")

    nums = []
    # Read numbers from file
    with open('numbers.txt') as file:
        # Make sure we only read in size integers
        nums = [int(next(file)) for x in range(size)]

    # print vector size to make sure it matches number in previous print statement
    print(f"Vector size: {len(nums)}")

    # Bubble sort algorithm
    haveSwapped = True
    maxIndex = len(nums) - 1
    while haveSwapped:
        haveSwapped = False
        for i in range(maxIndex):
            if nums[i+1] < nums[i]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                haveSwapped = True
        maxIndex -= 1
            
    # print the first and last ten numbers to demonstrate correct sorting
    print("To show that it worked, here are the first ten and last ten numbers:")
    print(nums[:10])
    print("...")
    print(nums[-10:])

# Selection Sort the vector
def selection_sort(size):
    print("Looking for size " + str(size) + "\n")

    nums = []
    # Read numbers from file
    with open('numbers.txt') as file:
        # Make sure we only read in size integers
        nums = [int(next(file)) for x in range(size)]

    # print vector size to make sure it matches number in previous print statement
    print(f"Vector size: {len(nums)}")

    #Selection sort algorithm
    for swapIndex in range(len(nums)):
        #Loop through starting at swapIndex keeping track of the min
        minIndex = swapIndex
        for i in range(len(nums)):
            if(nums[i] < nums[minIndex]):
                #there is a new minimum value
                minIndex = i

        #Swap minIndex and swapIndex
        temp = nums[swapIndex]
        nums[swapIndex] = nums[minIndex]
        nums[minIndex] = temp

    # print the first and last ten numbers to demonstrate correct sorting
    print("To show that it worked, here are the first ten and last ten numbers:")
    print(nums[:10])
    print("...")
    print(nums[-10:])


# Merge sort the vector
def merge_sort(size):
    print("Looking for size " + str(size) + "\n")

    nums = []
    # Read numbers from file
    with open('numbers.txt') as file:
        # Make sure we only read in size integers
        nums = [int(next(file)) for x in range(size)]

    # print vector size to make sure it matches number in previous print statement
    print(f"Vector size: {len(nums)}")

    # Calls the recursive merge sort function
    merge_sort_rec(nums, 0, len(nums)-1)

    # print the first and last ten numbers to demonstrate correct sorting
    print("To show that it worked, here are the first ten and last ten numbers:")
    print(nums[:10])
    print("...")
    print(nums[-10:])


def merge_sort_rec(nums, start_value, end_value):
    #If the array still needs to be further split
    if (end_value > start_value):
        #Creates new arrays representing the two halves
        center_value = len(nums)//2 #// operator does integer division
        left = nums[start_value:center_value]
        right = nums[center_value:end_value]

        #Recursively sorts the two halves
        merge_sort_rec(left, start_value, center_value)
        merge_sort_rec(right, center_value, end_value)

    # Merge
    temp = []
    left_index = start_value
    right_index = center_value + 1
    # While both left_index and right_index are in bounds
    while(left_index <= center_value && right_index <= end_value):
        if(nums[left_index] <= nums[right_index]):
            temp.append(nums[left_index])
            left_index = left_index + 1
        else:
            temp.append(nums[right_index])
            right_index = right_index + 1
    
    #One of the halves is empty and the other has at least one element
    while (left_index <= center_value):
        temp.append(nums[left_index])
        left_index = left_index + 1
    while (right_index <= end_value):
        temp.append(nums[right_index])
        right_index = right_index + 1

    # Now all values have been copied into temp
    # We need to copy everything back into nums
    for i in range (len(temp)):
        nums[i + start_value] = temp [i]


