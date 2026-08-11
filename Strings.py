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
