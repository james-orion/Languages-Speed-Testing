import matplotlib.pyplot as plt
import os
import platform
import subprocess
from subprocess import Popen, PIPE, check_output
import time
from Sorting import *

# Flags to determine which part of the file to run and how much to print to the console
debug = True
# TODO: Change these to True when you are ready to run the Python and C++ simulations
runPython = True
runCpp = True
runJava = False

# Create empty lists that will store the bubble sort runtimes
pythonTimes = []
cppTimes = []
javaTimes = []

# Python sorting
if runPython:
    # Sort 1000, 2000, 3000, ..., 10000 integers
    for size in range(1000, 10001, 1000):
        # If debug is true, print statement to show where you are in the program
        if debug:
            print(f"Let's see how long it takes Python to bubble sort {size} random integers from a file!")

        # Start the clock
        tic = time.time()

        #Calls the bubble sort function from the other file
        bubble_sort(size)

        # End clock
        toc = time.time()

        # If debug is true, print the time it took Python to sort the integers
        if debug:
            print(f"Python Bubble Sort finished in {(toc - tic):0.6f} seconds")
        
        # Add the runtime to the list
        pythonTimes.append(toc-tic)

    # If debug is true, after all test runs, print the list of Python runtimes
    if debug:
        print("Python times:")
        print(pythonTimes)

# C++ sorting
if runCpp:
    # Sort 1000, 2000, 3000, ..., 10000 integers
    for size in range(1000, 10001, 1000):
        # If debug is true, print statement to show where you are in the program
        if debug:
             print(f"Let's see how long it takes C++ to bubble sort {size} random integers from a file!")
        # Start the clock
        tic = time.time()
        try:
            # This is Python's way of calling the command line. We use it to compile the C++ files.
            subprocess.check_output("g++ -std=c++17 Sorting.cpp",stdin=None,stderr=subprocess.STDOUT,shell=True)
        except subprocess.CalledProcessError as e:
            # There were compiler errors in Sorting.cpp. Print out the error message and exit the program.
            print("<p>",e.output,"</p>")
            raise SystemExit

        # Depending on your OS, different executable files will be produced. Run the executable.
        if platform.system() == 'Windows':
            p = Popen('a.exe '+str(size), shell=True, stdout=PIPE, stdin=PIPE)
            # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting
            if debug:
                print(p.stdout.read().decode('utf-8'))
            os.remove("a.exe")
        else: # Mac and Linux case
            p = Popen(['./a.out '+str(size)], shell=True, stdout=PIPE, stdin=PIPE)
            # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting
            if debug:
                print(p.stdout.read().decode('utf-8'))
            os.remove("a.out")
        
        # End clock
        toc = time.time()

        # If debug is true, print the time it took C++ to sort the integers
        if debug:
            print(f"C++ Bubble Sort finished in {(toc - tic):0.6f} seconds")

        # Add the runtime to the list
        cppTimes.append(toc-tic)

    # If debug is true, after all test runs, print the list of C++ runtimes
    if debug:
        print("C++ times:")
        print(cppTimes)

    #TODO: use the selection sort method

    #TODO: use the merge sort method 

#TODO: call the java program and sort the numbers

# Graph the results

# Create a list of the sizes to use for the x axis tick marks
sizes = range(1000, 10001, 1000)
# Create lists that are offset so the Python bars aren't overlapping with C++ bars in the graph
pythonX = range(850, 10001, 1000)
cppX = range(1150, 10501, 1000)
# Create a graph plot with one (1) row and one (1) column.
# The third 1 signals to start at the first subplot (aka subplot 1 out of 1)
ax = plt.subplot(111)
# If not all of the data has been collected, use dummy data
if len(pythonTimes) < 10 or len(cppTimes) < 10:
    # Plot the dummy values in blue
    ax.bar(sizes, range(1, 11), width=300, color='b', align='center')
else:
    # Plot the Python bars in red
    ax.bar(sizes, pythonTimes, width=200, color='r', align='edge')
    # Plot the C++ bars in yellow
    ax.bar(sizes, cppTimes, width=200, color='y', align='center')
# Set the window title
plt.gcf().canvas.manager.set_window_title('Speed Test')
# Set the graph title
plt.title('Python vs. C++')
# Label the x axis
plt.xlabel('Number of integers to sort')
# Make sure the x-axis tick marks/labels are at each 1000
plt.xticks(sizes)
# Label the y axis
plt.ylabel('Times in seconds (Python in red, C++ in yellow)')
# Save the graph to a file
plt.savefig('BattleOfTheBubbleSorts.png')
# Display the graph in a new window
plt.show()


