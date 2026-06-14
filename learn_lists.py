#!/usr/bin/env python3

# This is a script that will cover basics of lists
# A list is a collection of items in a particular order

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# Accessing elements in a list: using indexes 
# Index Positions Start at 0, Not 1
# -1 gives the last item of the list

magicians = ['alice', 'david', 'carolina', 'jerome', 'preston']
print(magicians[0], magicians[4], magicians[-1], magicians[2:4])
# Slicing a list: getting a subset of the list
print(magicians[0:3], magicians[2:], magicians[-4:-2], magicians[-3:])

# Appending to a list
bicycles.append("schwinn")
print(bicycles, "\n")

# Inserting to a list to a given position
bicycles.insert(2, "mongoose")
print(bicycles)
# Combining 2 lists
drivers =['Hadjar', 'Lauda', 'Leclerc', 'Lewis', 'Max'] + ['Sonny', 'Arvid', 'Senna']
print(drivers, "\n")

# Removing elements from a list
del drivers[5]
print(drivers)

# Pop: remove last element from list and give the value as output
popped_driver = drivers.pop()
print(popped_driver)
print(drivers)
# Popping from a particular position
popped_driver = drivers.pop(2)
print(popped_driver)
print(drivers, "\n")
# Removing an item on value
# Note: it will remove the first occurence of the value
drivers =['Hadjar', 'Lauda', 'Leclerc', 'Lewis', 'Max'] + ['Sonny', 'Leclerc', 'Arvid', 'Senna']
print(drivers)
drivers.remove('Leclerc')
print(drivers, "\n")

# Organizing a list
# Sorting a list PERMANENTLY
bicycles.sort()
print("Sorted Bicycles:", bicycles)
# Sorting in reverse alphabetical PERMANENTLY
bicycles.sort(reverse = True)
print("Sorted Bicycles in Reverse:", bicycles)
# Sorting a list TEMPORARILY
sorted_bicycles = sorted(bicycles)
print("Sorted Bicycles:", sorted_bicycles)
# Reverse a list: means last to first, and does not sort (PERMANENTLY)
print("Drivers:", drivers)
drivers.reverse()
print("Reversed Drivers:", drivers)
# Length of a list
print("Length of Drivers:", len(drivers))

# Looping over a list's elements
for magician in magicians:
    magician = magician.title() 
    print(magician + ", that was a great trick!")

# Simple stats on lists
digits = [1,2,3,4,5]
print("Stats:", min(digits), max(digits), sum(digits))

# List Comprehensions
# Initializing a numerical list with a range function
squares = [value**2 for value in range(1, 11)]
print("Squares:", squares)
# Initializing a string list with a range function
repeats = [value*"hello world!" for value in range(1,6)]
print("Repeats:", repeats)

# Copying a list 
# Method 1: Does not create a new copy of the list; So, if you make a change to one list it will change the other also
magicians1 = magicians
magicians.append("Sircar")
print("Original List: ", magicians)
print("Duplicate List: ", magicians1)
# Method 2: This will create a copy of the list
magicians_copy = magicians[:]
magicians.append("Sircar Jr.")
print("Original List: ", magicians)
print("Duplicate List: ", magicians_copy)

# Tuples: A collection of items that are IMMUTABLE (cannot be changed)
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Cannot change value of elements
# dimensions(0) = 250         will result in an error
# But you can re-declare the whole tuple
dimensions = (400, 100)
