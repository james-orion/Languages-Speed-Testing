import matplotlib.pyplot as plt
import os
import platform
import subprocess
from subprocess import Popen, PIPE, check_output
import time
from Sorting import *

# Flags to determine which part of the file to run and how much to print to the console
debug = True
# Change these to True when you are ready to run the Python and C++ simulations
runPython = False
runCpp = False
runJava = False
runJS = True

# Create empty lists that will store the bubble sort runtimes
pythonBubbleTimes = []
pythonSelectionTimes = []
pythonRadixTimes = []

cppBubbleTimes = []
cppSelectionTimes = []
cppRadixTimes = []

javaBubbleTimes = []
javaSelectionTimes = []
javaRadixTimes = []

jsBubbleTimes = []
jsSelectionTimes = []
jsRadixTimes = []

# Python sorting
if runPython:
    # Bubble Sort 1000, 2000, 3000, ..., 10000 integers
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
        pythonBubbleTimes.append(toc-tic)

    # If debug is true, after all test runs, print the list of Python runtimes
    if debug:
        print("Python bubble times:")
        print(pythonBubbleTimes)

    # Selection Sort 1000, 2000, 3000, ..., 10000 integers
    for size in range(1000, 10001, 1000):
        # If debug is true, print statement to show where you are in the program
        if debug:
            print(f"Let's see how long it takes Python to selection sort {size} random integers from a file!")

        # Start the clock
        tic = time.time()

        #Calls the bubble sort function from the other file
        selection_sort(size)

        # End clock
        toc = time.time()

        # If debug is true, print the time it took Python to sort the integers
        if debug:
            print(f"Python Selection Sort finished in {(toc - tic):0.6f} seconds")
        
        # Add the runtime to the list
        pythonSelectionTimes.append(toc-tic)

    # If debug is true, after all test runs, print the list of Python runtimes
    if debug:
        print("Python selection times:")
        print(pythonSelectionTimes)


    # Radix Sort 1000, 2000, 3000, ..., 10000 integers
    for size in range(1000, 10001, 1000):
        # If debug is true, print statement to show where you are in the program
        if debug:
            print(f"Let's see how long it takes Python to radix sort {size} random integers from a file!")

        # Start the clock
        tic = time.time()

        #Calls the bubble sort function from the other file
        radix_sort(size)

        # End clock
        toc = time.time()

        # If debug is true, print the time it took Python to sort the integers
        if debug:
            print(f"Python Radix Sort finished in {(toc - tic):0.6f} seconds")
        
        # Add the runtime to the list
        pythonRadixTimes.append(toc-tic)

    # If debug is true, after all test runs, print the list of Python runtimes
    if debug:
        print("Python radix times:")
        print(pythonRadixTimes)


