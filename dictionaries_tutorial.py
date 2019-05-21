# Dictionaries
#
#
# Dictionary consists of key-value pairs. It is enclosed by curly
# braces {} and values can be assigned and accessed using square
# brackets[].
#
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
#
# To access the values: 'dictionary_name['key']'
#
assert student['name'] == 'John'
assert student['courses'] == ['Math', 'CompSci']
#
# Keys can actually be any immutable datatype
#
# Lets say we don't always want to receive a key error if an item
# is not present we can use:
# '.get('absent_key', 'message we want')' method:
#
assert student.get('phone', 'Not Found') == 'Not Found'
#
# To update a certain value:
#
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student['name'] = 'Jane'
assert student == {'name': 'Jane', 'age': 25, 'courses': ['Math', 'CompSci']}
#
# To update a set of values:
#
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
assert student == {'name': 'Jane', 'age': 26, 'courses': ['Math', 'CompSci'], 'phone': '555-5555'}
#
# To delete a certain key and its value we can use the 'del' keyword or
# use the 'pop' method:
#
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
del student['age']
assert student == {'name': 'John', 'courses': ['Math', 'CompSci']}
#
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
age = student.pop('age')
assert age == 25
assert student == {'name': 'John', 'courses': ['Math', 'CompSci']}
#
# Looping through the keys and values in a dictionary:
#
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
#
assert len(student) == 3
#
# First to see all the keys we have in our dictionary:
#
print(student.keys())
# Above line's output: dict_keys(['name', 'age', 'courses'])
#
# To see all the values:
#
print(student.values())
# Above line's output: dict_values(['John', 25, ['Math', 'CompSci']])
#
# Now to see the key value pairs:
#
print(student.items())
# Above line's output: dict_items([('name', 'John'), ('age', 25),
#                                   ('courses', ['Math', 'CompSci'])])
#
# Looping through all the keys and values in our dictionary
#
for key, value in student.items():
    print(key, value)
#
# Result:
#
# name John
# age 25
# courses ['Math', 'CompSci']