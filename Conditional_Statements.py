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
