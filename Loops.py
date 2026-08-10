# 1. for loop   → iterate over a sequence/iterable
# 2. while loop → repeat while a condition remains true

# FOR LOOP OVER RANGE
for variable in iterable:
    statement
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
