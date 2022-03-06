# THIS IS EDUREKA PYTHON CHEATSHEET CREATED BY FOLLOWING THEIR VIDEO TUTORIAL#
# CHEATSHEET AUTHOR - MONKS_MOJO
# DATE-12TH DECEMBER 2019
# VIDEO TITLE-Python Tutorial For Beginners | Python Full Course From Scratch | Python Programming | Edureka
# VIDEO LINK-https://www.youtube.com/watch?v=vaysJAMDaZw
# THIS TITORIAL IS TILL-3:34:22 User-Defined Exceptions
# CAUSE I JUST WANT TO LEARN PYTHON BASICS AND USE IT FOR COMPETITIVE PROGRAMMING

#################### START OF TUTORIAL ####################

# Python was created in December 1989 by Guido van Rossum
# Python is a interpreted, object oriented high level programming language.

# Q-difference between interpreted language and compiled time language
# Ans-
# Interpreted language-Reads every line individually and executes it. If found error it will stop the execution until the error is resolved.Interpreter is always present in the memory.
# Compiled language- the whole language is compiled in one go in to object code.if there are syntax error they are displayed at the end of compilation.Compiler is only loaded into the memory when the source code is needed to be converted to object code.

#### Features Of Python #####
# -> python is easy to learn read and write language
# -> python is free and open source software--FOSS(FREE OPEN SOURCE SOFTWARE)which means one can freely distribute the copies of this software and reads it source code and modify it.
# -> High level Language--one does not need to worry about the low level operating system functionalities like memory management while writing python scripts.
# -> Python is portable souppotred by many operating system.
# -> support functional programming and object oriented programming paradigm.
# -> python is extensible i.e it can be called by a c++ function of can be integrated in a c++ program.
#############################################


###### Operatorts In Python #######
# we have following operators.
# 1-Arthemetic Operator
# 2-Assignment Operator
# 3-Logical Operator
# 4-Comaprison Operator
# 5-Bitwise Operator
# 6-Identity Operator
# 7-Membership Operator

############## Arthemetic Operator ###########
num1 = 10
num2 = 25
print(" num-1 is ->{0}\n num2-2 is ->{1}".format(num1, num2))
# 1.a-addition
# add two operand or unary plus
print("addition->", num1+num2)  # 35

# 1.b-subtraction
# subtract two operand or unary subtract.
print("subtraction->", num1-num2)  # 15

# 1.c-multiplication
# multiplication two operand.
print("multiplication", num1*num2)  # 250

# 1.d-Division
# devision of left operand with right operand and return a float.
print("Devision", num1/num2)  # 0.4

# 1.e-Exponential
# left operand raised to the power of  right operand.
print("Exponential", num1**num2)  # 10000000000000000000000000

# 1.f-Modulas
# Remainder of the devision of left operand by the right operand.
print("Modulas", num2 % num1)  # 5

