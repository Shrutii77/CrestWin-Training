# LEGB - it is name resolution hierarchy used to determine order which interpreter searches for variable name.

# it searches sequentially L->E->G->B if variable not fond in any of these then it raise NameError.
# if variable define in both local as well as global then it use local

# Local-
# Name define inside a current function or lambda expression

# enclosing-
# nested function.

# global-
# Name define at the top-level of the script or module. and inside as global. build in names that are preloaded(len(), print())

# Control Statement: control statements are used to change the flow of a program.

# Conditional Statements: Are used to make decision. 

# if: 
# it helps to check a given condition is True if it is then associate block of code is executed.
# elif: 
# it checks multiple condition one by one if any matches then it ignore the rest.  
# else: 
# if no conditions are true then it executes. 


# Loop Statement:- used to iterate a set of instructions multiple times for a given condition.

# for loop- it iterate the elements in a sequential way. it is used when finite value is given for iterating.

# while loop - it is used to iterate a block of code till a give condition remains True. it is used when we don't know the value how many 
# times we need to iterate.



# pathlib 

# It treats paths as objects rather than just strings, making your code much cleaner and cross-platform friendly.
# Automatically handles the diff. btw Windows (\) and Mac/Linux (/) slashes.  
# from pathlib import Path


# os 

# OS stands for the Operating System module in Python that allows the developers to interact with the operating system. It provides functions to perform tasks like file and directory manipulation, process management, and more. 
# We can modify the file permissions.

# Environment Variables: os.getenv("API_KEY") how you keep secrets out of your code.
# Listing Files: os.listdir('.')
# System Commands: os.system()


# sys

# sys provides variables and functions that interact strongly with the Python interpreter itself, rather than the operating system.
# sys.argv - A list of command-line arguments passed to a script.
# sys.argv[0] - is always the script name.
# sys.exit(), sys.path()
# It cannot modify the file permissions.


# os  vs  pathlib
# Join Paths        os.path.join(a, b)       a / b
# Get Filename      os.path.basename(p)      p.name
# Create Folder     os.mkdir(path)           p.mkdir(exist_ok=True)
# Check Existence   os.path.exists(p)        p.exists()


# import 

# import statement is how you bring external code into your current Python script. Instead of writing everything from scratch, you pull in modules or packages.

# return: The statement that exits the function and passes a value back. Without it the function returns None.


# *args: Collects extra positional arguments into a tuple.

# **kwargs: Collects extra named arguments into a dictionary.



# Default Argument

# A Default Argument is a parameter that assumes a default value if no value is provided in the function call.



# Keyword Arguments 

# Allow you to ignore the order of parameters when calling a function. use the name of the parameter & assign it a value using the =.
