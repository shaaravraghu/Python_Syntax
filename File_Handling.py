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

# File Modes
open("data.txt", "r")
# r   read text
# w   write text
# a   append text
# x   cretae file if doesn't exist
# rb  read binary (preferable for non-text files)
# wb  write binary (preferable for non-text files)