# 1.g-floor division
# the division that result into whole number adjusted to the left in the number line.
print("Floor Division", num2//num1)  # 2
#################################################

################## Assignment Operator ##############
num3 = 10
# 2.a +=
num3 += 10
print("num3=num3+10 shorthand---->num3+=10-->{0}".format(num3))  # 20
# 2.b -=
num3 -= 10
print("num3=num3-10 shorthand---->num3-=10-->{0}".format(num3))  # 10
# 2.c *=
num3 *= 10
print("num3=num3*10 shorthand---->num3*=10-->{0}".format(num3))  # 100
# 2.d /=
num3 /= 10
print("num3=num3/10 shorthand---->num3/=10-->{0}".format(num3))  # 10
# 2.e %=
num3 %= 4
print("num3=num3%4 shorthand---->num3%=4-->{0}".format(num3))  # 2
# 2.f //=
num3 //= 2
print("num3=num3%2 shorthand---->num3//=2-->{0}".format(num3))  # 1
# 2.g **=
num3 **= 4
print("num3=num3**4 shorthand---->num3**=4-->{0}".format(num3))  # 1
######################################################################

################### Comparison Operator #########################
# 3.a >(greater than) return True if left operand is greater than right operand otherwise False
print(
    "num1-->{0} & num2--->{1} then  Is num1>num2-->{2}".format(num1, num2, num1 > num2))

# 3.b <(less than) return True if left operand is smaller than right operand otherwise False
print(
    "num1-->{0} & num2--->{1} then  Is num1<num2-->{2}".format(num1, num2, num1 < num2))

# 3.c ==(equal too) return True if left operand is equal to the right operand otherwise False
print("num1-->{0} & num2--->{1} then  Is num1==num2-->{2}".format(num1, num2, num1 == num2))

# 3.d !=(not equal too) return True if left operand is not equal to the right operand otherwise False
print(
    "num1-->{0} & num2--->{1} then  Is num1>num2-->{2}".format(num1, num2, num1 > num2))
############################################################################

####################### Logical Operator ##############################
x = True
y = False
print("x value-->", x)
print("y value-->", y)
# 1.and return True if both statement are true otherwise False
# 2.or return True if any of the statement is True Otherwise False
# 3.not return complement of the value
print("x and y-->", x and y)  # False
print("x or y-->", x or y)  # True
print("not y-->", not y)  # True
# -logical operator are mainly used in conditional statement
#######################################################################

#################### BITWISE OPERATOR ########################
# &(and)-->perform or operator on each bit of  number
# 7-->111(in binary),5--->101(in binary)
# performing bitwise & on -- (111-->7 & 101-->5) will result in 101-->5
print("7-->111(in binary),5--->101(in binary) performing bitwise & on it will give-->", 7 & 5)  # 5(101)

# |(or)-->perform and operator on each bit of number
# 7-->111(in binary),5--->101(in binary)
# performing bitwise | on -- (111-->7 | 101-->5) will result in 111->7
print("7-->111(in binary),5--->101(in binary) performing bitwise | on it will give-->", 7 | 5)  # 7(111)


# ^(xor)-->perform xor operator on each bit of number
# 7-->111(in binary),5--->101(in binary)
# performing bitwise ^ on -- (111-->7 ^ 101-->5) will result in 010->2
print("7-->111(in binary),5--->101(in binary) performing bitwise ^ on it will give-->", 7 ^ 5)  # 2(010)
##############################################################

###############Identity Operator################
# --> is (return True if the operands are identical.i.e refers to the same object)
# --> is not(return True if the operands are not identical.i.e does not refer to same object)
# everything in python is an object
# to know the type of object we use type() function
x = 5  # (will be identical to number 5)

print("type of x is->", type(x))
print("Is x is 5", x is 5)  # True
print("Is x is not 5", x is not 5)  # False
################################################

##################### Membership Operator ###########################
# helps in searching of an element in the list or string
# in -->Returns true if the perticular element is found in the list
# not in --> Returns true if the perticular element is not found in the list
list1 = [1, 2, 3, 4, 5, 6]
print("the list is-->", list)
print("is 3 present in the list-->", 3 in list1)
print("is 3 not present in the list-->", 3 not in list1)
#######################################################################


###################### DATATYPES IN PYTHON ##############################
# >> python is a loosly typed language
# >> therefore no need to define datatype of the variable
# >> no need to declare variable before using them

# datatypes are of two types 1> mutable 2> immutable

# 1> mutable datatypes contain
# a> set
# b> dictionaries
# c> list

# 2> immutable datatypes contain
# a> number
# b> string
# c> tuple


#############################################################
# 1> mutable datatypes contain
# a> number
# in numbers we have >>..
# 1. integer(integer numbers)
print("addition of two integer 4 + 8 = ", 4+8)
# in python integer length is based on system memory

# 2. floats(numbers with decimal places)
print("addition of two float numbers 5.6 + 3.2 =", 5.6+3.2)

# 3. complex numbers
x = 3.14j
print("complex literal value", x)
print("real_part =", x.real)
print("imaginary part=", x.imag)
##################################################################

######################################################################
# b> string
# string are the sequence of the characters
string1 = "hello this is a string"
# multiline string can be denoted with the help of triple quote
string2 = """ this is now a multiline string
string continue in new line
"""

# Operatons that can be performed on the string are
# 1.> concatenation- means combining of two strings with the help of + operator
print("concatenation of two strings")
print(string1+string2)

# 2.> repetition- means repetition of the string with the help of * operator
print("repeating of this string 5 times"*5)

# 3.> slicing- means extracting a substring from a string.
print(string1)
print("extracting a substring from above string")
print(string1[3:7])  # lo t
print(string1[:6])  # 0 to 5 hello
print(string1[3:-3])  # from index 3 to index -4 from behind lo this is a str

# 4.> indexing- accessing the perticular character from a string
print(string1[0])  # first character >h
print(string1[4])  # fifth character >0
print(string1[-3])  # third character from behind >i
###

# some common string method
# 1. len() method-- returns length of the string.
word = "edureka"
print(word)  # edureka
print("length of the word-->", len(word))  # 7

# 2. find() method-- returns starting index of the substring you want to find in the string.
print("starting index of 're' in edureka is-->", word.find("re"))  # 3

# 3. replace() method-- replace a substring with another substring in the string.function takes two arguments find("substring you want to replace","new substring")
print("Replacing 'ed' with 'e' in edureka using replace() method-->",
      word.replace("ed", "e"))  # eureka
# 4. split() method-- split the string into a list of individual characters
print("spliting the "+word+" into ", word.split('*'))

# 5. count() method-- count the occurrence of specified character in the string
# count is the case sensitive
print("counting the occurrence of e in "+word+" is ", word.count('e'))  # 2

# 6.upper() method-- convert string to upper case
# EDUREKA
print("converting {0} to uppercase will give-{1}".format(word, word.upper()))

# 7.lower() method-- convert string to lower case
# edureka
print("converting {0} to lowercase will give-{1}".format(word, word.lower()))

# 8. isalpha() method-return true if the string contains alphabets
print(" '{0}' the string '{1}' is made of alphabets".format(
    word.isalpha(), word))  # True

# 9. max() method-return character with highest ascii value in the string
print(" '{0}' in the string '{1}' have highest ascii value".format(
    max(word), word))  # u

# 10. min() method-return character with lowest ascii value in the string
print(" '{0}' in the string '{1}' have lowest ascii value".format(
    min(word), word))  # a
#############################################################################


#############################################################################
# c> tuples
# a tuple is the sequence of immutable python objects like floating number, string literal etc.
# tuple can't be changed unlike list
# tuples are defined using curved braces
my_tup = ("Edureka", "python", 100, 90.87)
friends_tup = ("john", "jimmy", "jim", "juno",)
print("diplaying of tuples")
print(my_tup)  # ("Edureka", "python", 100, 90.87)
print(friends_tup)  # ("john", "jimmy", "jim", "juno",)

# diffrent operations that can be performed on the tuples are
# 1.> concatenation-combining of two tuples with '+' operator
print("combining of above two tuples")
print(my_tup+friends_tup)
print(friends_tup+("ray", "jonson"))

# 2.> Repetition- repetition of the element tuples
print(my_tup*2)

# 3.> slicing- means extracting a sub tuple  from a tuple.
print(friends_tup[2:])
# if out of range you will not get error

# 4.> indexing- means accessing a perticular tuple element from tuple
print(friends_tup[0])
##############################################################################
################################################################################

##############################################################################
# Mutable DATA TYPES

##########################################################################
# 1->List
#   a list is the sequence of mutable python objects.
#   the list can be modified
#   a list can be shown with the help of [] braces

my_list = ["hello", "P", 123, 12.78]
color_list = ["blue", "yellow", "pink", "red", "green"]

print(my_list)
print(color_list)

# diffrent operations that can be performed on the list are
# 1.> concatenation-combining of two list with '+' operator
print("combining of above list")
print(my_list+color_list)
print(color_list+["black", "grey"])

# 2.> Repetition- repetition of the list element
print(my_list*2)

# 3.> slicing- means extracting a sub list  from a list.
print(color_list[2:])
# if out of range you will not get error

# 4.> indexing- means accessing a perticular  element from list
print(color_list[0])

# type specific methods of the list
# 1. append(value) method-adds value to the ned of the list
print(color_list.append("brown"))

# 2. pop() method-removes value from the list
print(color_list.pop())
# you can also remove the specific element by specifying the index number
print(color_list.pop(0))

# 3. exteds([value1,value2])-add item to the already presented list
print(my_list.extend(["hope", 100]))

# 4. insert(index,value)-insert element in the list at a perticular index.
print(my_list.insert(4, "holy"))
#######################################################################

####################### Dictionaries in python #######################

# dictionaries are the most flexible built in data type of python
# dictionaries items are stored and fetch by key instead of by positional index
# dictionaries are the key value pair
my_dict = {1: "hey", 2: "hi", 3: "hello"}
print(my_dict)
# diffrent ways to create a dictionary

# 1.- empty dictionary
empty_dict = {}

# 2.- dictionary with integer keys
integer_key_dict = {1: "yellow", 2: 10.7, 3: 4567}

# 3.- dictionary with mixed keys
mixed_key_dict = {1: "yellow", "hello": 101, 'C': "curly"}

# dictionary methods

# accessing the dictionary method
print(my_dict)
print(my_dict[2])  # where 2 is the key

# length of the dictionary
print("length of the my_dict is-->", len(my_dict))

# key() printing all the keys of the dictionaries
print("printing all the key of my_dict--> ", my_dict.keys())

# values() printing all the values of the dictionaries
print("printing all the values of my_dict--> ", my_dict.values())

# items() printing all the key value pairs of the dictionaries
print("all the key value pair of the my_dict--> ", my_dict.items())

# get(key) returns the value for the specified key
print("value present at key 1 in my dict is -->", my_dict.get(1))

# update({key:value}) add a key value pair to the already existing key
print("adding a key value to my_dict")
my_dict.update({4: "namaste"})
print(my_dict)

# pop(key) removes the specified key value from the dictionary.
my_dict.pop(4)
print("poping out last element from the my_dict")
print(my_dict.items())

#######################################################################

#################### SETS IN PYTHON ###############################
# a set is an unordered collection of the items
# a set cannot have duplicate values. which means every element should be unique
my_set = {"god", "almighty", "the one"}
whole_set = {1, 2, 4, 5, 6, 9}
integer_set = {-1, -9, 0, 1, 2, 3}
print(my_set)

# sets methods

# 1.union-does union(concatenate two sets) on two sets
print("union on {0} and {1} is-> {2}".format(integer_set,
                                             whole_set, (integer_set | whole_set)))

# 2.intersection-display only the common element from two sets
print("intersection on {0} and {1} is-> {2}".format(integer_set,
                                                    whole_set, (integer_set & whole_set)))

# 3.difference-display the distinct element from the left set
print("distinct or diffrent element in {0} from {1} is-> {2}".format(
    integer_set, whole_set, (integer_set - whole_set)))
###################################################################

######################### END OF DATATYPES ########################

########################Flowcontrol#################################
# 1.--> if elif else condition statement
marks = int(input("eneter the marks"))  # by default the input if string
if(marks > 80):
    print("grade A")
elif(marks < 80 and marks >= 60):
    print("grade B")
elif(marks < 60 and marks >= 40):
    print("grade C")
else:
    print("grade F")

# looping
# while - when we have a condition and don't know the number of iteration we want to run the loop
# entry controlled loops

print("find the sum on n natural number")
num = int(input("enter the number till you want sum"))
if(num <= 0):
    print("eneter a positive number")
else:
    sum = 0
    while(num >= 0):
        sum += num
        num -= 1
print("the sum of number is {0}".format(sum))

# for- when we know the number of iteration we need to run the loop are known

# range starts from 10 end at 0 and keep decrementing by 1
for quantity in range(10, 0, -1):
    print("{0} bottle of beer left".format(quantity))


#### break and continue statement function ###
# Break is used to come out of the loop when certain conditions are met
print("to come out of the loop when counter hits ten")
counter = 0
while True:
    if counter > 10:
        break
    else:
        print("the current counter is on-->", counter)

print("the loop has been ended")

# Continue-> it ensures when certain conditions are met the following statements are skipped inside the loop and the loop will move on to the next iteration.
print("odd number between 1 and 20")
print("printing of odd number with the help of continue statement")
for index in range(20):
    if(index % 2 == 0):
        continue
    else:
        print("{0} is odd".format(0))
print("the loop has ended")
##############################################

######### FUNCTIONS IN PYTHON ################
# Functions are of two types

# 1.inbuilt functions- example len(),type(),name.upper()

# 2.user defined function - it is the a block of organized reusable set of instructions and statements that is used to perform some relatable actions.

# advantages of the functions
# re-usability of the code
# procedural decomposition make code more organized

print("a function for addition of two numbers")


def addition(num1, num2):
    return num1+num2


num1 = float(input("enter 1st number"))
num2 = float(input("enter second number"))
result = addition(num1, num2)
print("{0} + {1} is = {2} ".format(num1, num2, result))

# python uses and supports call by value methodology where is always an object reference

original_list = ["telly", "mark", "alex"]
print("original list is-->", original_list)
# making a function which updates the original list


def list_updater(argument_list):
    argument_list = ["naruto", "sasuke", "obito"]
    print("the list is updated")
    return argument_list


print("passing original_list to the list_updater() function")
print("updated list-->")
print(list_updater(original_list))  # ["naruto","sasuke","obito"]

print("but did the original list actually changed or the function take the copy of the original list and worked on it")

print("original_list after passing it to the function")
print(original_list)
##############################################
############ FIBONACCI SERIES ################


def print_fib(fib_range):
    a = 0
    b = 1
    print(a)
    print(b)
    while (fib_range):
        c = a+b
        print("{0}+{1}->{2}".format(a, b, c))
        a = b
        b = c
        fib_range -= 1


print_fib(20)
##############################################


############### File Handling In Python ##################

############## Reading From File ########################

file_pointer = open("file_handling.txt", "r")
# open function allows to open a connection between file and script
# all the data from the file will be store inside file_pointer defined above
# it takes  two arguments file path and write mode
# diffrent modes we have in python file handling are
# 1.> r (read)
# 2.> w (write)
# 3.> a (append)
# 4.> r+ (read & write)

# to make sure the file is in redable format with file_name.redable() function that returns True if the file is in readable format. else False

if(file_pointer.readable()):
    print("we can read from the file")
    print(file_pointer.read())
else:
    print("unable to read file")

# when you want to read a file line by line or want to read a specific line.we use a readline() function
# we have another function readlines() which convert each line into the list.
if(file_pointer.readable()):
    print("we can read from the file")
    print("reading first line")
    file_pointer.seek(0)  # put the pointer to the first line
    print(file_pointer.readline()[0:-1])  # traversing of only the first line
else:
    print("unable to read file")

if(file_pointer.readable()):
    print("we can read from the file")
    line_list = file_pointer.readlines()  # saving the list
    print("each line in the file is now element of the list")
    print("reading first line")
    print(line_list[0])

    print("reading last line")
    print(line_list[-1])
else:
    print("unable to read file")
file_pointer.close()  # it is really important that you close a file
# a lock mechanism is given to the file so if you don't close the file it wont be able to be open by another applications

####################### writing to a file ##############
# to write to the previously existed file we use appned mode (a).
# to write to a newly created file we use write mode which create a file
# append mode
file_pointer = open("file_handling.txt", "a")
print("appending to the file")
print("enter your new friend name")
friend_name = "\ntony stark\nbruce wayne\n"
file_pointer.write(friend_name)
file_pointer.close()
print("checking if the data is written to the file")

# after appending checking wether the data is written to the file of not
file_pointer = open("file_handling.txt", "r")
file_pointer.seek(0)  # putting the file pointer to start
if(file_pointer.readable()):
    print("we can read from the file")
    print(file_pointer.read())
else:
    print("unable to read file")

file_pointer.close()

# write mode
print("opening a file to the write mode")
file_pointer = open("file_handling.txt", "w")
print("writing to the file")
print("overwriting the file")
file_pointer.write("\nJim Morrison\nJohn Lennon \n Pepper Stone\nKurt Cobain")
print("data written to the file")

# after appending checking wether the data is written to the file of not
file_pointer = open("file_handling.txt", "r")
file_pointer.seek(0)  # putting the file pointer to start
if(file_pointer.readable()):
    print("we can read from the file")
    print(file_pointer.read())
else:
    print("unable to read file")

file_pointer.close()
################################################################################
