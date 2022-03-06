# PROGRAMIZ PYTHON TUTORIAL CHEATSHEET
#author-monks_mojo
#date-20th september 2019


# Python Comments
# Comments are very important while writing a program. It describes what's going on inside a program so that a person looking at the source code does not have a hard time figuring it out. You might forget the key details of the program you just wrote in a month's time. So taking time to explain these concepts in form of comments is always fruitful.

# In Python, we use the hash
# (#) symbol to start writing a comment.

# It extends up to the newline character. Comments are for programmers for better understanding of a program. Python Interpreter ignores comment.

# This is a comment
# print out Hello
print('Hello')

# Multi-line comments
# If we have comments that extend multiple lines, one way of doing it is to use hash (#) in the beginning of each line. For example:

# This is a long comment
# and it extends
# to multiple lines
# Another way of doing this is to use triple quotes, either ''' or """.

# These triple quotes are generally used for multi-line strings. But they can be used as multi-line comment as well. Unless they are not docstrings, they do not generate any extra code.

"""This is also a
perfect example of
multi-line comments"""

# INTRODUCTION TO PYTHON
# PYTHON IS A CROSS PLATFORM PROGRAMMING LANGUAGE MEANS IT CAN RUN ON MULTIPLE OS LIKE WINDOWS, MACos & LINUX
# ITS FREE AND OPEN SOURCE
# PYTHON FILES ARE ALWAYS CREATED WITH THE .py EXTENSION
# TO RUN A PYTHON FILE IN CMD/TERMINAL WRITE
# python <filename>.py

# YOUR FIRST PYTHON SCRIPT
print("hello world!")

# python keywords
# keywords are the reserved meaning in python
# we cannot use keywords as a variable name function name or as a identifier.
# they are used to define syntax and structure of python language and hold a specific meaning keyword in python are case sensitive.

# there are approx 33 keyword in the python language

# all the keywords except True, False & None are in lowercase.
# example of keywords in python
# 1.finally
# 2.class
# 3.return
# 4.try
# 5.while

# python identifier

# an identifier is a name given to entities like class function variables etc.
# it helpus to differentiate diffrent entities

# Rules for writing identifiers

# 1. Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore _. Identifier can be of any length.


# 2. Names like myClass, var_1 and print_this_to_screen, all are valid example.

# 3.An identifier cannot start with a digit. 1variable is invalid, but variable1 is perfectly fine.

# 4. Keywords cannot be used as identifiers.
# for ex-
# global=1; //this will give invalid syntax error

# 5.We cannot use special symbols like !, @, #, $, % etc. in our identifier. for ex-h@llo=10// invalid syntax error.

# Things to Remember
# Python is a case-sensitive language. This means, VAR and var are not the same. Always name identifiers that make sense.


# Multiple words can be separated using an underscore, this_is_a_long_variable.

# PYTHON STATEMENTS
# Instructions that a Python interpreter can execute are called statements. For example, a = 1 is an assignment statement.

# Multi-line statement
# # In Python, end of a statement is marked by a newline character. But we can make a statement extend over multiple lines with the line continuation character (\). For example:
a = 1+2+3+4 +\
    5+6+7+8 +\
    10
print("value of a=", a, "using explicit line continuation")

# using \ is the explicit way to show line continuation
# we can also implement using
# In Python, line continuation is implied inside parentheses ( ), brackets [ ] and braces { }. For instance, we can implement the above multi-line statement as

a = (1+2+3+4 +
     5+6 +
     7+8+10)
print("value of a=", a, "using explicit line continuation")

# in python its not a good practice to   use ;(semicolon) after every statement.

# in python we use semicolon to put multiple statements in a single line using semicolons, as follows

a = 1
b = 2
c = 3

# Python Indentation
# Most of the programming languages like C, C++, Java use braces { } to define a block of code. Python uses indentation.

# A code block (body of a function, loop etc.) starts with indentation and ends with the first un indented line. The amount of indentation is up to you, but it must be consistent throughout that block.

# Generally four whitespaces are used for indentation and is preferred over tabs. Here is an example.

