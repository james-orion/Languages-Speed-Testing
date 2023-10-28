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
    for swapIndex in range(0, len(nums)):
        #Loop through starting at swapIndex keeping track of the min
        minIndex = swapIndex
        for i in range(swapIndex, len(nums)):
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

# Radix Sort the vector
def radix_sort(size):
    print("Looking for size " + str(size) + "\n")

    nums = []
    # Read numbers from file
    with open('numbers.txt') as file:
        # Make sure we only read in size integers
        nums = [int(next(file)) for x in range(size)]

    # print vector size to make sure it matches number in previous print statement
    print(f"Vector size: {len(nums)}")

    #Radix sort algorithm
    largest = max(nums)

    # Do a counting sort for every digit, 10^i where i is the current digit number is
    # passed in to the counting sort function
    digit = 1
    while largest // digit > 0:
        counting_sort(nums, digit)
        digit *= 10


    # print the first and last ten numbers to demonstrate correct sorting
    print("To show that it worked, here are the first ten and last ten numbers:")
    print(nums[:10])
    print("...")
    print(nums[-10:])

# Helper method to do counting sort for radix sort
# sorts according to the digit represented by digit
def counting_sort(nums, digit):
    num = len(nums)

    # The sorted output array
    output = [0] * num

    # initializing count array
    count = [0] * 10

    # Stores the count of each occurance in the count array
    for i in range(0, num):
        index = (nums[i]/digit)
        count[int(index%10)] += 1 #increases the count of the number at the digit place by one

    # Update count so it contains the actual position of the digit in the array
    for i in range (1, 10):
        count[i] += count[i-1]

    # Builds the output array
    i = num - 1
    while(i >= 0):
        index = (nums[i]/digit)
        output[count[int((index)%10)] - 1] = nums[i]
        count[int((index)%10)] -= 1
        i -= 1

    # Copies the output array into nums[] so that the array is now sorted
    for j in range(0, len(nums)):
        nums[j] = output[j]
