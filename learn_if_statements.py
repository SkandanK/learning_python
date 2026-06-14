#!/usr/bin/env python3

# This script will ctake 2 floating numbers as input and 
# output if the first number is greater than the second number or less than or equal to.
# importing sys module 
import sys

# initializing variables
#input_year = 2001
input_number1 = float(sys.argv[1])
input_number2 = float(sys.argv[2])

# Method 1: Using if - else:
if input_number1 > input_number2:
    print("1st number is greater than 2nd number")
else: 
    if input_number1 < input_number2:
        print("1st number is less than 2nd number")
    else:
        print("1st number is equal to 2nd number") 

# Method 2: Using elif: if - else
# Always use else as a catch all for invalid data
if input_number1 > input_number2:
    print("1st number is greater than 2nd number")
elif input_number1 < input_number2:
    print("1st number is less than 2nd number")
else:
    print("1st number is equal to 2nd number")

# Conditional Operators:
print('1 == 2', 1 == 2)
print("'bmw' == 'bmw'", 'bmw' == 'bmw')
print("'Audi'.lower() == 'audi'", 'Audi'.lower() == 'audi')
print("'bmw' != 'bmw'", 'bmw' != 'bmw')
print('1 > 2', 1 > 2)
print('1 >= 2', 1 >= 2)
print('1 < 2', 1 < 2)
print('1 <= 2', 1 <= 2)

# Multiple conditions: And, or
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >=21

age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >=21

age_0 = 18
age_0 >= 21 and age_1 >=21

# Checking if a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings

# Checking if a value is not in a list
banned_users = ["andrew", "carolina", "david"]
user = 'marie'
if user not in banned_users:
    print(f"{user.title(O)}, you can post a response if you wish")

# Checking if list isn't empty

requested_toppings = []
if requested_toppings:
    print("List is not empty")
else:
    print("List is empty")

