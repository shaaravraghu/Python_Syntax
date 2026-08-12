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

# Encoding
with open("data.txt", "r", encoding="utf-8") as f:

# File Position
# current position:
f.tell()
# move to:
f.seek(0)

# File Existance
if path.exists():
if path.is_file():
if path.is_dir():

# Serialisation
# Serialization means converting an object/data structure into a format that can be stored or transmitted.
# Conceptually:
# Python object
#      ↓
# serialization
#      ↓
# bytes / text
# And back:
# serialized data
#      ↓
# deserialization
#      ↓
# Python object
# Common formats:
# JSON
# Pickle
# CSV

# JSON Files
# Python Object -> JSON
import json
data = {
    "name": "Alice",
    "age": 20
}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
# JSON -> Python Object
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# JSON-Supported Python Types
# Common mappings:
# Python	JSON
# dict	    object
# list	    array
# str	    string
# int	    number
# float	    number
# True	    true
# False	    false
# None	    null

