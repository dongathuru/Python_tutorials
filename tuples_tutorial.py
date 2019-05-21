# Tuples
#
#
# Lists are enclosed in brackets [ ] and their elements and size can
# be changed, while tuples are enclosed in parentheses ( )
# and cannot be updated. Tuples are immutable
#
first_tuple = (123, 'hello')
#
# As seen below when declaring a tuple with one element ALWAYS ADD A
# TRAILING COMMA otherwise it won't be seen as a tuple.
#
second_tuple = ('world',)
#
# By the way tuples don't support item assignment and those many
# methods that mutate the list cannot be applied to them
#
# tuple[1]='update'  #this will give you error.
#
# Otherwise they behave pretty much the same as lists we can access
# items and also loop through them.
#
assert first_tuple[0]  == 123
#
assert first_tuple + second_tuple == (123, 'hello', 'world')