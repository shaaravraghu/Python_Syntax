# A class is a blueprint.
# An object is an instance of that class.

class Person:
    pass
p1 = Person()
p2 = Person()
# Person  → class
# p1      → object
# p2      → object
type(p1)
isinstance(p1, Person)

class Dog:
    species = "Canis familiaris"
dog1 = Dog()
dog2 = Dog()
print(dog1.species) # Object referencing attributes of class
print(dog2.species) # Object referencing attributes of class

# Attributes can be attached to individual objects.
class Person:
    pass
p1 = Person()
p2 = Person()
p1.name = "Alice"
p2.name = "Bob"
print(p1.name)
print(p2.name)

# Constructor (add pre-defined data into objects instance of class) 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p = Person("Alice", 20)
print(p.name)
print(p.age)

# Self
class Person:
    def greet(self):
        print("Hello", self.name)

p = Person()
p.greet() # explicitely refers to Person.greet(p)

# An instance method operates on a particular object.
# Attributes defined directly inside the class belong to the class.

# @classmethod: A class method receives the class as its first argument, conventionally called 'cls'
class Person:
    species = "Human"

    @classmethod 
    def get_species(cls):
        return cls.species

# Class method as alternative constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))

p = Person.from_string("Alice,20") 

# @staticmethod
class Math:
    @staticmethod
    def add(a, b):
        return a + b
# When a function logically belongs to a class but doesn't need object/ class state.

# | Method   | Decorator       | First argument | Access instance? | Access class? |
# | -------- | --------------- | -------------- | ---------------- | ------------- |
# | Instance | none            | `self`         | ✅               | ✅            |
# | Class    | `@classmethod`  | `cls`          | ❌ directly      | ✅            |
# | Static   | `@staticmethod` | none           | ❌               | ❌            |

class Example:
    def instance_method(self):
        pass
    @classmethod
    def class_method(cls):
        pass
    @staticmethod
    def static_method():
        pass

