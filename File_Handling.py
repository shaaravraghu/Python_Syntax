# with: context managers
# Most important Python constructs for file handling.
# Instead of:
file = open("data.txt")
try:
    data = file.read()
finally:
    file.close()
# Uses:
with open("data.txt") as file:
    data = file.read()


