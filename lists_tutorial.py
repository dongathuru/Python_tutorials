# Lists
#
#
# A list contains items separated by commas and enclosed within square
# brackets [].
# lists are almost similar to arrays in C. One difference is that all
# the items belonging to a list can be of  different data type.
#
# lists are mutable and ordered
#
my_list = ['pizza', 123, 10.2, 'd']
courses = ['History', 'Math', 'Physics', 'CompSci']
#
# To know the length of a list use the 'len' keyword:
#
assert len(courses) == 4
#
# To access the 1st element in a list:
#
assert courses[0] == 'History'
#
# To access the last element in the list:
#
assert courses[-1] == 'CompSci'
#
# To access multiple elements in a list from a start-index('0')
# to an end-index('2' (not included)):
#
assert courses[0:2] == ['History', 'Math']
#
# If you start accessing from the beginning you don't have to
# include the start index('0'):
#
assert courses[:2] == ['History', 'Math']
#
# Same for the end-index:
#
assert courses[2:] == ['Physics', 'CompSci']
#
#
# LIST METHODS:
#
# Adding an element to the end of a list use '.append()':
#
courses.append('Art')
assert courses == ['History', 'Math', 'Physics', 'CompSci', 'Art']
#
# To insert an element to a given index use '.insert(index, element)':
#
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.insert(0, 'Art')
assert courses == ['Art', 'History', 'Math', 'Physics', 'CompSci']
#
# To add multiple elements/another list to a list use '.extend()':
#
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.extend(courses_2)
assert courses == ['History', 'Math', 'Physics', 'CompSci', 'Art', 'Education']
#
# To remove a given element from a list use '.remove()':
#
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.remove('Math')
assert courses == ['History', 'Physics', 'CompSci']
#
# To remove the last element from a list use '.pop()'
#
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.pop()
assert courses == ['History', 'Math', 'Physics']
#
# You can also access a 'popped' element and assign it:
#
courses = ['History', 'Math', 'Physics', 'CompSci']
popped = courses.pop()
assert popped == 'CompSci'
#
# To reverse the order of a given list use '.reverse()':
#
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.reverse()
assert courses == ['CompSci', 'Physics', 'Math', 'History']
#
# To order elements in a given list use '.sort()':
#
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.sort()
assert courses == ['CompSci', 'History', 'Math', 'Physics']
#
nums = [1, 5, 4, 3]
nums.sort()
assert nums == [1, 3, 4, 5]
#
# Ordering elements in reverse requires '.sort(reverse=True)':
#
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.sort(reverse=True)
assert courses == ['Physics', 'Math', 'History', 'CompSci']

nums = [1, 5, 4, 3]
nums.sort(reverse=True)
assert nums == [5, 4, 3, 1]
#
# The problem with the above is that they are altering the list
# 'in-place': (changing the original) now the alternative to this is:
#
# The '.sorted()' method:
#
nums = [1, 5, 4, 3]
courses = ['History', 'Math', 'Physics', 'CompSci']
sorted_courses = sorted(courses)
assert sorted_courses == ['CompSci', 'History', 'Math', 'Physics']
#
# You can also use 'min', 'max', 'sum' to know the 'minimum' and
# 'maximum' elements in a list and their 'sum' respectively:
#
assert min(nums) == 1
assert max(nums) == 5
assert sum(nums) == 13
#
# Finding the indexes of elements in a list use '.index()':
#
courses = ['History', 'Math', 'Physics', 'CompSci']
assert courses.index('CompSci') == 3
#
# Looking for the 'existence' or 'lack there of' an element in a
# list use 'in' / 'not' keywords:
#
assert 'Art' not in courses
#
# To print all the elements in a given list:
#
for course in courses:
    print(course)
#
# Result:
#
# History
# Math
# Physics
# CompSci
#
# NB: So by default the print statement goes to a new line each time
# its executed
#
print()
#
# So the enumerate function below allows us to be able to print
# (index, element) pairs. But since the function's default start-index
# is '0' we can add a 'start' parameter specify where it can start:
#
for index, value in enumerate(courses, start=1):
    print(index, value)
#
# Result:
#
# 1 History
# 2 Math
# 3 Physics
# 4 CompSci
#
#
# To turn our list into strings separated by a given value
# will be using a list method called '.join()'
#
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_str = ', '.join(courses)
assert courses_str == 'History, Math, Physics, CompSci'
#
# Turning a list into a string we use the 'split method'
#
courses_str = 'History, Math, Physics, CompSci'
courses = courses_str.split(', ')
assert courses == ['History', 'Math', 'Physics', 'CompSci']
#
# To produce a given list 2 times:
#
my_list = ['Hello', 'world']
assert my_list * 2 == ['Hello', 'world', 'Hello', 'world']
#
# You can also concatenate 2 lists:
#
assert my_list + my_list == ['Hello', 'world', 'Hello', 'world']