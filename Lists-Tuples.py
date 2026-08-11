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












