#!/usr/bin/env python3

# this script will take as input age of a person 
# it will calculate ticket price based on age
# it will output the ticket price
# standard ticket price: $15
# child (less than 13 years old) ticket price: 50% discount 
# elderly (more than or is 65 years old): 25% discount
# baby (0-2): free
# importing sys module 
import sys
# initializing variables
input_age = float(sys.argv[1])
output_price = 15

name = input("Enter your name: ")

if input_age < 3: 
    print ("Price for", name, "is Free")
elif input_age < 13:
    output_price13 = output_price*(0.5)
    print ("Price for", name, "is $", output_price13)
elif input_age >= 65:
    output_price65 = output_price*(0.75)
    print ("Price for", name, "is $", output_price65)
else:
    print ("Price for", name, f"is ${output_price}!")
    print(f"Hello, {name}!")


