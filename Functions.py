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
