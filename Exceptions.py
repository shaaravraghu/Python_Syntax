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

# Multiple Except Blocks
try:
    x = int(input("Enter number: "))
    result = 10 / x

except ValueError:
    print("Invalid integer")

except ZeroDivisionError:
    print("Cannot divide by zero")
# Multiple Errors in a Single Except Block
try:
    ...
except (ValueError, TypeError):
    print("Invalid input")

# Accessing the Exception Class
try:
    x = int("abc")
except ValueError as e:
    print(e)
    print(type(e))
    print(str(e))
