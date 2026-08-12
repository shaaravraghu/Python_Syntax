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

# Else Block
try:
    x = int("10")
except ValueError:
    print("Invalid")
else:
    print("Successfully converted:", x)
# The else block executes only if no exception occurred.

# Finally Block
# Finally executes regardless of whether an exception occurred. Always runs.
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
finally:
    print("Always runs")

# raise
raise ValueError("message")
# re-raises/ creates error when handeled by except or something else

# exception chaining
try:
    value = int("abc")
except ValueError as e:
    raise RuntimeError("Could not process input") from e

# suppressing exception context
try:
    int("abc")
except ValueError:
    raise RuntimeError("Invalid configuration") from None

# Custom Exceptions
class InsufficientFundsError(Exception):
    pass
raise InsufficientFundsError("Not enough money")

# Custom Exception with Data
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Balance={balance}, requested={amount}"
        )
try:
    raise InsufficientFundsError(100, 500)
except InsufficientFundsError as e:
    print(e.balance)
    print(e.amount)