# C++ sorting
if runCpp:
    # Bubble Sort 1000, 2000, 3000, ..., 10000 integers
    for size in range(1000, 10001, 1000):
        # If debug is true, print statement to show where you are in the program
        if debug:
             print(f"Let's see how long it takes C++ to bubble sort {size} random integers from a file!")
        # Start the clock
        tic = time.time()
        try:
            # This is Python's way of calling the command line. We use it to compile the C++ files.
            subprocess.check_output("g++ -std=c++17 cpp/BubbleSort.cpp",stdin=None,stderr=subprocess.STDOUT,shell=True)
        except subprocess.CalledProcessError as e:
            # There were compiler errors in BubbleSort.cpp. Print out the error message and exit the program.
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
        cppBubbleTimes.append(toc-tic)

    # If debug is true, after all test runs, print the list of C++ runtimes
    if debug:
        print("C++ bubble times:")
        print(cppBubbleTimes)

    
    # Selection Sort 1000, 2000, 3000, ..., 10000 integers
    for size in range(1000, 10001, 1000):
        # If debug is true, print statement to show where you are in the program
        if debug:
             print(f"Let's see how long it takes C++ to selection sort {size} random integers from a file!")
        # Start the clock
        tic = time.time()
        try:
            # This is Python's way of calling the command line. We use it to compile the C++ files.
            subprocess.check_output("g++ -std=c++17 cpp/SelectionSort.cpp",stdin=None,stderr=subprocess.STDOUT,shell=True)
        except subprocess.CalledProcessError as e:
            # There were compiler errors in SelectionSort.cpp. Print out the error message and exit the program.
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
            print(f"C++ Selection Sort finished in {(toc - tic):0.6f} seconds")

        # Add the runtime to the list
        cppSelectionTimes.append(toc-tic)

    # If debug is true, after all test runs, print the list of C++ runtimes
    if debug:
        print("C++ selection times:")
        print(cppSelectionTimes)
   

    # Radix Sort 1000, 2000, 3000, ..., 10000 integers
    for size in range(1000, 10001, 1000):
        # If debug is true, print statement to show where you are in the program
        if debug:
             print(f"Let's see how long it takes C++ to radix sort {size} random integers from a file!")
        # Start the clock
        tic = time.time()
        try:
            # This is Python's way of calling the command line. We use it to compile the C++ files.
            subprocess.check_output("g++ -std=c++17 cpp/RadixSort.cpp",stdin=None,stderr=subprocess.STDOUT,shell=True)
        except subprocess.CalledProcessError as e:
            # There were compiler errors in RadixSort.cpp. Print out the error message and exit the program.
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
            print(f"C++ Radix Sort finished in {(toc - tic):0.6f} seconds")

        # Add the runtime to the list
        cppRadixTimes.append(toc-tic)

    # If debug is true, after all test runs, print the list of C++ runtimes
    if debug:
        print("C++ radix times:")
        print(cppRadixTimes)

# Java sorting
if runJava:
    # Bubble Sort 1000, 2000, 3000, ..., 10000 integers
    for size in range(1000, 10001, 1000):
        # If debug is true, print statement to show where you are in the program
        if debug:
             print(f"Let's see how long it takes java to bubble sort {size} random integers from a file!")
        # Start the clock
        tic = time.time()
        try:
            # This is Python's way of calling the command line. We use it to compile the Java files.
            subprocess.check_output("javac sort_java/BubbleSort.java",stdin=None,stderr=subprocess.STDOUT,shell=True)
        except subprocess.CalledProcessError as e:
            # There were compiler errors in BubbleSort.java. Print out the error message and exit the program.
            print("<p>",e.output,"</p>")
            raise SystemExit

        # Executes the java file
        p = Popen('java sort_java/BubbleSort.java '+str(size), shell=True, stdout=PIPE, stdin=PIPE)
        # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting
        if debug:
            print(p.stdout.read().decode('utf-8'))
        
        # End clock
        toc = time.time()

        # If debug is true, print the time it took C++ to sort the integers
        if debug:
            print(f"Java Bubble Sort finished in {(toc - tic):0.6f} seconds")

        # Add the runtime to the list
        javaBubbleTimes.append(toc-tic)

    # If debug is true, after all test runs, print the list of C++ runtimes
    if debug:
        print("Java bubble times:")
        print(javaBubbleTimes)


    # Selection Sort 1000, 2000, 3000, ..., 10000 integers
    for size in range(1000, 10001, 1000):
        # If debug is true, print statement to show where you are in the program
        if debug:
             print(f"Let's see how long it takes java to selection sort {size} random integers from a file!")
        # Start the clock
        tic = time.time()
        try:
            # This is Python's way of calling the command line. We use it to compile the Java files.
            subprocess.check_output("javac sort_java/SelectionSort.java",stdin=None,stderr=subprocess.STDOUT,shell=True)
        except subprocess.CalledProcessError as e:
            # There were compiler errors in SelectionSort.java. Print out the error message and exit the program.
            print("<p>",e.output,"</p>")
            raise SystemExit

        # Executes the java file
        p = Popen('java sort_java/SelectionSort.java '+str(size), shell=True, stdout=PIPE, stdin=PIPE)
        # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting
        if debug:
            print(p.stdout.read().decode('utf-8'))
        
        # End clock
        toc = time.time()

        # If debug is true, print the time it took C++ to sort the integers
        if debug:
            print(f"Java Selection Sort finished in {(toc - tic):0.6f} seconds")

        # Add the runtime to the list
        javaSelectionTimes.append(toc-tic)

    # If debug is true, after all test runs, print the list of C++ runtimes
    if debug:
        print("Java selection times:")
        print(javaSelectionTimes)


    # Radix Sort 1000, 2000, 3000, ..., 10000 integers
    for size in range(1000, 10001, 1000):
        # If debug is true, print statement to show where you are in the program
        if debug:
             print(f"Let's see how long it takes Java to radix sort {size} random integers from a file!")
        # Start the clock
        tic = time.time()
        try:
            # This is Python's way of calling the command line. We use it to compile the Java files.
            subprocess.check_output("javac sort_java/RadixSort.java",stdin=None,stderr=subprocess.STDOUT,shell=True)
        except subprocess.CalledProcessError as e:
            # There were compiler errors in SelectionSort.java. Print out the error message and exit the program.
            print("<p>",e.output,"</p>")
            raise SystemExit

        # Executes the java file
        p = Popen('java sort_java/RadixSort.java '+str(size), shell=True, stdout=PIPE, stdin=PIPE)
        # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting
        if debug:
            print(p.stdout.read().decode('utf-8'))
        
        # End clock
        toc = time.time()

        # If debug is true, print the time it took C++ to sort the integers
        if debug:
            print(f"Java Radix Sort finished in {(toc - tic):0.6f} seconds")

        # Add the runtime to the list
        javaRadixTimes.append(toc-tic)

    # If debug is true, after all test runs, print the list of C++ runtimes
    if debug:
        print("Java radix times:")
        print(javaRadixTimes)


