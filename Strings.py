# Creating strings, with quotes, escape sequences, raw string, type, index-sequence
s = "Hello"
s = 'Hello'
s = """Hello
World"""
s = '''Hello
World'''
s = "I'm learning Python"
s = 'He said "Hello"'
s = 'I\'m learning Python'
s = "He said \"Hello\""
s = "He said \"Hello\""
# | Escape | Meaning         |
# | ------ | --------------- |
# | `\n`   | Newline         |
# | `\t`   | Tab             |
# | `\\`   | Backslash       |
# | `\'`   | Single quote    |
# | `\"`   | Double quote    |
# | `\r`   | Carriage return |
# | `\b`   | Backspace       |
# | `\0`   | Null character  |
# raw string
s = r"C:\Users\Shaarav\Documents"
print(type(s)) # <class 'str'>
# P  y  t  h  o  n
# 0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1












# Immutability, length, iteration, slicing, quick reverse, concatenation, repetition, membership, comparison
s = "Python"
s[0] = "J" # Type error
s =  """s[:]""" + "J" + s[1:]
print(s) # was made to reference another object; instead of changing it
len(s)
s = "Python"
for ch in s:
    print(ch) # item-based
for i in range(len(s)):
    print(s[i]) # range-based
# reverse string
s[::-1]
a = "Hello"
b = "World"
c = a + " " + b # concatenation
"ab"*3 # repetition
variable/ char in/ not in variable/ char
# == != > >= < <=: Python compares Unicode code points lexicographically.











# In-built Functions 
s = "Python"
s.lower()   # python
s.upper()   # PYTHON
s # immutability ("Python")

# upper/ lower case
"hello world".capitalize() # Hello world (only 1st character)
"hello world".title() # Hello World
"PyThOn".swapcase() # pYtHoN
s = "   hello   "

# strip
print(s.strip()) #|Hello|
s.rstrip() # right strip
s.lstrip() # left strip
"abcHelloabc".strip("abc") #|Hello|
"--Hello------".strip("-") #|Hello|

# replace
s = "hello world"
print(s.replace("world", "Python")) #hello Python
s.replace("a", "x", 2) # limit to first 2 matches

# locate
s = "hello world"
print(s.find("world")) # 6 (index number) and returns -1 if not found!
s.index("xyz") # returns ValueError

# counter
s = "banana"
print(s.count("a")) # 3
"aaaa".count("aa") # 2: counts non-overlapping occurances

# match start/ end
s = "Python programming"
s.startswith("Python")  # True
s.endswith("ing")       # True
s.startswith(("Java", "Python", "C++")) # alternate option: tuples

# split
s = "apple,banana,orange"
result = s.split(",")
print(result) # ['apple', 'banana', 'orange']
s = "hello   world   python"
print(s.split()) # ['hello', 'world', 'python']
s = "a-b-c-d"
print(s.split("-", 2)) # ['a', 'b', 'c-d']
print(s.rsplit("-", 2)) # ['a-b', 'c', 'd']
s = "hello\nworld\npython"
print(s.splitlines()) # ['hello', 'world', 'python']

# join
separator.join(iterable)
words = ["Python", "is", "awesome"]
result = " ".join(words)
print(result)

# partition
s = "name=Shaarav"
print(s.partition("=")) # ('name', '=', 'Shaarav')
# before
# separator
# after
s.rpartition()















# String Validation Methods
s.isalpha()	# all characters are letters	
s.isdigit()	# all characters are digits	
s.isalnum()	# all characters are letters OR digits	
s.isspace()	# all characters are whitespace	
s.islower()	# has at least one character, and all characters are lowercase
s.isupper()	# has at least one character, and all characters are uppercase	
s.istitle()	# string follows title-case rules	
isdecimal()	# Decimal digits 0–9 
isdigit()	# Decimal digits + some special digit characters ONLY
isnumeric()	# Digits + numeric characters such as fractions, Roman numerals, decimal (everything related to numbers)









# zfill()
"42".zfill(5)
# 00042
"-42".zfill(5)
# -0042

# Alignment
"hello".ljust(10)
"hello".rjust(10)
"hello".center(10)
"hello".center(11, "-")

# f-String: Formatting
# Variables
name = "Shaarav"
age = 20
print(f"My name is {name} and I am {age}")
# Expression
a = 10
b = 20
print(f"Sum = {a + b}")
# Functions
print(f"Length = {len('Python')}")

# Number Formatting 
x = 3.14159265
f"{x:.2f}"    # 2 decimal places
f"{x:10}"     # width 10
f"{x:05}"     # zero padded
f"{x:,}"      # thousands separator
# Percentage Formatting
x = 0.756
print(f"{x:.2%}")
# Format Specifiers
f"{value:format_spec}"
f"{42:05}"       # 00042
f"{42:<10}"      # left aligned
f"{42:>10}"      # right aligned
f"{42:^10}"      # centered
f"{1234567:,}"   # 1,234,567

# format()
name = "Shaarav"
print("Hello, {}".format(name))
print("{} + {} = {}".format(2, 3, 5))
print("{name} is {age}".format(name="Shaarav", age=20))
# older syntax
name = "Shaarav"
age = 20
print("My name is %s and I am %d" % (name, age))
