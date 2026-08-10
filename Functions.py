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