for i in range(1, 101):
    print(i)
    if(i == 5):
        break

# Docstring in Python

# Docstring is short for documentation string.

# It is a string that occurs as the first statement in a module, function, class, or method definition. We must write what a function/class does in the docstring.
# Triple quotes are used while writing docstrings. For example:


def double_function(num):
    """Function to double the value"""
    print(2*num)


print(double_function.__doc__, "of 10")
double_function(10)

# Python Variables

# A variable is a named location used to store data in the memory. It is helpful to think of variables as a container that holds data which can be changed later throughout programming. For example,

number = 10
print(number)
# here we created a variable name number to which we can assign the value.

# a variable value can be changed
number = 0.1
print(number)

# Initially, the value of number was 10. Later it's changed to 1.1.
# we can assign value to the operator using assignment operator

# Note: In Python, we don't assign values to the variables, whereas Python gives the reference of the object (value) to the variable.

# changing the value of the variable using assignment operator
website = "apple.com"
print(website)
website = "google.com"
print(website)

# Note : Python is a type inferred language; it can automatically know apple.com is a string and declare website as a string.

# either python is loosely typed either the type of the variable or the value that variable holds is known when the statement is interprated

# example to assign multiple value to the multiple variables

a, b, c = 10, 0.6, "snake & ladders"
print("a= ", a, "b= ", b, "c= ", c)

# we can also assign same value to multiple variable

a = b = c = 10
print("a= ", a, "b= ", b, "c= ", c, "are all same")

# Constants
# A constant is a type of variable whose value cannot be changed. It is helpful to think of constants as containers that hold information which cannot be changed later.

# in python the CONSTANTS are declared in seprate module and the we import module to the main file

# for ex-:9
# create a file constant.py
# declare constants in it
# like
PI = 3.14
GRAVITY = 9.8
# import constant.py file in main file
# print the constants
print("printing the constants")
print(PI)
print(GRAVITY)

# Literals
# Literal is a raw data given in a variable or constant. In Python, there are various types of literals they are as follows:

# Numeric Literal
# Numeric Literals are immutable (unchangeable). Numeric literals can belong to 3 different numerical types Integer, Float and Complex.

a = 0b1010  # binary literal
b = 100  # decimalliteral
c = 0o310  # octal literal
d = 0x12c  # hexadecimal literal

print("a value hold binary literal converted to decimal", a)
print("b value hold decimal literal", b)
print("c value hold octal literal converted to decimal", c)
print("d value hold hexadecimal literal converted to decimal", d)

# float literal
float_1 = 10.5
float_2 = 1.5e2  # 1.5*10^2
print("value of float_1 literal", float_1)
print("value of float_2 literal", float_2)

# complex literal
x = 3.14j
print("complex literal value", x)
print("real_part =", x.real)
print("imaginary part=", x.imag)

# String literals

# A string literal is a sequence of characters surrounded by quotes. We can use both single, double or triple quotes for a string. And, a character literal is a single character surrounded by single or double quotes.

string_literal = "this is python string"
character_literal = 'c'
print("the string literal is", string_literal)
print("the character literal is", character_literal)
multiline_string = '''hello today i am gonna show you->
the multiline string->
present in python'''
print("multiline string in python")
print(multiline_string)

# We can use the slicing operator [ ] to extract an item or a range of items from a string. Index starts form 0 in Python
print("string length-", len(string_literal))
print("string_literal[0:4]-", string_literal[0:4])
print("string_literal[7:]", string_literal[7:])
print("string_literal[:len(string_literal)]",
      string_literal[:len(string_literal)])
# strings are immutable in nature so below command will cause an error
#string_literal[22] = 's'

# Boolean literals

# A Boolean literal can have any of the two values: True or False.

x = (1 == True)  # since value of true=1 it will return 1
y = (1 == False)  # since value of false=0 it will return 0 as 1!=0
a = True+1  # 2
b = False+5  # 5
print("boolean literal")
print("x is ", x)
print("y is", y)
print("a is", a)
print("b is", b)

