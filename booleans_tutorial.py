# Booleans
#
#
# A boolean is a value of either:
#   True
#   False
#
# In Python 2.x and in Python 3.x, a boolean is also an int.
# The bool type is a subclass of the int type and True and False are
# its only instances namely 1 and 0 respectively.
#
assert True
assert not False
#
# True equivalent values:
#
assert bool(1) is True
assert bool([0]) is True
assert bool('a') is True
#
# False equivalent values:
#
assert bool(0) is False
assert bool([]) is False
assert bool('') is False

# Logical operations like 'and', 'or', 'not' can be performed
# on booleans.