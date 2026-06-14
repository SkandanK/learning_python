#!/usr/bin/env python3

# Functions: blocks of code that do a specific job or task
# #1 way to organize code is to write as functions
# Many functions can be stored in one file called modules

# simple function to print a greeting
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

# function with one parameter
def greet_user_name(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

# function with multiple positional arguments: order of arguments is required
def add_student(name, grade):
    """Display student info."""
    print(f"Name of student is {name.title()}!")
    print(f"Grade of student is {grade}!")


greet_user()
greet_user_name('jesse')
greet_user_name('jay')

# Passing POSITIONAL arguments: Order of arguments has to be maintained
add_student('Skandan', 9)
# Passing KEYWORD based arguments: Order of arguments need not be maintained
add_student(grade = 9, name = 'Skandan')

