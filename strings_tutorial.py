# Strings:
#
#
# String are identified as a contiguous set of characters represented in
# quotation marks. Python allows for either pairs of single or double
# quotes.
# Strings are immutable sequence data type, i.e each time one makes
# any changes to a string, a completely new string object is created.
#
# Strings are basically 'sentences':
#
single_quote_string = 'Hello World'
#
# or
#
double_quote_string = "Hello World"
#
# 'multi-line string':
#
multi_line_string = '''
String are identified as a contiguous set of characters represented in 
the quotation marks. Python allows for either pairs of single or 
double quotes. 
'''
#
# You can escape inline quotes using the '\' character however I
# find better to just interchange between single and double quotes
#
string_with_an_escaped_apostrophe = 'Adam\'s world'
my_preferred_unescaped_string = "Adam's world"
#
# You can test whether a string contains a certain word using the 'in'
# keyword e.g. whether the word 'Python' is in the 'multi_line_string'
#
assert 'Python' in multi_line_string
#
# STRING METHODS
#
# Python's string type provides many functions that act on strings.
# you can look them up in the Python documentation page.
# Some include and may follow the following structure:
#
my_message = 'Hello world'
#
# To capitalise each letter:
assert my_message.upper() == 'HELLO WORLD'
# To turn all the characters into lowercase:
assert my_message.lower() == 'hello world'
# To capitalise each first letter in a word in a sentence:
assert my_message.title() == 'Hello World'
# To count the no. of times a character appears in a string:
assert my_message.count('l') == 3
# To find the start location of a particular word in a sentence:
assert my_message.find('world') == 6
# In case the word being looked for does'nt exist:
assert my_message.find('universe') == -1
# To replace a given word with another in a sentence:
assert my_message.replace('world', 'universe') == 'Hello universe'
# To strip/remove whitespaces
assert '     Gon vs Hisoka    '.strip() == 'Gon vs Hisoka'
#
# All the above amongst others are some of the string methods...
#
#
# By the way: Finding out the length of a string use the 'len' keyword:
#
assert len(multi_line_string) == 155
#
# To split a string on a certain delimiter and produce a list:
#
assert my_message.split(' ') == ['Hello', 'world']
assert my_message.split('w') == ['Hello ', 'orld']
#
# For the joining/concatenating on a certain delimiter:
#
my_list = ['I', 'am', 'Chairman', 'Netero']
my_sentence_from_my_list = ' '.join(my_list)
assert my_sentence_from_my_list == 'I am Chairman Netero'
#
#
#
# STRING character ACCESSING and SLICING:
#
# So you can access the specific characters of a string just like you
# would values in a list and we start counting the indexes from '0'.
#
my_message = 'Hello world'
#
# e.g. getting the 1st character:
#
assert my_message[0] == 'H'
#
# The last character:
#
assert my_message[-1] == 'd'
#
# Slicing: You can access a given number of characters at a time.
# Note the last index's character ('5') is not displayed/included:
#
assert my_message[0:5] == 'Hello'
#
# or if you're starting for the beginning don't have to include the '0'
#
assert my_message[:5] == 'Hello'
#
# same applies for the end:
#
assert my_message[6:] == 'world'
#
#
#
# STRING FORMATTING:
#
# Now there exists a problem when it comes to incorporating things
# like variables..e.t.c inside a string of course one way to do
# it is by normal concatenation:
#
greeting = 'Hello'
name = 'Pitou'
my_message = greeting + ', ' + name + ' and welcome!'
assert my_message == 'Hello, Pitou and welcome!'
#
# As you can clearly see its ugly as Heck! and for long strings
# it can be confusing.
# So in comes 'String formatting':
#
my_formatted_message = '{}, {} and welcome!'.format(greeting, name)
assert my_formatted_message == 'Hello, Pitou and welcome!'
#
# For repetitive stuff:
#
tag = 'h1'
text = 'This is a headline'
sentence = '<{0}><{1}></{0}>'.format(tag, text)
assert sentence == '<h1><This is a headline></h1>'
#
# For dictionaries
#
person = {'name': 'Jenn', 'age': 23}
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
assert sentence == 'My name is Jenn and I am 23 years old.'
#
# For lists
#
my_list = ['Jenn', 23]
sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(my_list)
assert sentence == 'My name is Jenn and I am 23 years old.'
#
#
# Even better since Python 3.6 you can use 'f' strings:
#
my_formatted_message = f'{greeting}, {name} and welcome!'
assert my_formatted_message == 'Hello, Pitou and welcome!'
#
# For dictionaries
#
person = {'name': 'Tom Brady', 'age': 40}
sentence = f"My name is {person['name']} and I am {person['age']} years old."
assert sentence == 'My name is Tom Brady and I am 40 years old.'
#
#
#
# Some of the material from:
#     James Powell:
#     Cory Schafer:
#     PythonNotesForProfessionals: