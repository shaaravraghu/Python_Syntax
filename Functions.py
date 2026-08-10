# Defining a function
def function_name():
    # function body
    pass
# Example
def greet():
    print("Hello!")
greet() # Hello
# Functiom with parameters
def greet(name):
    print("Hello", name)
greet("Shaarav")
# Multiple parameters
def greet(name):
    print("Hello", name)
greet("Shaarav")
# Return
def add(a, b):
    return a + b
result = add(10, 20)
print(result) # 30
# Immediate function exit
def test():
    print("A")
    return
    print("B")
test()



# Return v/s Print
def f1(x):
    print(x)
def f2(x):
    return x
a = f1(10)
b = f2(10)
print(a)
print(b)
# 10
# None
# 10
# Python implicitely does return None for pass in functions







# Returning Multiple Values
def operations(a, b):
    return a + b, a - b, a * b
result = operations(10, 5)
print(result) # (15, 5, 50)
# unpack tuple
x, y, z = operations(10, 5)
print(x)
print(y)
print(z)










# Function Parameters
# Positional Parameters
def add(a, b):
    return a + b
add(2, 3)
# Keyword Arguments
add(a=2, b=3)
add(b=3, a=2)
# can change order
# mixing positional and keyword arguments
add(2, b=3) # valid
add(b=3, 2) # invalid








# Default Arguments
def greet(name="World"):
    print("Hello", name)
greet() # Hello World
greet("Shaarav") # Hello Shaarav
# Default Argument Trap with Mutable Element
def add_item(item, items=[]):
    items.append(item)
    return items
print(add_item(1)) # [1]
print(add_item(2)) # [1, 2]
print(add_item(3)) # [1, 2, 3]
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
print(add_item(1)) # [1]
print(add_item(2)) # [2]
print(add_item(3)) # [3]










# Positional-only parameters (ensures all parameters before / are positional)
def add(a, b, /):
    return a + b
add(2, 3) # valid
add(a=2, b=3) # invalid
# further example
def f(a, b, /, c, d):
    pass
# a, b → positional-only
# c, d → positional OR keyword










# Keyword-only parameters (ensures all parameters after * are keyword-based)
def greet(name, *, age):
    print(name, age)
greet("Shaarav", age=20) # Valid
greet("Shaarav", 20) # Invalid





# Combining / and *
def f(a, b, /, c, d, *, e, f):
    pass
# a, b       → positional-only
# c, d       → positional or keyword
# e, f       → keyword-only




# *args
# *args collects an arbitrary number of positional arguments into a tuple.
def add(*args):
    print(args)
add(1, 2, 3, 4) # (1, 2, 3, 4) 
# example
def add(*args):
    total = 0
    for x in args:
        total += x
    return total
print(add(1, 2, 3, 4)) # 10
# args is just a conventional name.







# **kwargs
# **kwargs collects arbitrary keyword arguments into a dictionary.
def show(**kwargs):
    print(kwargs)
show(name="Shaarav", age=20)
# {'name': 'Shaarav', 'age': 20}
def show(**kwargs): # for iteration
    for key, value in kwargs.items():
        print(key, value)











# Combined Example
def f(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
f(1, 2, 3, 4, 5, x=10, y=20)
# 1
# 2
# (3, 4, 5)
# {'x': 10, 'y': 20}









# Argument Unpacking
# List/ Tuple based
def add(a, b, c):
    return a + b + c
nums = [10, 20, 30]
# Dictionary based
def greet(name, age):
    print(name, age)
data = {
    "name": "Shaarav",
    "age": 20
}
greet(**data)
print(add(*nums))






# Functions as Objects
# A function can be assigned to a variable.
def greet():
    print("Hello")
x = greet # does not call the function.
x() # calls it.




# Passing Functions as Arguments
def square(x):
    return x * x
def apply(func, value):
    return func(value)
print(apply(square, 5))




