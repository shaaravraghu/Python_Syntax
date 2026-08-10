# IF BLOCK
if condition:
    statement
if True:
    print("Runs")
if False:
    print("Doesn't run")
# Unlike C/C++/Java, Python uses indentation to define blocks.
# effectively evaluated as: 
bool(condition)










# ELSE AND ELIF BLOCKS
x = 10
if x > 10:
    print("Greater")
elif x == 10:
    print("Equal")
elif x > 0:
    print("Positive")
else:
    print("Negative")
# Python checks conditions top-to-bottom.
# As soon as one condition is true, its block executes and the remaining elif/else branches are skipped.
# Use elif when you have multiple mutually exclusive possibilities.
# Only one else is allowed for a particular if chain.
# else executes if none of the preceding conditions were true.





# MULTIPLE IF BLOCKS
x = 10
if x > 5:
    print("A")
if x > 8:
    print("B")
# if / elif / elif / else
#         ↓
# choose ONE branch
#         if
#         if
#         if
#         ↓
# each condition independently gets a chance






# TRUE/ FALSE USING AND/ OR
# returns value instead of True/ False when value is provided!
# CHAINED COMPARISONS
if 10 <= x <= 20:
if 10 <= x and x <= 20: # long form
a < b < c < d
a < b and b < c and c < d # long form
# a (value/ object) in b (object): True/ False


# NESTED TERNARY
result = (
    "A" if x > 90
    else "B" if x > 80
    else "C"
)
# equivalent form
if x > 90:
    result = "A"
elif x > 80:
    result = "B"
else:
    result = "C"







# WALRUS OPERATOR
if (n := len("Python")) > 5:
    print(n)
#  without walrus
n = len("Python")
if n > 5:
    print(n)
# common use case
while (line := input("Enter: ")) != "quit":
    print(line)










# MATCH/ CASE: SWITCH EQUIVALENT
# More powerful than switch: Because you can match structure + values + extract data at the same time.
# runs until 1st true case is hit (exempts other true/ false cases after 1st case hits true)
point = (0, 5)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print("On Y-axis:", y)
    case (x, 0):
        print("On X-axis:", x)
    case (x, y):
        print("Somewhere else:", x, y)
# point
#   ↓
# (0, 5)
# case (0, 0)   ❌
# case (0, y)   ✅
#               ↓
#              y = 5
#  Simpler way to remember
match value:
    case pattern:
        action
# case isn't necessarily asking:
# "Is this exactly equal to X?"
# It can ask:
# "Does this value have this particular structure?"
case 5:             # exactly 5
case (0, y):        # tuple: 0 followed by anything
case (x, 0):        # tuple: anything followed by 0
case [x, y, z]:     # list with exactly 3 items
case _:             # anything
# multiple patterns
match x:
    case 1 | 2 | 3:
        print("x is 1, 2, or 3")
    case _:
        print("something else")








