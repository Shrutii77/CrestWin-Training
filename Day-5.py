# Day-5
# (16/04/2026)


# super() :-

# super() function is used to call a method from parent(superclass) inside a child(subclass). It allows the child class to access and 
# extend the properties and methods of the parent class. It is commonly used in oops to achieve code reusability and to avoid redundancy.
# Works with single, multiple, and multilevel inheritance.

# class Parent():
#     def show(self):
#         print("Parent Class")
# class Child(Parent):
#     def show(self):
#         super().show()
#         print("Child")
        
# o=Child()
# o.show()



# Attributes:- 

# Attributes are the properties associated with the objects. access using dot (obj.attribute). It can be variable or methods are define
# within a class or instance of that class.

# Class Attributes:- A class is a blueprint for creating objects, and class attributes are variables that are associated with a class 
# rather than with instances (objects) of that class.
# - Define within class but outside methods
# - access by class name or instance
# - modification affect all instances

# Instance attributes:- instance attributes are variables that belong to an instance of a class.
# - Define within method (usually __init__)
# - access by instance only
# - affect only specific instance


# class Emp:
#     # Class attribute   
#     s = "Cf"     
#     def __init__(self, name, id):
#         # Instance attributes
#         self.name = name
#         self.id = id

# # Create two instances of the Emp class
# emp1 = Emp("Yon", 5)
# emp2 = Emo("Ren", 3)

# # Access the class attribute
# print(emp1.s)  # o/p: Cf
# print(emp2.s)  # o/p: Cf

# # Access the instance attributes
# print(emp1.name)  # o/p: Yon
# print(emp2.name)  # o/p: Ren


# Inheritance:-

# Inheritance allows a new class to inherit a property and behaviour from an existing class.

# Types:-
# 1 Single- A child class inherit from one parent class.
# 2 Multiple - A child class inherit from more than one parent class.
# 3 Multilevel- A child class inherit from parent class, which in turn inherits from another parent class.
# 4 hierarchical - More than one child class inherit from one parent class.
# 5 hybrid- combination of more than one type of inheritance.



# self :-

# It is a conventional name for first parameter of any instance method within a class. It allows to access and modify the attributes 
# and methods of that object.



# Dunder(magic) method:-

# It is special method with double underscore
# that enable operator overloading and custom object behavior.

# dir(int) lists all attributes and methods of the int class including dunder methods like __add__, __str__, etc. = print(dir(int))

# __init__ = Constructor It is the special method automatically called as soon as the object of that class is created.

# __repr__ = define official string representation of an object used for debugging. shows type & memory add. of obj. machine readable.

# __eq__ (self, other)= define the behaviour of the equality operator ==

# __str__ = str method is called when you use print() or str(). It should provide a simple, human-readable description of what the object is.
# def __str__(self):
#         return f "User: {self.name}"


# MRO :- 

# Method resolution order when the same method exists in more than one class in inheritance chain i.e. multiple than it decides which
# method should be taken 1st. occurs in diamond problem.


# staticmethod:-

# it doesn't takes cls and self as a 1st parameter. behave like a plain function in class namespace cos logically related to that class.



# classmethod:-

# cls as 1st parameter and work on itself. used to create "Factory Methods"—methods that return a class object for different use cases.

