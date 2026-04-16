# Day-3 (15/04/2026)

#Topics covered:-
# { • Data types: int, float, str, bool, None 
# • Collections: list, tuple, dict, set 
# • Comprehensions, unpacking, type() 
# • f-strings, string methods, slicing }


#  Data Type - Data types in Python are a way to classify data items.

# Integers- Value is represented by int class. It can be +ve or -ve whole no. (without fraction and decimal)
# a=12
# float-Value is represented by float class. It is a real no. with floating point representation. 
# a=0.9
# complex-Value is represented by complex class. it specified as (real part + imaginary part)j.
# a=2+4j

# List- It is used to store the elements defined as square brackets ([]) separated by commas (,). List is Mutable it means we can modify it after creating and It is ordered collection and allow duplicate values. It is slower than tuple due to mutability.
# eg:-
# a=[1,2,3]
# a.append(4)
# print(a)  # o/p= [1,2,3,4]

# list_1=[1,2,3]
# list_1.append([4,5,6])
# print(list_1)    # o/p= [1, 2, 3, [4, 5, 6]]
# l=[1,2,3]
# l.extend([4,5,6])
# print(l)  # o/p= [1, 2, 3, 4, 5, 6]

# l.insert(2,7)             
# print(l)  # o/p= [1, 2, 7, 3, 4, 5, 6]

# Tuple- It is used to store the elements defined by parenthesis () separated by commas , . Tuples are Immutable i.e. We can't change after creating it. It is the ordered collection and allows duplicate values. It is Faster than list due to immutability.
# eg:- 
# Fruits=("Apple","Mango","Grapes")
# print(Fruits)    # o/p=("Apple","Mango","Grapes")
 
# Set- Set are the unordered collection of elements and it can't be change and doesn't allow duplicate values. Elements are stored inside the curly braces {} separated by commas ,. Set are considered as dictionary so we use set() to change the datatype.
# eg:- 
# a={1,2,3} or a=set([1,2,3])

# a=set([1,2,3])
# print(type(a))    # o/p= <class 'set'>

# Dictionary- Dictionary are the key value pairs used to store the elements inside the curly braces {} separated by commas , .
# eg:- 
# a={"name","age"}
# b={"Yon",10}
# s=dict((c,d) for c,d in zip(a,b)) 
# print(s)   # o/p= {'name':'Yon', 'age':10}

# Comprehension= It is the Concise way of writing a list ,dict or anything which makes more readable and clean.
# n=[1,2,3,4]
# a=[i for i in n]
# print(a)    #o/p= [1, 2, 3, 4]

# type()= type() function used to identify the data types at a runtime like what kind of data.
# a="Hii"
# print(type(a))  # o/p= <class 'str'>

# packing - Collects multiple values into a single variable (list,tuple,dic). using (* for tuples/lists) and (** for dic). it happens in a func header (definition).
# eg :-
# def score(*args):
#     print("scores are: ", args)

# score(100, 200, 300, 400, "Team Win")  # o/p= scores are: (100,200, 300, 400, 'Team Win')


# unpacking- Extract all the values from the collection (list, tuple, dic) into individual variable. it happens in a function call
# def info(name, age):
#     print(f"I: {name}, Age: {age}")
# data = {"name": "Yon", "age": 30}
# info(**data)   # o/p= I: Yon, Age: 30

# f-string= f-string is a formatted string literals to make string formate easier. we can add variables and expressions inside the string using curly braces {}.
# name="Yon"
# print(f"YEah! {name} won")   # o/p= Yeah! Yon won

# literals= Constant data (fixed value written directly in the code). list, string and boolean literals are there :- string = " ", ' ', """ """.

# string methods:-
# upper()      replace()    
# lower()      split()  
# title()      index()      
# strip()      islower()

#eg:-
# a = "python"
# print(a.zfill(10))        # 0000python
# print(a.center(20, "-"))  # -------python-------
# print(a.ljust(15, "*"))   # python*********
# print(a.rjust(15, "*"))   # *********python

# a = "xxxpythonxxx"
# print(a.strip("x"))       # python

# a = "CrestWin-Training"
# print(a.partition("-"))   # ('CrestWin', '-', 'Training')

# Slicing - Slicing is fundamental concept that let us easily access specific elements in a list.
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[1:4])  # o/p= [2, 3, 4]


