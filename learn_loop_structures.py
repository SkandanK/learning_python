#!/usr/bin/env python3

magicians = ['alice', 'david', 'carolina', 'jerome', 'preston']
# magicians.sort()

# For loop: iterating a specific number of times
# looping over a list
for magician in magicians:
    magician = magician.title() 
    print(magician + ", that was a great trick!")

# List functions
print(magicians[0], magicians[4], magicians[-1], magicians[2:4])
print(magicians[0:3], magicians[2:], magicians[-4:-2], magicians[-3:])

# Looping over a range
# Range function gives the values from the starting value until the last value EXCLUDING the last value
# In the example below 5 is excluded 
for value in range(1, 5):
    print(value)

# Use an incremental value in the range function
# This example will give all odd numbers from 1 to 11
for value in range(1, 12, 2):
    print(value)

# While loop: iterating based on a condition
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("\nEnter any word starting with A, enter 'exit' to stop")
word = ''
while word != 'exit':
    word = input("Enter your word:")
    if word[0].upper() == 'A':
        print("You entered: " + word)
    else:
        continue        # Once you come to continue, you go back to next iteration
    print("You understand the request")

age = int(input('Enter your age!'))
while age > 0:
    if age >= 126: 
        break 
    elif age >= 18:
        print("Adult Detected!!!")
    else:
        print("Minor Detected!!!")
    age = int(input('Enter your age!'))


person = input('Enter your name')
question = input('Are you a magician, yes or no?')
while person