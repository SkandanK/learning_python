#!/usr/bin/env python3

# This script will calculate whether this year is a leap year or not
# importing sys module 
import sys

# initializing variables
#input_year = 2001
input_year = int(sys.argv[1])

# leap year logic below (calculations)
if (input_year % 4) == 0:
    if (input_year % 400) == 0:
        print("Not a Leap Year")
    else:
        print("Leap Year Confirmed")
else:
    print("Not a Leap Year")