# special literal(None Literal)
# python contains one special literal i.e None. We use to give null value to it
# for ex
drink = "available"
food = None


def menu(item):
    if item == drink:
        print(drink)
    else:
        print(food)


print("use of none literal")
menu(drink)
menu(food)


# Data Types in python
# Every value in python has a datatype Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.

# There are various data types in Python. Some of the important types are listed below.

# 0. python number
# Integers, floating point numbers and complex numbers falls under Python numbers category. They are defined as int, float and complex class in Python.

# We can use the type() function to know which class a variable or a value belongs to and the isinstance() function to check if an object belongs to a particular class.

a = 5  # integer
print(a, "is of type", type(a))

a = 2.0  # float
print(a, "is a type of", type(a))
# A floating point number is accurate up to 15 decimal places. Integer and floating points are separated by decimal points. 1 is integer, 1.0 is floating point number.

a = 1+2j  # complex
print(a, "is it complex number ? \n ans:", isinstance(a, complex))

# Literal Collections
# there are four different literals collection like list,set,tuple,dictionary..


# 1. python list
# list is an orered sequence of item(WE CAN PERFORM SLICING OPERATION ON LIST BECAUSE THEY ARE ORDERED). it is one of the most used data type in the python and is very flexible.
fruit = ["apple", "orange", "banana"]

# all the items in the list do not to be of same type
list1 = [1, 2.8, "python-list"]
print("python list1-", list1)

print("list literal- ", fruit)
# We can use the slicing operator [ ] to extract an item or a range of items from a list. Index starts form 0 in Python
print("slicing example on fruit & list1")
print("list1[0]-", list1[0])  # 1 index start from 0
print("list1[0:3]-", fruit[0:3])  # apple orange banana
print("list1[1:2]-", fruit[1:2])  # start from index 1 to (2-1)
print("list1[1:]-", fruit[1:])  # orange banana
print("list1[:3]", fruit[:3])  # apple orange banana

# python list are mutable
fruit[2] = "mangos"
print("printing fruit list to show mutability \n", fruit)

# 2. python tuple
# Tuple is an ordered sequence of items same as list.The only difference is that tuples are immutable. Tuples once created cannot be modified.

# Tuples are used to write-protect data and are usually faster than list as it cannot change dynamically.

# It is defined within parentheses () where items are separated by commas.
number = (10, 20, 30, 30)
print("tuple literal-", number)

# all the elements of the tuple can be of diffrent types
tuple1 = (1.0, 6, "HelloTuple")
# We can use the slicing operator [] to extract items but we cannot change its value.
print("tuple1[2]-", tuple1[2])
print("tuple1[0:3]-", tuple1[0:3])

# 3. python dictionary
# Dictionary is an unordered collection of key-value pairs.

# It is generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data. We must know the key to retrieve the value.

# In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value. Key and value can be of any type.

alphabets = {"a": "apple", "b": "ball", "c": "cat"}
print("dictionary literal", alphabets)
print("type of alphabets-", type(alphabets))
print("alphabets['a']-", alphabets["a"])
print("alphabets['b']-", alphabets["b"])

# 4. python set
# Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }. Items in a set are not ordered.
# We can perform set operations like union, intersection on two sets. Set have unique values. They eliminate duplicates.
vowels = {"a", "e", "i", "o", "u"}
set1 = {5, 2, 3, 3, 4, 6}
print("set literal-", vowels)
print("set1-", set1)
# Since, set are unordered collection, indexing has no meaning. Hence the slicing operator [] does not work. so below statement will give error
# print(set1,set[1])

# we can also convert one one data type to another
print("converting", 5, "int to float", float(5))
print("converting", 5.0, "float to int", int(5.0))
print("converting", 100, "int to string", str(5.0))
# you can't convert string to int the following code will give error
# >>> int('12po')

# converting string to a list
print("converting string-"+'"cool mamba"'+"to list", list("cool mamba"))
# converting list to tuple
print("converting list", [10, 11.56, "hello"],
      "to tuple", tuple([10, 11.56, "hello"]))

