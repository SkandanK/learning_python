#!/usr/bin/env python3

# This is a script that will cover basics of variables and data types

## 1 simple variable declaration and print: 
message = "Hello Python World!"
print(message)
# variable names rules: only letters,numbers, and underscores. cannot use python keywords
# guideline: variable names should be lowercase, should be short but descriptive

## 2 types of variables 
# Strings: A series of characters. Anything in quotes("")('')
first_name = "ada"
last_name = "lovelace"
print(first_name, last_name)            
# print is an in-built function that can take multiple parameters; default seperator is space (" ")

# String methods: in-built operations available in python for strings
print(first_name.title(), last_name.upper(), last_name.lower())
# f-strings: formatted strings
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
# Adding whitespace with tabs or newlines 
print("Languages:\n\tPython\n\tC\n\tJavaScript\n")
# Stripping whitespace
favorite_lang = '      python    '
print(f"'{favorite_lang.rstrip()}''{favorite_lang.lstrip()}''{favorite_lang.strip()}'")

# Numbers: Integers and floating numbers
# Integer Operators: +, -, *, /, **.
print(3 + 3, 4 - 3, 3 * 3, 6 / 3, 9 ** 3, 2 + 3 * 4, (2 + 3) * 4)
# Float operators: +, -, *, /, **, %,
print(3.0 + 3, 4 - 3.0, 3.0 * 3, 6 / 3, 9 ** 3.0, 2 + 3.0 * 4, (2.0 + 3) * 4)
# Special use of underscore on display ("_")
universe_age = 14_000_000_000
print(universe_age)
print(1000,1_000,10_00)
# Multiple assignment statement
x, y, z = 0, 1, 2
print(x,y,z)
# Constants: Python does NOT have constant type, so we just use all CAPS as a guideline
PI = 3.14159265
print(PI)


# Type casting: applying a type to a value
age = int("35")     # Converting string to integer
weight = float("150.5")     # Converting string to float
jersey = str(22)    # Converting into string

# Boolean data type: stores True or False
flag = True
flag = False
answer = ""
if answer:
    print("String not empty")
else:
    print("String is empty")

answers = []
if answers:
    print("List not empty")
else:
    print("List is empty")
    