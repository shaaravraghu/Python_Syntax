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
