# Lists: A list is an ordered, mutable collection of objects.
my_list = [1, 2, 3, 4, 5]
# A list can contain various datatypes at a single time.
data = [10, "hello", 3.14, True, None]
# Nested Lists
nested = [[1, 2], [3, 4], [5, 6]]
# Empty
empty = []
empty = list()











# Index, Access, Modification, Slicing
# Index:    0    1    2    3    4
#           ↓    ↓    ↓    ↓    ↓
# List:    10   20   30   40   50
#          -5   -4   -3   -2   -1
list1[i] # access
# modification
numbers = [10, 20, 30]
numbers[1] = 100
numbers[0:2] = [50, 60]
# slicing
list[start:stop:step]








# Append, Extend, Insert
numbers = [1, 2, 3]
numbers.append(4) # [1, 2, 3, 4]
numbers.append([5, 6]) # [1, 2, 3, 4, [5, 6]]
numbers = [1, 2, 3]
numbers.extend([4, 5, 6]) # [1, 2, 3, 4, 5, 6]
x = [1, 2]
x.extend("abc") # [1, 2, 'a', 'b', 'c']
list.insert(index, value)
numbers = [10, 20, 30]
numbers.insert(1, 99) # [10, 99, 20, 30]









# Remove (Value), Pop (Index), Del
numbers = [10, 20, 30, 20]
numbers.remove(20) # [10, 30, 20]
numbers.remove(100) # ValueError
numbers = [10, 20, 30]
x = numbers.pop() # 30 ([10, 20])
print(x) # 30
print(numbers) # [10, 20]
x = numbers.pop(1)
numbers = [1, 2, 3]
numbers.clear() # []
# del is a Python statement, not a list method.
numbers = [10, 20, 30, 40]
del numbers[1] # numbers: [10, 30, 40]
del numbers[1:3] # numbers: [10]
del numbers
print(numbers) # NameError



# Search (in), Index, Count
numbers = [10, 20, 30]
print(20 in numbers) # True
print(50 not in numbers) # True
numbers = [10, 20, 30, 20]
print(numbers.index(20))
numbers.index(value, starting_index)
numbers = [1, 2, 2, 2, 3]
print(numbers.count(2)) # 3











# Length, Concatenation, Repetition
len(my_list)
a = [1, 2]
b = [3, 4]
c = a + b
print(c) # [1, 2, 3, 4]
a = [1, 2]
print(a * 3) # [1, 2, 1, 2, 1, 2]
# Important Example
x = [[0] * 3] * 3
print(x) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
x[0][0] = 99
print(x) # [[99, 0, 0], [99, 0, 0], [99, 0, 0]]
# Because all three inner lists refer to the same object.
# Correct way of initialising
x = [[0] * 3 for _ in range(3)]
x[0][0] = 99
print(x) # [[99, 0, 0], [0, 0, 0], [0, 0, 0]]












# Deep and Shallow Copy
# Deep Copy
a = [1, 2, 3]
b = a
# This does not create a new list.
# Both variables refer to the same list.
b.append(4)
print(a) # [1, 2, 3, 4]
# Shallow Copy
b = a.copy()
# or:
b = a[:]
# or:
b = list(a)
# Example
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)
print(b)
# [1, 2, 3]
# [1, 2, 3, 4]








# List Comprehension
# [expression for item in iterable if condition]
# Regular Method
squares = []
for x in range(5):
    squares.append(x ** 2)
# List Comprehension Method
squares = [x ** 2 for x in range(5)] # [0, 1, 4, 9, 16]
# Another Example
even = [x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]

# Nested List Comprehension
# Regular Method
flat = []
for row in matrix:
    for x in row:
        flat.append(x)
# Nested List Comprehension Method
flat = [x for row in matrix for x in row]
print(flat)










# Tuple: Ordered, Immutable Collection
numbers = (1, 2, 3, 4)
numbers = 1, 2, 3, 4 # Tuple Packing
numbers = ()
numbers = 1,
numbers = tuple()
# x = (10): not tuple (type int)
# Regular Indexing
# Cannot append, remove, or modify: best way to change is tuple() -> list() -> (changes) -> tuple()



# Built-in Functions
t = (1, 2, 2, 3, 2)
print(t.count(2))
t = (1, 2, 2, 3, 2)
print(t.count(2))



# Packing and Unpacking
person = ("Shaarav", 21, "India") # Packing
name, age, country = person # Unpacking
print(name)
print(age)
print(country)
# Extended Unpacking
numbers = (1, 2, 3, 4, 5)
a, *b = numbers
print(a) # 1
print(b) # [2, 3, 4, 5]
a, b, *c, d = numbers
print(a) # 1
print(b) # 2
print(c) # [3, 4]
print(d) # 5














# Miscellaneous
# Mutable Objects in Immutable Objects
t = ([1, 2], [3, 4])
# We cannot modify t[0] but we can modify t[0][0] and t[0][1]
# is v/s ==
a = [1, 2]
b = a
# refers to same object
a is b # True
a == b # True
c = a.copy()
#  doesn't refer to same object
c is a # False
c == a # True (value)
# Unpacking
a = [1, 2, 3]
print(a) # [1, 2, 3]
print(*a) 1 2 3
a = [1, 2, 3]
b = [4, 5, 6]
c = [*a, *b]
print(c) # [1, 2, 3, 4, 5, 6]
c = [a, b] # [[1, 2, 3], [4, 5, 6]]
# f(*args) to unpack lists and tuples and f(**kwargs) to unpack dictionaries
# Hashability
{(1, 2): "value"} # Creates Dictionary Keys
{[1, 2]: "value"} # Not Hashable



# Sorting
list.sort(key=None, reverse=False)
# key refers to function to be used while sorting
sequence.sort()
data.sort(reverse=True)
data.sort(key=lambda x: (-x["score"], x["name"]))
result = sorted(data) # doesn't change input
result = list(reversed(iterable))