# we can also convert list to set, tuple to set & # and vice versa

# list to dict
print("converting list", [[1, 2], [3, 4]], "to dict", dict([[1, 2], [3, 4]]))


# type conversion
# the process of converting the value of one data type of one value to another data type is called type conversion.
# python has two type of type conversion
# 1. implicit type conversion
# 2. explicit type conversion

# Implicit Type Conversion:
# In Implicit type conversion, Python automatically converts one data type to another data type. This process doesn't need any user involvement.

# Let's see an example where Python promotes conversion of lower datatype (integer) to higher data type (float) to avoid data loss.

num_int = 30
num_float = 10.87
print("implicit type conversion")
print(num_int, type(num_int))
print(num_float, type(num_float))
print(num_int+num_float, type(num_int+num_float))

num_int = 30
num_string = "456"
print(type(num_int))
print(type(num_string))
print("adding THESE two will give error TypeError: unsupported operand type(s) for +: 'int' and 'str' ")
print("However Python has the solution for this type of situation which is know as Explicit Conversion.")

# In the above program,

# We add two variable num_int and num_str.
# As we can see from the output, we got typeerror. Python is not able use Implicit Conversion in such condition.
# However Python has the solution for this type of situation which is know as Explicit Conversion.
print("adding them using explicit type casting will solve the problem")
# Explicit Type Conversion:
# In Explicit Type Conversion, users convert the data type of an object to required data type. We use the predefined functions like int(), float(), str(), etc to perform explicit type conversion.

# This type conversion is also called typecasting because the user casts (change) the data type of the objects.

# Syntax :


# Typecasting can be done by assigning the required data type function to the expression.
# declared above
# num_int=123
# num_str="456"
# adding them with the help of explicit type conversion
num_string = int(num_string)
print("num_string coverted to int using explicit type casting")
print(num_string+num_int)
print(type(num_int+num_string))

# Python Input, Output and Import
# Python provides numerous built-in functions that are readily available to us at the Python prompt.

# Some of the functions like input() and print() are widely used for standard input and output operations respectively. Let us see the output section first.

# We use the print() function to output data to the standard output device (screen).

# We can also output data to a file, but this will be discussed later. An example use is given below.

print("the sentence will be output to the screen")
# Output: this sentence will be output to the screen
a=5
print("the value of a is",a)#5

# The actual syntax of the print() function is

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# Here, objects is the value(s) to be printed.

# The sep separator is used between the values. It defaults into a space character.

# After all values are printed, end is printed. It defaults into a new line.

# The file is the object where the values are printed and its default value is sys.stdout (screen). Here are an example to illustrate this.

print(1,2,3,4)
# output: 1 2 3 4

print(1,2,3,4,sep="*")
# output: 1*2*3*4

print(1,2,3,4,sep="$",end="&")
#output: 1$2$3$4$5&

# Output formatting
# Sometimes we would like to format our output to make it look attractive. This can be done by using the str.format() method. This method is visible to any string object.
# Here the curly braces {} are used as placeholders. We can specify the order in which it is printed by using numbers (tuple index).

x=5; y=10
print("the value of x is {0} and y is {1}".format(x,y))

print("i love {0} and {1}".format('bread','butter'))

print(" love bread {1} and butter {0}".format('bread','butter'))

# Python Input
# Up till now, our programs were static. The value of variables were defined or hard coded into the source code.

# To allow flexibility we might want to take the input from the user. In Python, we have the input() function to allow this. The syntax for input() is
print("welcome please register")
name=input("please enter your name")
phone_no=input("enter your phone no.")
weight=input("please enter the weight")
print("successfully registered")
print("welcome {0} you have registered successfully".format(name))
print("your phone no is {0} & your weight is {1}".format(phone_no,weight))

# Python import
# When our program grows bigger, it is a good idea to break it into different modules.

# A module is a file containing Python definitions and statements. Python modules have a filename and end with the extension .py.

# Definitions inside a module can be imported to another module or the interactive interpreter in Python. We use the import keyword to do this.

# For example, we can import the math module by typing in import math.