# JavaScript sorting
if runJS:
    # Bubble Sort 1000, 2000, 3000, ..., 10000 integers
    for size in range(1000, 10001, 1000):
        # If debug is true, print statement to show where you are in the program
        if debug:
             print(f"Let's see how long it takes JavaScript to bubble sort {size} random integers from a file!")
        # Start the clock
        tic = time.time()

        # Runs the javascript file
        p = Popen('Node javascript/BubbleSort.js '+str(size), shell=True, stdout=PIPE, stdin=PIPE)
        # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting
        if debug:
            print(p.stdout.read().decode('utf-8'))
        
        # End clock
        toc = time.time()

        # If debug is true, print the time it took C++ to sort the integers
        if debug:
            print(f"JavaScript Bubble Sort finished in {(toc - tic):0.6f} seconds")

        # Add the runtime to the list
        jsBubbleTimes.append(toc-tic)

    # If debug is true, after all test runs, print the list of C++ runtimes
    if debug:
        print("JavaScript bubble times:")
        print(jsBubbleTimes)



# Graph the results - Bubble Sort

# Create a list of the sizes to use for the x axis tick marks
sizes = range(1000, 10001, 1000)
# Create lists that are offset so the Python bars aren't overlapping with C++ bars in the graph
pythonX = range(850, 10001, 1000)
cppX = range(1150, 10501, 1000)
# Create a graph plot with one (1) row and one (1) column.
# The third 1 signals to start at the first subplot (aka subplot 1 out of 1)
ax = plt.subplot(111)
# If not all of the data has been collected, use dummy data
if len(pythonBubbleTimes) < 10 or len(cppBubbleTimes) < 10 or len(javaBubbleTimes) < 10:
    # Plot the dummy values in blue
    ax.bar(sizes, range(1, 11), width=300, color='b', align='center')
else:
    # Plot the Python bars in red
    ax.bar(sizes, pythonBubbleTimes, width=-100, color='r', align='edge')
    # Plot the C++ bars in yellow
    ax.bar(sizes, cppBubbleTimes, width=100, color='y', align='edge')
    # Plot the Java bars in green
    ax.bar(sizes, javaBubbleTimes, width=100, color='g', align='center')
