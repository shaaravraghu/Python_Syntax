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
