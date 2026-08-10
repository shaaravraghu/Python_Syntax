# 1. for loop   → iterate over a sequence/iterable
# 2. while loop → repeat while a condition remains true

# FOR LOOP OVER RANGE
for variable in iterable: # Initialization + Condition + Update
    statement # Body
for i in range(5):
    print(i)
# 0 - (n-1) iterations
range(start, stop, step)
# negative step value for backward iteration; start > stop

# FOR LOOP OVER ITEM
# String Iteration
word = "Python"
for ch in word:
    print(ch)
# List Iteration
arr = [10, 20, 30, 40]
for x in arr:
    print(x)
# Tuple Iteration
data = (10, 20, 30)
for x in data:
    print(x)
# Set Iteration: not preferred since it's an unordered list
s = {10, 20, 30}
for x in s:
    print(x)
# Dictionaries Iteration
d = {
    "a": 10,
    "b": 20,
    "c": 30
}
for x in d: # key iteration
    print(x) 
# a
# b
# c
for x in d.values(): # value iteration
    print(x)
# 10
# 20
# 30
# keys and values iteration
for key, value in d.items():
    print(key, value)
# a 10
# b 20
# c 30









# ENUMERATE
for i, value in enumerate(arr):
    print(i, value)
# 0 10
# 1 20
# 2 30
for i, value in enumerate(arr, start=1):
    print(i, value)
# 1 10
# 2 20
# 3 30

# ZIP
names = ["A", "B", "C"]
marks = [90, 80, 70]
for name, mark in zip(names, marks):
    print(name, mark)
# A 90
# B 80
# C 70
# stops at shorter item









#  NESTED LOOPS
for i in range(n):
    for j in range(n):
        print(i, j)
# Dependant Loop
for i in range(n):
    for j in range(i):
        print(i, j)
# Triangular Loop
for i in range(n):
    for j in range(i + 1, n):
        ...








# WHILE LOOP
while condition:
    statement
i = 0
while i < 5:
    print(i)
    i += 1
# Initialization
#   ↓
# Condition
#   ↓
# Body
#   ↓
# Update
#   ↓
# Repeat




# INFINITE LOOP, BREAK & CONTINUE
while True:
    ...
for i in range(10):
    if i == 5:
        break # terminate loop
    print(i)
for i in range(10):
    if i == 5:
        continue # skip current iteration
    print(i)
# break only terminates the inner-most loop is a nested loop system
# continue only skips current iteration of the inner most loop in a nested loop system







# ELSE
for iterator in range/ item:
    body
else:
    body
# runs always after loop unless forcibly stopped by break statement (continue has no effect on it)
while condition:
    body
else:
    body
# runs always after loop unless forcibly stopped by break statement (continue has no effect on it)
# shouldn't be confused by if-else statement








# PASS
# Written to syntactically create a block (no use); meant for writing some code in a loop that is empty otherwise. Continue is completely different from pass.
# Scope of Variable
# Loops do not create any seperate scope.






# ITERATING WHILE MODIFYING A LIST
# Avoid
arr = [1, 2, 3, 4, 5]
for x in arr:
    if x % 2 == 0:
        arr.remove(x)
# Safer Approach 1
arr = [x for x in arr if x % 2 != 0]
# Safer Approach 2: iterate over a copy
for x in arr[:]:
    if x % 2 == 0:
        arr.remove(x)








# REAL UNDERSTANDING OF FOR LOOP
for x in arr:
    print(x)
# what it actually does
iterator = iter(arr)
while True:
    try:
        x = next(iterator)
        print(x)
    except StopIteration:
        break









# ITERABLE V/S ITERATOR
arr = [10, 20, 30]
it = iter(arr)
next(it) # 10
next(it) # 20
next(it) # 30 
next(it) # StopIteration
# Iterable: something that you can call
# list
# tuple
# string
# set
# dictionary
# range
# Iterator: An object that keeps track of its current position and supports: next()
