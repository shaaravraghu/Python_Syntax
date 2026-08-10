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







