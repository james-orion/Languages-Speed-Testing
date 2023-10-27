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
    sort_merge(nums, 0, len(nums)-1)

    # print the first and last ten numbers to demonstrate correct sorting
    print("To show that it worked, here are the first ten and last ten numbers:")
    print(nums[:10])
    print("...")
    print(nums[-10:])

def merge(nums, start_value, center_value, end_value):
    left_end = center_value - start_value + 1
    right_end = end_value - center_value

    #Create temp arrays for the left and right halves
    left_temp = [0] * left_end
    right_temp = [0] * right_end

    # Copy numbers into the temp arrays
    for i in range(0, left_end):
        left_temp[i] = nums[start_value + i]
    for j in range(0, right_end):
        right_temp[i] = nums[center_value + 1 + j]

    # Merge the temp arrays back into nums
    left_index = 0    # first index of left temp array
    right_index = 0    # first index of right temp array
    merged_index = 0    # first index of merged array

    while left_index < left_end and right_index < right_end:
        if left_temp[left_index] <= right_temp[right_index]:
            nums[merged_index] = left_temp[left_index]
            left_index += 1
        else:
            nums[merged_index] = right_temp[right_index]
            right_index += 1
        merged_index += 1

    #Copy the remaining elements of left_temp
    while left_index < left_end:
        nums[merged_index] = left_temp[left_index]
        left_index += 1
        merged_index += 1

    # Copy the remaining elements of right_temp
    while right_index < right_end:
        nums[merged_index] = right_temp[right_index]
        right_index += 1
        merged_index += 1


def sort_merge(nums, start_value, end_value):
    if start_value < end_value:
        center_value = (start_value + (end_value - 1)) // 2

        # Sort first and second halves
        sort_merge(nums, start_value, center_value)
        sort_merge(nums, center_value + 1, end_value)
        merge(nums, start_value, center_value, end_value)
