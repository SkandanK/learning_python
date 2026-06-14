#!/usr/bin/env python3

# A Dictionary is composed of key-value pairs 
# Used to store pieces of RELATED information
student = {'name': 'skandan', 'gender': 'male', 'eye_color': 'black'}
print(student['name'])
print(student['gender'])
print('Original: ', student)

# Adding to a dictionary: Access is through the key
student['school'] = 'AHS'
print('Added school: ', student)
# Modifying a value
student['school'] = 'WHS'
print('Modified: ', student)
# Starting an empty dictionary
new_student = {}
print('Empty: ', new_student)

# Deleting a key-value pairs
del student['school']
print('Deleted: ', student)

# Using get() method on dictionary: get allows to give a default value if key is not found
print(student.get('gender', 'not_found'))
print(student.get('city', 'not_found'))
if student.get('city', 'not_found') == 'not_found':
    print("Key was not found. Moving on")

# Looping for Dictionaries:
# Looping over all items in a dictionary
for key, value in student.items():
    print('Items: ', key, value)
# You can simply say k,v also

# Looping over all keys in a dictionary
for k in student.keys():
    print('Key: ', k, 'Value: ', student[k])

# Looping over all keys in a dictionary, in sorted order
for k in sorted(student.keys()):
    print('Sorted Key: ', k, 'Value: ', student[k])

# Looping over all keys in a dictionary
for val in student.values():
    print('Value: ', val)
