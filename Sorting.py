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

#TODO: Selection Sort the vector
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


#TODO: Merge sort the vector

#TODO: print the first and last ten numbers from the vector to the console
