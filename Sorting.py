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
    # Finds the number of digits in the largest number
    largest = nums[0]
    for i in range(1, len(nums)):
        if(nums[i] > largest):
            largest = nums[i]
    count = 0
    if largest == 0:
        count = 1
    while largest != 0:
        largest /= 10
        count += 1
    num_digits = count

    buckets = [][] * 10
    for i in range(0, num_digits):
        # Copy everything from nums into buckets
        for j in range(0, len(nums)):
            digit = (nums[i] // (10 ** i)) % 10
            buckets[digit].append(nums[i])
        # Copy everything from buckets back into nums
        index = 0
        for bucket in range(0, len(buckets)):
            for item in range(0,  len(buckets[bucket])):
                nums[index] = buckets[bucket][item]
                index += 1
            buckets[bucket].clear()


    # print the first and last ten numbers to demonstrate correct sorting
    print("To show that it worked, here are the first ten and last ten numbers:")
    print(nums[:10])
    print("...")
    print(nums[-10:])