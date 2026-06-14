#!/usr/bin/env python3

### Nesting: One data type inside another data type
# Dictionaries containing Lists
students = {
    '100': ['Arjun','AHS', 'Gr9'],
    '101': ['Ameya','WHS','Gr10'],
    '102': ['Arun','TMS','Gr8']
    }
print('Dict containing lists: Student 101: ', students['101'])

# List containing dictionaries
student101 = {'name': 'Arjun', 'school': 'AHS', 'grade': 9}
student102 = {'name': 'Ameya', 'school': 'WHS', 'grade': 10}
student103 = {'name': 'Arun', 'school': 'TMS', 'grade': 8}
student_list = [student101, student102, student103]
for st in student_list:
    print('List containing dictionaries:', st['name'])

# Dictionary containing dictionaries
students_roster = {
    '100': {'name': 'Arjun', 'school': 'AHS', 'grade': 9},
    '101': {'name': 'Ameya', 'school': 'WHS', 'grade': 10},
    '102': {'name': 'Arun', 'school': 'TMS', 'grade': 8}
    }
print("Name of a given student number: ", students_roster['102']['name'])
# Loop and print all names
for key, value in students_roster.items():
    print('List contains name:', value['name'])