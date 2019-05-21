# Sets
#
#
# Sets are unordered collections of UNIQUE objects, there are two
# types of set:
#
# 1. Sets: They are mutable and new elements can be added once
# sets are defined
#
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
assert basket == {'apple', 'orange', 'pear', 'banana'}
#
# 2. Frozen Sets: They are immutable and new elements cannot added
# after its defined.
#
basket = frozenset(['apple', 'orange', 'apple', 'pear'])
assert basket == frozenset({'pear', 'apple', 'orange'})
#
# WOW! WOW! MAJOR N.B.
# To create an empty set never use '{}' as it will create an empty
# dictionaries hence use:
empty_set = set()
#
# Set are useful for quickly testing for membership and for
# performing intersection, union and difference operations:
#
# First to find out the length of a set use the 'len' keyword:
#
first_basket = {'apple', 'orange', 'pear', 'banana'}
second_basket = {'avocado', 'apple'}
#
assert len(first_basket) == 4
assert len(second_basket) == 2
#
# SET OPERATIONS:
#
# The membership/inclusion test:
#
assert 'orange' in first_basket
assert 'avocado' not in first_basket
#
# Calculate the intersection (In both sets):
#
assert first_basket & second_basket == {'apple'}
assert first_basket.intersection(second_basket) == {'apple'}
#
# Calculate the union (All unique elements in both):
#
assert first_basket | second_basket == {'avocado', 'pear', 'banana',
                                        'orange', 'apple'}
assert first_basket.union(second_basket) == {'avocado', 'pear', 'banana',
                                        'orange', 'apple'}
#
# Calculate the difference:
#
assert first_basket - second_basket == {'orange', 'pear', 'banana'}
assert first_basket.difference(second_basket) == {'orange', 'pear', 'banana'}
#
#
#