# import math
# print(math.pi)
# >>#output: 3.14

# What are operators in python?
# Operators are special symbols in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.

# Arithmetic operators
# Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication etc
x=15
y=2

print("x={0} y={1} x+y--> {2}".format(x,y,x+y))
# +	Add two operands or unary plus

print("x={0} y={1} x-y--> {2}".format(x,y,x-y))
# - Subtract right operand from the left or unary minus

print("x={0} y={1} x*y--> {2}".format(x,y,x*y))
# * multiply two operand
x=float(x)
y=float(y)

print("x={0} y={1} x/y--> {2}".format(x,y,x/y))
# /	Divide left operand by the right one (always results into float)

print("x={0} y={1} x%y--> {2}".format(x,y,x%y))
# %	Modulus - remainder of the division of left operand by the right

print("x={0} y={1} x//y--> {2}".format(x,y,x//y))
# //	Floor division - division that results into whole number adjusted to the left in the number line
print("x={0} y={1} x**y--> {2}".format(x,y,x**y))
# **	Exponent - left operand raised to the power of right

# Comparison operators

# Comparison operators are used to compare values. It either returns True or False according to the condition.



#  > 	Greater that - True if left operand is greater than the right 	x > y
print("x={0} y={1} x>y --> {2}".format(x,y,x>y))
# True

#  < 	Less that - True if left operand is less than the right 	x < y
print("x={0} y={1} x<y --> {2}".format(x,y,x<y))
# False

# == 	Equal to - True if both operands are equal 	x == y
print("x={0} y={1} x==y --> {2} ".format(x,y,x==y))
#False

# != 	Not equal to - True if operands are not equal 	x != y
print("x={0} y={1} x!=y -->{2}".format(x,y,x!=y))
#True

# >= 	Greater than or equal to - True if left operand is greater than or equal to the right 	x >= y
print("x={0} y={1} x>=y--> {2}".format(x,y,x>=y))
# True

# <= 	Less than or equal to - True if left operand is less than or equal to the right 	x <= y
print("x={0} y={1} x<=y---> {2}".format(x,y,x<=y))
# False

# Logical Operator
x=True
y=False

# and---True if both the operands are true	x and y
print("x-{0} & y-{1} is -{2}".format(x,y,x and y))
# output: x and y is False

# or---True if either of the operands is true	x or y
print("x-{0} or y-{1} is -{2}".format(x,y,x or y)
)
# output: x or y is True
 
# not---True if operand is False (complements the operand) not x
print("x is {0} so not {1} is {2}".format(x,x,not x))

# Bitwise Operator

# Bitwise operators act on operands as if they were string of binary digits. It operates bit by bit, hence the name.

# For example, 2 is 10 in binary and 7 is 111.

# In the table below: Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)
x=10
y=4

print("x is {0} y is {1} x & y (in decimal) will be -->{2}".format(x,y,x & y))
# &	Bitwise AND	x& y = 0 (0000 0000)

print("x is {0} y is {1} x | y (in decimal) will be -->{2}".format(x,y,x | y))
# |	Bitwise OR	x | y = 14 (0000 1110)

print("x is {0} so ~ x will be {1}".format(x,~x))
# ~	Bitwise NOT	~x = -11 (1111 0101)

print("x is {0} and  y is {1} so x 'xor' y will be {2} ".format(x,y, x^y))
# ^	Bitwise XOR	x ^ y = 14 (0000 1110)

print("bitwise right shift of x -{0} to 2 bits  will be -{1}".format(x,x>>2))
# >> Bitwise right shift (x = 10 (0000 1010 in binary))	x>> 2 = 2 (0000 0010)

print("bitwise left shift operator of x-{0} to 2 bits will be -{1}".format(x,x<<2))
# << Bitwise left shift (x = 10 (0000 1010 in binary))	x<< 2 = 40 (0010 1000)

# Special operators
# Python language offers some special type of operators like the identity operator or the membership operator. They are described below with examples.

# Identity operators
# is and is not are the identity operators in Python. They are used to check if two values (or variables) are located on the same part of the memory. Two variables that are equal does not imply that they are identical.

# Identity operators in Python

# Operator	Meaning	Example
# is	True if the operands are identical (refer to the same object)	x is True

# is not	True if the operands are not identical (do not refer to the same object)	x is not True
#example
x1= 5
y1= 5
x2= 'hello'
y2= 'hello'
x3= [1,2,3]
y3= [1,2,3]

print("IDENTITY OPERATOR IN PYTHON")
print("x1 is {0} and y1 is {1} then 'x1 is y1' is {2}".format(x1,y1,x1 is y1))#True
# Here, we see that x1 and y1 are integers of same values, so they are equal as well as identical because the integer 5 act as object. 

print("x2 is {0} y2 is {1} then 'x1 is not y1' is {2}".format(x2,y2,x2 is not y2))#false
# Here, we see that x2 and y2 are string literals, so they are equal as well as identical because the string literal act as object. 

print("x3 is {0} y3 is {1} then 'x3 is y3' is {2}".format(x3,y3,x3 is y3))#false
# But x3 and y3 are list. They are equal but not identical. It is because interpreter locates them separately in memory although they are equal.


# Membership operators
# in and not in are the membership operators in Python. They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).

# In a dictionary we can only test for presence of key, not the value.

# Operator	Meaning	Example
# in	True if value/variable is found in the sequence	

# not in	True if value/variable is not found in the sequence

x='hello world'
print("x is {0} so is 'h in x' will be {1}".format(x,'h' in x))#True
print("'HELLO' in x{0} will be {1}".format(x,'HELLO' in x))#False

# Python Namespace and Scope

# Name (also called identifier) is simply a name given to objects. Everything in Python is an object. Name is a way to access the underlying object.

# For example, when we do the assignment a = 2, here 2 is an object stored in memory and a is the name we associate it with. We can get the address (in RAM) of some object through the built-in function, id(). Let's check it.

a=2 #2 integer is the object
print("id() of a =",a,"will be",id(a))#
print("id() of 2 will be",id(2))
print("a=a+1 =",a+1)
print("now the id of a",a,"will be",id(a))
print("id() of 3",id(3))
b=2
print("id of b",b,"will be",id(b))

# Functions are objects too, so a name can refer to them as well.
def printHello():
    '''printHello function is an object in python'''
    print("inside printHello function")
print(printHello.__doc__)    
printHello()
print("id of printHello function will be",id(printHello))

# namespace
# In Python, you can imagine a namespace as a mapping of every name, you have defined, to corresponding objects.

# Different namespaces can co-exist at a given time but are completely isolated.

# A namespace containing all the built-in names is created when we start the Python interpreter and exists as long we don't exit.

# This is the reason that built-in functions like id(), print() etc. are always available to us from any part of the program. Each module creates its own global namespace.

# These different namespaces are isolated. Hence, the same name that may exist in different modules do not collide.

# Modules can have various functions and classes. A local namespace is created when a function is called, which has all the names defined in it. Similar, is the case with class. Following diagram may help to clarify this concept.

# Nested Namespaces in Python Programming

# Python Variable Scope
# Although there are various unique namespaces defined, we may not be able to access all of them from every part of the program. The concept of scope comes into play.

# Scope is the portion of the program from where a namespace can be accessed directly without any prefix.

# At any given moment, there are at least three nested scopes.

# 1. Scope of the current function which has local names
# 2. Scope of the module which has global names
# 3. Outermost scope which has built-in names
# When a reference is made inside a function, the name is searched in the local namespace, then in the global namespace and finally in the built-in namespace.

# If there is a function inside another function, a new scope is nested inside the local scope.


def outer_function0():
    '''calling of outer_function0()'''
    b=90
    print("value of b in outer_function0()",b)
    def inner_function0():
        '''calling of inner_function0()'''
        b=60
        print("value of b in inner_function0()",b)
    print(inner_function0.__doc__)
    inner_function0()
b=30
print(outer_function0.__doc__)
outer_function0()
print("inside built-in namespace")
print("value of b inside built-in namespace",b)

#the use of global keyword
# global keyword helps you to refer to the variable declared in global/built-in namespace
 
# Here, all reference and assignment are to the global a due to the use of keyword global.


def outer_function1():
    ''' calling of outer_function1() '''
    global a
    a=20
    print("indside outer_function1() a=",a)

    def inner_function1():
        '''calling of inner_function1()'''
        global a
        a=40
        print("inside inner_function1() a=",a)
    print(inner_function1.__doc__)    
    inner_function1()    
a=80
print(outer_function1.__doc__)
outer_function1()
print("inside built-in namespace")
print("value of a inside built-in namespace",a)

# Python if...else Statement

# Decision making is required when you want to execute a certain condition is satisfied

# if (condition):
#     print("if above condition is true this block will be executed")
# else:
#     print("if condition is false else block will be executed")

# Python interprets non-zero values as True. None and 0 are interpreted as False.

num =3
if num>0:
    print("num is greater than 0")
print("end of if block 1 this will be always be executed")

if num <3:
    print("num is less than zero")
print("end of if block 2 this will always will be executed")    


# you can declare an if block alone 
# or a if block immediately followed by else block 
# or if block followed by multiple elif block and the else block

num=int(input("enter a number :"))


# while taking input the system by default take input in string format so make sure to type cast into required data type

if (num > 0):
    print("number is positive")
elif (num < 0):
    print("number is negative")
else:
    print("number is equal to 0")        

# If all the conditions are False, body of else is executed.

# Only one block among the several if...elif...else blocks is executed according to the condition.

# The if block can have only one else block. But it can have multiple elif blocks.


# Python Nested if statements

# We can have a if...elif...else statement inside another if...elif...else statement. This is called nesting in computer programming.

# Any number of these statements can be nested inside one another. Indentation is the only way to figure out the level of nesting. This can get confusing, so must be avoided if we can.

num=float(input("enter a number:"))
if(num >= 0):
    if(num == 0):
        print("number is zero")
    else:
        print("number is positive")
else:
    print("number is negative")

#Python for loop

# the for loop in python is use to traverse or iterate through list tuple strings
# Syntax
# for val in sequence:
#     print(val)
# Here, val is the variable that takes the value of the item inside the sequence on each iteration.

# Loop continues until we reach the last item in the sequence. The body of for loop is separated from the rest of the code using indentation

#programs to find the sum of all the numbers stored in the list

#list of numbers
numbers=[6,5,3,9,7,2,1]
sum=0
print("sum of the list {0} using the for loop".format(numbers))
for number in numbers: 
    sum+=number
print("sum of the number list-{0} is {1}".format(numbers,sum))

# The range() function
# We can generate a sequence of numbers using range() function. range(10) will generate numbers from 0 to 9 (10 numbers).

# We can also define the start, stop and step size as range(start,stop,step size). step size defaults to 1 if not provided.

# This function does not store all the values in memory, it would be inefficient. So it remembers the start, stop, step size and generates the next number on the go.

# To force this function to output all the items, we can use the function list().

# some range example
print(range(1,10))

#converting the above range into list
range_list=list(range(0,10))
print(range_list)

#(start,stop-1)
print(list(range(5,16)))

#(start,stop-1,step size)
print(list(range(2,22,2)))  


genres=['blues','rock','jazz','techno']
# string list with for loop
print("traversing string list")
for genre in genres:
    print("I love",genre)

# We can use the range() function in for loops to iterate through a sequence of numbers. It can be combined with the len() function to iterate though a sequence using indexing. Here is an example.

#programs to iterate through a list using indexing

for i in range(len(genres)):
    print("I like",genres[i])

# for loop with else

# A for loop can have an optional else block as well. The else part is executed if the items in the sequence used in for loop exhausts.

# break statement can be used to stop a for loop. In such case, the else part is ignored.

# Hence, a for loop's else part runs if no break occurs.

# Here is an example to illustrate this.

digits =[0,1,2,3]
for digit in digits:
    print(digit)
else:
    print("no item left")



# What is while loop in Python?

# The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.

# We generally use this loop when we don't know beforehand, the number of times to iterate.
# Syntax of while Loop in Python

# while test_expression:
#     Body of while

# In while loop, test expression is checked first. The body of the loop is entered only if the test_expression evaluates to True. After one iteration, the test expression is checked again. This process continues until the test_expression evaluates to False.

# In Python, the body of the while loop is determined through indentation.

# Body starts with indentation and the first un indented line marks the end.

# Python interprets any non-zero value as True. None and 0 are interpreted as False.

#example of while loop
# the numbers list we have declared earlier is
# numbers=-{6,5,3,9,7,2,1}

print("the sum of the list {0} using while loop".format(numbers))
sum=0
i=0
while i < len(numbers):
    sum+=numbers[i]
    i+=1

print("the sum of the numbers-list {0} is {1}".format(numbers,sum))

print("the sum of natural no. using while loop in python")
number_limit=int(input("enter the number till you want its sum"))
i=1
sum=0
while i <= number_limit:
    sum += i
    i+=1

print("the sum of natural number till {0} is = {1}".format(number_limit,sum))

# while loop with else

# Same as that of for loop, we can have an optional else block with while loop as well.

# The else part is executed if the condition in the while loop evaluates to False.

# The while loop can be terminated with a break statement. In such case, the else part is ignored. Hence, a while loop's else part runs if no break occurs and the condition is false.

# Here is an example to illustrate this.

# example to illustrate the use of else statement with the while loop

i=0

while i < 3:
    print("inside the while loop")
    i+=1
else:
    print("inside else")

#break statements in python
#break and continue are used to break the normal flow of the loop
# In Python, break and continue statements can alter the flow of a normal loop.

# Loops iterate over a block of code until test expression is false, but sometimes we wish to terminate the current iteration or even the whole loop without checking test expression.

# Python break statement

# The break statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.

# If break statement is inside a nested loop (loop inside another loop), break will terminate the innermost loop.

print("working of the break statement")
words=list("hello boys")
print("the list of words is {}".format(words))
for word in words:
    if(word == "y"):
        print("break encountered")
        break
    else:
        print(word,end=" ")
print("end of for loop")

#python continue statement

# The continue statement is used to skip the rest of the code   inside the loop for the current iteration only. loop does not terminate but continue on with thw next iteration.

print("working of the continue statement")
words=list("kool cucumber")
for word in words:
    if(word == "u"):
        print("continue encountered")
        continue


    print(word,end=" ")

print("end of for loop")

# What is pass statement in Python?
# In Python programming, pass is a null statement. The difference between a comment and pass statement in Python is that, while the interpreter ignores a comment entirely, pass is not ignored.

# However, nothing happens when pass is executed. It results into no operation (NOP).

# We generally use it as a placeholder.

# Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. They cannot have an empty body. The interpreter would complain. So, we use the pass statement to construct a body that does nothing.
words=list("call 911")
for words in words:
    pass
else:
    print("the loop is passed")

# some example of loops in python

# infinite loop using while loop
# num=0
# while True:
#     num=num+1
#     print(num,end=" ")

#loop with condition in the start

print("print word with stars in it for example w*o*r*d")
word=input("enter a word or skip by pressing enter")
i=0
while i<len(word):
    print(word[i],end="*")
    i=i+1
else:
    print("\n word printed") 

print("done of condition at the start")

#loop with condition in the middle
print("program to depict all the vowels")
i=0
vowels=list("aeiouAEIOU")
print(vowels)
while True:
    if (i<5):
        v=input("enter the vowels")
        if v in vowels:
            print("yes {0} is vowel".format(v))
            i=i+1
        else:
            print("you have entered a wrong vowel")
            break
    else:
        print("you have answered all the vowels")
        break

print("game has ended")

#loop with condition at the end
print("lets roll a dice")
import random
while True:
    input("press enter to roll the dice")
    num=random.randint(1,6)
    print("dice shows",num)
    option = input("Roll The Dice Again(y/n):- ")
    if(option=="n" or option =="N"):
        break
print("end of game")
