# PRINT AND COMMENTS

# Single-line comment
"""
Multi-line string
Often used as a multi-line comment
"""
print("Hello")
print(10)
print(3.14)
print("Age:", 20) # No Space
print("A", "B", "C") # No Space
print("A", "B", "C", sep="-") # A-B-C
print("Hello", end=" ")
print("World") # Hello World
# By default each print gives output in following line




# VARIABLES
# Dynamically typed
x = 10
name = "Shaarav"
pi = 3.14
flag = True
int x = 10       # ❌
string name = "A"  # ❌
# Object has a type
x = 10
print(type(x)) # <class 'int'>
# Variable can point to a different type later
x = 10
x = "hello"
x = 3.14





# VARIABLE NAMING
# Python is case sensitive
# Valid
age = 20
_age = 20
age2 = 20
student_name = "A"
# Invalid
2age = 20       # ❌
student-name = "A"  # ❌
class = 10      # ❌ keyword









# MULTIPLE ASSIGNMENT
a, b, c = 1, 2, 3
a = b = c = 0







# SWAPPING VARIABLES
a, b = b, a








# BASIC DATA TYPES
a = 10             # int
b = 3.14           # float
c = 2 + 3j         # complex
d = True            # bool
e = "hello"         # str
f = None            # NoneType



# INTEGERS
x = 999999999999999999999999999999999999999
x = 2 ** 1000
print(x)
# Python integers have arbitrary precision. No normal C/C++-style integer overflow at a fixed bit width.





# FLOATING POINT
x = 3.14
y = 1.0
z = 5e3 # 5000.0
type(5e3) # float
print(0.1 + 0.2) # 0.30000000000000004: Don't assume decimal floating-point arithmetic is exact.




# COMPLEX NUMBER
z = 3 + 4j
z.real
z.imag
z.conjugate()





# BOOLEAN
x = True
y = False
print(True == 1) # True
print(False == 0) # True
print(int(True))   # 1
print(int(False))  # 0



# NONE
x = None
x is None
