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

# Reading a File
# Entire File
with open("data.txt", "r") as f:
    content = f.read()
# Fixed Number of Characters
with open("data.txt", "r") as f:
    data = f.read(10)
# readline()
with open("data.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline() # call multiple times if needed
    # string ends with \n
# readlines()
with open("data.txt", "r") as f:
    lines = f.readlines()
    # creates list with strings (with \n)
# Remove /n escape sequence
with open("data.txt") as f:
    for line in f:
        line = line.strip()
        print(line)
# Itertae over a File
with open("data.txt", "r") as f:
    for line in f:
        print(line)


# Writing a File
# write()
with open("output.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")
# writelines()
with open("output.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")
