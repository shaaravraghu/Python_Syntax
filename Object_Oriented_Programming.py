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

# Class Attribute v/s Instance Attribute
class User:
  var = None
  def __init__(self, name, age, email):
    self.name = name # converts parameters into instance attributes
    self.age = age
    self.email = email

user1 = User(Alice, 20, alice@example.com)
user2 = User(AliceBob, 25, bob@example.com)

class Username:
  def record(name, age, email):
  # name, age, and email are not attributes but parameters and belong to function and not class
  # to define attributes we either use instance attributes (constructor (__init__)- call class to handle) or class attributes (have to assign a value or var = None)

# We use self.var for instance attributes (inside __init__) and var for regular class attributes (top level of class)

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

# Inheritance: A class can inherit from another class.
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    pass
d = Dog()
d.speak() # Animal Speaks

# Method Overriding: Child class overrides Parent
class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    def speak(self):
        print("Woof")
d = Dog()
d.speak() # Woof

# Super: access parent implementation
class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")
# Animal sound
# Woof

# Super for parent and child constructor implementation
class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
d = Dog("Max", "Labrador")
print(d.name)
print(d.breed)

# Polymorphism and Interface
# Polymorphism means the same interface can work with different object types.
class Dog:
    def speak(self):
        return "Woof"
class Cat:
    def speak(self):
        return "Meow"
def make_sound(animal):
    print(animal.speak())
make_sound(Dog())
make_sound(Cat())
# No explicit type checking is necessary (Duck Typing).

# Encapsulation
# Python doesn't have Java-style strict private fields. Instead, it uses conventions and name mangling.
# Public
self.name
# Protected convention
self._name
# A single underscore means: "Internal use; don't rely on this externally."
# Private-ish attribute
self.__balance

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
account = BankAccount(1000)
account.__balance # doesn't work normally.

# Python performs name mangling:
account._BankAccount__balance

# Properties
# Properties allow you to make a method behave like an attribute.
class Person:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age

# Important Dunder Methods

__init__      # initialization
__new__       # object creation
__str__       # str(obj)
__repr__      # repr(obj)

__len__       # len(obj)

__getitem__   # obj[key]
__setitem__   # obj[key] = value
__delitem__   # del obj[key]

__contains__  # x in obj

__eq__        # ==
__ne__        # !=
__lt__        # <
__le__        # <=
__gt__        # >
__ge__        # >=

__add__       # +
__sub__       # -
__mul__       # *
__truediv__   # /
__floordiv__  # //
__mod__       # %
__pow__       # **

__iter__      # iter(obj)
__next__      # next(obj)

__enter__     # with
__exit__      # with

# Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
# Python internally calls:
p1.__add__(p2)

# Dataclasses
# Instead of writing boilerplate code:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Alternative
from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int
# Dataclasses automatically provide useful functionality such as initialization and a useful representation.
# Default values
@dataclass
class Person:
    name: str
    age: int = 18
# field()
from dataclasses import dataclass, field
@dataclass
class Student:
    name: str
    subjects: list = field(default_factory=list)
# subjects: list = [] # would create a shared mutable default, which is generally undesirable.

# Abraction
# Abstract Class: nominal typing
from abc import ABC, abstractmethod 
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
# Animal(): you cannot normally initiate this
# A subclass must implement the abstract method:
class Dog(Animal):
    def speak(self):
        return "Woof"
d = Dog()
print(d.speak())

# Abstract Class: structural typing
from typing import Protocol
class Speaker(Protocol):
    def speak(self) -> str:
        ...
class Dog:
    def speak(self) -> str:
        return "Woof"
# class Dog(Speaker): this is not needed anymore

# The important idea is:
# ABC → nominal typing
# Protocol → structural typing

# Composition
# Instead of:
class Car(Engine):
    ...
# you often want:
class Car:
    def __init__(self):
        self.engine = Engine()
# This represents: Car HAS-A Engine
# rather than: Car IS-A Engine

# Multiple Inheritence
class A:
    pass
class B:
    pass
class C(A, B):
    pass
# C inherits from both A and B.
