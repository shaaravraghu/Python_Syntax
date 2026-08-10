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







# STRINGS
s = "Hello"
s = 'Hello'
s = '''Hello
World'''
s = """Hello
World"""
# Indexing
# P  y  t  h  o  n
# 0  1  2  3  4  5
# -6 -5 ...      -1
# Slicing
s[start:stop:step]
s[:3]     # "Pyt"
s[3:]     # "hon"
s[:]      # "Python"
s[::-1] # "nohtyP"
# Immutability
s = "hello"
s[0] = "H"     # ❌ TypeError
s = "H" + s[1:] # Immutability
# Concatenation
a = "Hello"
b = "World"
c = a + " " + b # Hello World
"abc" * 3 # abcabcabc




# ESCAPE SEQUENCES
\n    # newline
\t    # tab
\\    # backslash
\'    # single quote
\"    # double quote
# alternative raw string
path = r"C:\Users\test"


# f-STRING
name = "Shaarav"
age = 20
print(f"My name is {name} and I am {age}") # Variables
a = 10
b = 20
print(f"Sum = {a + b}") # Expressions
pi = 3.14159265
print(f"{pi:.2f}") # 3.14 Truncating Floating Point
x = 42
print(f"{x:5}") # Width
x = 0.756
print(f"{x:.2%}") # 75.60% Percentage







# INPUT
x = input()
print(type(x))
# <class 'str'>: Always takes input as string






# TYPE CONVERSION
x = int("123") # str to int
x = float("3.14") # str to float
str(123) 
str(3.14) # number to str
float(10) # 10.0: int to float
int(3.9) # 3
int(-3.9) # -3: float to int


# IMPORTANT INPUT PATTERNS
n = int(input()) # Single int
a, b = map(int, input().split()) # 2+ int
arr = list(map(int, input().split())) # Array
words = input().split() # multiple strings





# ARITHMETIC OPERATORS
+       # addition
-       # subtraction
*       # multiplication
/       # true division
//      # floor division: A // B = floor(A/B)
%       # modulo
**      # exponentiation












# OPERATOR PRECEDENCE
# Python operator precedence (highest → lowest)
# 1. Parentheses
()
# 2. Exponentiation
**
# 3. Unary operators
+x, -x, ~x
# 4. Multiplication, division, floor division, modulo
*, /, //, %
# 5. Addition and subtraction
+, -
# 6. Bitwise shifts
<<, >>
# 7. Bitwise AND
&
# 8. Bitwise XOR
^
# 9. Bitwise OR
|
# 10. Comparisons
<, <=, >, >=, ==, !=
in, not in
is, is not
# 11. Boolean NOT
not
# 12. Boolean AND
and
# 13. Boolean OR
or
# 14. Conditional expression
x if condition else y
# 15. Lambda
lambda






# == vs is
# == asks: Do these objects have equal values?
# is asks: Are these the exact same object?
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # True
print(a is b) # False
a = [1, 2, 3]
b = a
print(a == b) # True
print(a is b) # True









# BIT-WISE OPERATOR
&     # AND
|     # OR
^     # XOR
~     # NOT
<<    # left shift
>>    # right shift
# Short circuit evaluation of comparison elements!
# Left shift <<
5 << 1
# 0101 << 1  →  1010
# Result: 10
# Right shift >>
10 >> 1
# 1010 >> 1  →  0101
# Result: 5
x << n   # shift bits LEFT by n positions
x >> n   # shift bits RIGHT by n positions
x << n  == x * (2 ** n)
x >> n  == x // (2 ** n)










# TRUTHINESS
# Default False Values
False
None
0
0.0
""
[]
()
{}
set()

# Ternary Expression
x = a if (condition) else b






# BASIC BUILT-IN FUNCTIONS
abs() # returns value without sign
round() # rounds half (0.5) to even number (not always upwards)
pow(base, power) 
min()
max()
sum()
len()
type()
id()
divmod(dividend, divisor) # (quotient, remainder) == (a//b, a%b)