# Set the window title
plt.gcf().canvas.manager.set_window_title('Speed Test - Bubble Sort')
# Set the graph title
plt.title('Python, C++ and Java')
# Label the x axis
plt.xlabel('Number of integers to sort')
# Make sure the x-axis tick marks/labels are at each 1000
plt.xticks(sizes)
# Label the y axis
plt.ylabel('Times in seconds (Python in red, C++ in yellow, Java in green)')
# Save the graph to a file
plt.savefig('BattleOfTheBubbleSorts.png')
# Display the graph in a new window
plt.show()


# Graph the results - Selection Sort

# Create a list of the sizes to use for the x axis tick marks
sizes = range(1000, 10001, 1000)
# Create lists that are offset so the Python bars aren't overlapping with C++ bars in the graph
pythonX = range(850, 10001, 1000)
cppX = range(1150, 10501, 1000)
# Create a graph plot with one (1) row and one (1) column.
# The third 1 signals to start at the first subplot (aka subplot 1 out of 1)
ax = plt.subplot(111)
# If not all of the data has been collected, use dummy data
if len(pythonSelectionTimes) < 10 or len(cppSelectionTimes) < 10 or len(javaSelectionTimes) < 10:
    # Plot the dummy values in blue
    ax.bar(sizes, range(1, 11), width=300, color='b', align='center')
else:
    # Plot the Python bars in red
    ax.bar(sizes, pythonSelectionTimes, width=-100, color='r', align='edge')
    # Plot the C++ bars in yellow
    ax.bar(sizes, cppSelectionTimes, width=100, color='y', align='edge')
    # Plot the Java bars in green
    ax.bar(sizes, javaSelectionTimes, width=100, color='g', align='center')
# Set the window title
plt.gcf().canvas.manager.set_window_title('Speed Test - Selection Sort')
# Set the graph title
plt.title('Python, C++, and Java')
# Label the x axis
plt.xlabel('Number of integers to sort')
# Make sure the x-axis tick marks/labels are at each 1000
plt.xticks(sizes)
# Label the y axis
plt.ylabel('Times in seconds (Python in red, C++ in yellow, Java in green)')
# Save the graph to a file
plt.savefig('BattleOfTheSelectionSorts.png')
# Display the graph in a new window
plt.show()


# Graph the results - Radix Sort

# Create a list of the sizes to use for the x axis tick marks
sizes = range(1000, 10001, 1000)
# Create lists that are offset so the Python bars aren't overlapping with C++ bars in the graph
pythonX = range(850, 10001, 1000)
cppX = range(1150, 10501, 1000)
# Create a graph plot with one (1) row and one (1) column.
# The third 1 signals to start at the first subplot (aka subplot 1 out of 1)
ax = plt.subplot(111)
# If not all of the data has been collected, use dummy data
if len(pythonRadixTimes) < 10 or len(cppRadixTimes) < 10 or len(javaRadixTimes) < 10:
    # Plot the dummy values in blue
    ax.bar(sizes, range(1, 11), width=300, color='b', align='center')
else:
    # Plot the Python bars in red
    ax.bar(sizes, pythonRadixTimes, width=-100, color='r', align='edge')
    # Plot the C++ bars in yellow
    ax.bar(sizes, cppRadixTimes, width=100, color='y', align='edge')
    # Plot the Java bars in green
    ax.bar(sizes, javaRadixTimes, width=100, color='g', align='center')
# Set the window title
plt.gcf().canvas.manager.set_window_title('Speed Test - Radix Sort')
# Set the graph title
plt.title('Python, C++, and Java')
# Label the x axis
plt.xlabel('Number of integers to sort')
# Make sure the x-axis tick marks/labels are at each 1000
plt.xticks(sizes)
# Label the y axis
plt.ylabel('Times in seconds (Python in red, C++ in yellow, Java in green)')
# Save the graph to a file
plt.savefig('BattleOfTheRadixSorts.png')
# Display the graph in a new window
plt.show()
