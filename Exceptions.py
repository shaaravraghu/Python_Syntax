# An exception occurs when Python encounters an error during execution.
# Try/ Except
try:
    # code that may fail
except:
    # handle failure
# Example
try:
    x = 10 / 0
except:
    print("Something went wrong")
# Better: catch the specific exception
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
