#  Dictionary: stores key-value pairs
d = {
    "name": "Shaarav",
    "age": 21,
    "company": "Anthropic"
}
d = {
    "name": "Shaarav",
    21: "hello",
    True: 100,
    3.14: [1, 2, 3]
}








# Creating Dictionaries
d={}
d=dict()
d = {
    "a": 10,
    "b": 20
}
d = dict(name="Shaarav", age=21)
# from pairs
d = dict([
    ("a", 1),
    ("b", 2),
    ("c", 3)
])
# {"a": 1, "b": 2, "c": 3}





# Accessing Values
d[key]
# KeyError if key doesn't exist
d.get(key) # returns None if key not found and value if key exists
dictionary.get(key, default) # if needed set a default value





# Adding a key
d = {}
d["name"] = "Shaarav"
d["age"] = 21
#  Updating a value
d[key] = value
# multiple updates at the same time using update
d.update({
    "age": 22,
    "city": "Bangalore"
})
# Update with another dictionary
a = {"x": 1, "y": 2}
b = {"y": 20, "z": 3}
a.update(b)
print(a)




# Checking key existence
key in/ not in dictionary # True/ False
# Getting all the keys
d.keys()
# dict_keys(['a', 'b', 'c'])
list(d.keys())
# Getting all the values
d.values()
list(d.values())
# Getting key-value pairs
d.items()
# ('a', 1)
# ('b', 2)







# Iterating through a dictionary
# Keys
for key in d:
    print(key)
for key in d.keys():
    print(key)
# Values
for value in d.values():
    print(value)
# Key-Value Pairs
for key, value in d.items():
    print(key, value)








# Deletion
del d["key"]
del d # dictionary completely deleted
value = d.pop(key)
value = d.pop(key, value) # instead of raising KeyError if key not found
d.popitem() # removes and returns last inserted key-value pair
d.clear() # {}
len(d)
