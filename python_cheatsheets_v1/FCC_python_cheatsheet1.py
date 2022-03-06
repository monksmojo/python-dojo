# THIS IS FREE CODE CAMP Learn Python - Full Course for Beginners [Tutorial] PYTHON CHEATSHEET CREATED BY FOLLOWING THEIR VIDEO TUTORIAL ON YouTube.
# CHEATSHEET AUTHOR - MONKS_MOJO
# DATE-12TH august 2019
# VIDEO TITLE-Learn Python - Full Course for Beginners [Tutorial]
# VIDEO LINK-https://youtu.be/rfscVS0vtbw
#  BIG THANKS TO FREE CODE CAMP AND MIKE DANE FROM GIRAFFE ACADEMY FOR BECOMING MY TEACHER FOR THIS COURSE


import useful_tools  # custom python file we created
from math import ceil, floor, sqrt

print("hello world")
# first python programme to print hello world
# printing some slashes and symbol
# using semicolon at the end of every statement is optional
print("   /|")
print("  / |")
print(" /__|")

########################### variables in python ####################

print("once there was a man name george")
print("he was 70 years old")
print("he liked his name very much")
print("but he didn't like age 70")


# instead of hard coding age and name  we can use a variable to store character name and age;

# Variables-> a container to store some data values to manage data. some of them are defined below.

character_name = "clark"
character_age = "35"
print("once there was a man name" + character_name)
print("he was" + character_age + "years old")
print("he liked his name very much")
print("but he didn't like age " + character_age)

# so we use  variables character_name and character_age to store the value which can be changed later on.

###################different type of variables###################

# string= stream of character forming plain text;
string_name = "clark kent"

# number= can contain decimal/float/double values
number_age = 10
amount_in_decimal = 46.23

# boolean= can contain true or false
is_male = True
is_female = False  # first character of true and false is uppercase

######################### working with the strings ###################
# phrase is sequence of characters
phrase = "hi i am a phrase"  # example of a string

# string with newline character in it
print("Hello everyone\nMy name is monks_mojo")

# concatenation of two strings
phrase2 = "What monks_mojo"
print(phrase2+" is noob !!!")

############ type specific function in strings ###############

# conversion of string into uppercase string.upper()
print("conversion of string into uppercase-->", phrase.upper())

# conversion of string into lowercase lower(string)
print("conversion of string into lowercase-->", phrase.lower())

# to check wether the string is in uppercase or lowercase by using if isupper() #and islower() function which returns a boolean value True Or False
print("is phrase is in uppercase -->", phrase.isupper())  # False
print("is phrase is in lowercase -->", phrase.islower())  # True

# we can also call type specific function after a type specific function
print("is " + phrase + " is in uppercase - ->",
      phrase.upper().isupper())  # True


phrase2 = "What monks_mojo knows python"

# length of the string with the help of len(string) function
print("string is-->", phrase2)
print("length of the " + phrase2 +
      " string is with the help of len(string) function is -->", len(phrase2))

# accessing a perticular character in the string with the help of index numbers which start from zero
print("first character in " + phrase2 + " is-->", phrase2[0])
print("last character in " + phrase2 + " is-->", phrase2[-1])

# you can also retrieve a index number of a character or a word from a string using string.index("character function") function
print("index of m in " + phrase2 + " is-->", phrase.index("m"))
# returns the index of the occurrence of the first m
print("index from where monks word start in-> " +
      phrase2 + " is-->", phrase2.index("monks"))

# replace a perticular sub string inside a string by using string.replace("old-substring","new-substring")
print(phrase2+" has been changed to-->\n  ",
      phrase2.replace("python", "front-end"))

############################## working with numbers#########################
# decimal number can go up to 15 position after decimal point
print("decimal number can go up to 15 position after decimal point", 2.3256)

# there is no limit of number or decimal it all depends on the memory of computer

# printing of the negative number
print("printing of the negative number", -78.32)

# calculation of the equation
print("result of the equation 10*3+4 is-->", 10*3+4)  # 34

print("result of the equation 10*(3+4) is-->", 10*(3+4))  # 70

# precedence of the numbers and operators matters

my_num = 5
print("type of {0} is {1}".format(my_num, type(my_num)))

# performing type conversion on variables
my_num = str(5)
print("type of {0} is {1}".format(my_num, type(my_num)))

print("you can concatenate a number and string by type conversion of number into string")

print("the number is"+my_num)

################ some type defined number functions of number are ###########
my_num = int(my_num)
# absolute function
print("absolute of ", my_num, " is->", abs(my_num))

# power function
# pow(x,y) function will returns the power of pow x^y
print("2^3 is->", pow(2, 3))

# max
# max(x,y) will return the maximum number from the argument passed i.e x,y
print("maximum number between 10 and 45 is->", max(10, 45))

# min
# min(x,y) will return the minimum number from the argument passed i.e x,y
print("minimum number between 10 and 45 is->", min(10, 45))

# sometimes to perform some of the math function inside the python file you have to include the math libraray

# round() function round of decimal number
print("rounding of 3.6 is->", round(3.6))  # 3

# ceil() function round of decimal number to upper value
print("ceil of 3.6 is->", ceil(3.6))  # 4

# floor() function round of decimal number to lower value
print("floor of 3.6 is->", floor(3.6))  # 3

# sqrt() function finds squareroot of the number
print("squareroot of 36 is->", sqrt(36))  # 6

################## geting input from the user #################################

name = input("enter your name: ")
print("welcome "+name+" to python cheatsheet")

# by default the input taken from the user are in string format so we have to perform type conversion
age = input("enter your age : ->")
print("so yourage is ->", age)

# what happens if we forgot to type convert data explicitly while taking input from the user
num1 = input("enter the first number: ")  # let say 3
num2 = input("enter the second number: ")  # let say 4
print("addition of "+num1+" and "+num2+" is ", num1+num2)  # 34 wrong output

# since the user input is treated as string so the above code will produce wrong output
print("wrong output")

print("correct output programme")
print("basic calculator")

num1 = float(input("eneter the first number: "))  # let say 3
num2 = float(input("eneter the second number: "))  # let say 7
print("addition of ", num1, " and ", num2,
      " is ", num1+num2)  # 10 right output

print("subtraction of ", num1, " and ", num2,
      " is ", num1-num2)  # -4 right output

##################### creation of passage based on user input ######
print("creation of passage based on user input")
name = input("enter your name: ")
age = int(input("enter your age: "))
weight = float(input("enter your weight: "))

print("hello welcome {0} to the python cheatsheet your age is {1} and your weight is {2}".format(
    name, age, weight))

# ############################### list in python ######################
# list are ordered and mutable form of collection of data which can be manipulated
friend = ["chief", "monks", "bossman"]

# since lists are ordered collection of data we can access them using index number
print(friend)
print("first element in->", friend, "is-> ", friend[0])  # chief
print("last element in->", friend, "is-> ", friend[-1])  # bossman
print("second last element in->", friend, "is-> ", friend[-2])  # monks
# to access list from reverse we use negative number notation

# a list can contain diffrent data types

data_list = ["derek", 17.3, 100, True]
print("display of list with diffrent data type->", data_list)

# slicing
print("display list from second element to second last element in->", data_list)
print(data_list[1:-2])

################ type defined function in the list ################

# append("value")
# add item to the end of the list with append() function
print("adding tom hanks to ", friend)
friend.append("tom hanks")
print(friend)

# another way to add item to list are using slicing method
friend[2:2] = ["tony"]
print("another way to add item to list are using slicing method")
print(friend)

# insert(index,value)
# when we want to add a item in a list at a specific position we use insert(index,value) function. taking two arguments 1. index where we want to insert 2. the value which we want to insert in the list
print("adding the weekend to 2nd position of", friend)
friend.insert(1, "the weekend")
print(friend)

# remove("value")
# when we want to remove an item from the list by giving item name as the argument
print("removing the weekend from the list")
friend.remove("the weekend")
print(friend)

# pop(index number)
# by default the pop() function will remove and return the last element from the list
# but we can also specify which element to remove from the list by giving index number as argument
friend.pop(2)
print(" removing tony from the list of friends ")
print(friend)

# clear()
# when we want to delete all items from the list we use clear
data_list.clear()
print("empty list ", data_list)

print("populating the list again")
data_list.append(3.14)
data_list.append(3.14)
data_list.append(3.14)
print(data_list)

# count("value")
# returns the no. of times argument value passed in the function is present in the list
print("no. of 3.14 item in list->", data_list)
print(data_list.count(3.14))  # 3

# index(index number)
# gives the index position of the item if its present in the list.
print("index of 'chief' in {0} is {1}".format(friend, friend.index("chief")))

# sort()
# sort the list in the accending order
print(
    "sorting the list {0} in accending order-> {1}".format(friend, friend.sort()))

# copy()
# copies the list to another list
print("creating copy of the list", friend)
friend_copy = friend.copy()

# reverse of the string
print("reversing the items of the list", friend_copy.reverse())

#################### tuples ################################

# it is a datastructures similar to the list where we store diffrent items.

# tuples are defined inside parentheses ()

# main difference between list and tuple is that tuple are immutable.
# i.e you cannot add items to the tuples neither you can edit the element of the tuples.

# similarities between list and tuple is both of them are ordered

coordinates = (4, 5)
# coordinates[0]=7 this will give syntax error
print("2d coordinates")
# since tuples are ordered collection of data you can access the element using index number
print(
    "x cordinate in the following 2d coordinates->{0} are ->{1}".format(coordinates, coordinates[0]))

coordinates1 = (10, 11)
coordinates2 = (16, 15)
# we can add two tuples to create one tuples
xyz_coordinates = coordinates1+coordinates2

print("The dimensional coordinates ", xyz_coordinates)

# we can create a list which contain tuples
coordinates_list = [(4, 5), (7, 10), (11, 13)]
print("a list of coordinates are", coordinates_list)

####################### Functions ########################
# function are bunch of statements used to execute a specific task.
# helps you to organizer code
# function defined once can be called again and again

# defining of the function


def sayhello(name):
    print("hello "+name+" from sayhello function")


# function call
sayhello("freddy")
# make sure you have defined function before calling it
sayhello("david")

# function can also return data
# or sometimes we want functions to return data hence we use return keyword in functions


def number_cube(num):
    return num*num*num
# any statements after return will not execute.
# after returning the value the function terminates until and unless called again


# we can directly print return value or can store it inside the variable
cube_result = number_cube(15)
print("the cube of 15 is ->", cube_result)

cube_result = number_cube(127)
print("the cube of 127 is ->", cube_result)

################# IF CONDITIONAL STATEMENTS ########################

# if statements are used when we want execute statements only when certain conditions are met
# we use comparison and logical operator in the conditional statement
# if elif and else mostly return boolean value(True,False)


is_male = True
is_tall = False

if(is_male):
    print("you are male")
else:
    print("you are not male")

# use of logical operator and or not
if(is_male or is_tall):
    if(is_male):
        print("you are male")

    if(is_tall):
        print("you are tall")
elif(is_male and is_tall):
    print("you are both male and tall")
else:
    print("you are neither male nor tall")

# comparison operator in conditional statements


def max_of_3(num1, num2, num3):
    if((num1 >= num2) and (num1 >= num3)):
        print(num1, "is greatest")
    elif(num2 >= num3):
        print(num2, "is greatest")
    else:
        print(num3, " is greatest")


print(" find greatest of 3 numbers")
num1 = int(input("eneter 1st number"))
num2 = int(input("eneter 2nd number"))
num3 = int(input("eneter 3rd number"))

max_of_3(num1, num2, num3)

# upgrading basic calculator
print("welcome to basic calculator to perform")
print("1.+ ,2.- ,3.* ,4./,5.%   ")
num1 = int(input("eneter 1st number"))
num2 = int(input("eneter 2nd number"))
op = input("enter the operator you want to use on operands")
if(op == "+"):
    print("addition of {0}+{1} is->{2}".format(num1, num2, num1+num2))
elif(op == "-"):
    print("subtraction of {0}-{1} is->{2}".format(num1, num2, num1-num2))
if(op == "*"):
    print("multiplication of {0}*{1} is->{2}".format(num1, num2, num1*num2))
if(op == "/"):
    print("division of {0}/{1} is->{2}".format(num1, num2, num1/num2))
if(op == "%"):
    print("modulus of {0}%{1} is->{2}".format(num1, num2, num1 % num2))
else:
    print("sorry operator not suppourted")

########################### dictionaries ##########################
# dictionaries are special type of data structure that helps you store info in the form of key value pair.
# dictionaries are created using curly braces.
# we can access a data inside the dictionary with the help of keys and it is unique
month = {"jan": "january", "feb": "february", "mar": "march", "apr": "april", "may": "may", "jun": "june",
         "jul": "july", "aug": "august", "sep": "september", "oct": "october", "nov": "november", "dec": "december", }
# getting value with key
print("nov key value->", month["nov"])

# another method to retrieve value from key is to use get() function
# advantage of using get() function is that it displays a default msg if the key is not present in the dictionary.
print(month.get("nov"))

print(month.get("fyi", "month not available "))

######################### while loop #########################

# while loop are called enter controlled loop.
# i.e in while loop the conditions are checked in the beginning

# while loop execute code as long as the condition in the beginning is true

###################### guessing game ############################
############# version 1 ################

your_word = ""
secret_word = "soda pop"
print("game to guess the secret word")
while your_word != secret_word:
    your_word = input("eneter the secret word->")
print("yes you guessed the word right its-->", secret_word)

##############################################################

######################### version 2 ##########################
secret_word = "soda pop"
your_word = ""
guess_count = 0
guess_limit = 3
limit_reached = False

while (your_word != secret_word) and not(limit_reached):
    if(guess_count < guess_limit):
        your_word = input("enter the secret word")
        guess_count += 1
    else:
        limit_reached = True
if(limit_reached):
    print("you reached the max guess count")
    print("you loose")
else:
    print("you guessed the word right its->", secret_word)
###########################################################

############### version 3 my_version using break ##########
guess_limit = 3
secret_word = "soda pop"
print("you have "+str(guess_limit)+" chances to guess the secret word")
while guess_limit > 0:
    print("chances_left->"+str(guess_limit))
    your_word = input("what you think secret word will be->")
    if(your_word == secret_word):
        break
    else:
        guess_limit -= 1
if(guess_limit <= 0):
    print("you are out of guess limit")
    print("you loose")
else:
    print("yeah you guessed the word right->", secret_word)
#################################################################

######################### FOR LOOP ##############################
# for loop are mainly used when you want to iterate through a collection of item
# all those collection which has starting and ending point

# travesring through a string
for letter in "youtube rewind":
    print(letter, end="-")
print("\n end of for loop")

# iterating through the list
friends = ["jim", "jimmy", "john"]
print("my friends are->")
for friend_name in friends:
    print(friend_name, end=", ")
print("\nend of friend list")

# printing of even number less than 21
for index in range(11):
    if(index % 2 == 0):
        print("the number->{0} is even".format(index))
    else:
        print("the number->{0} is odd".format(index))

### inbuilt exponential function ###
print("2^3 is->", (2**3))

### creating your exponential function ####


def exponential(base_num, power_num):
    result = 1
    if(power_num == 0):
        return 1
    else:
        for pow in range(power_num):
            result *= base_num
            pow = pow  # this statement has no effect on the code neglect it
        return result


print("the power of 2^3 is-->", exponential(2, 3))

############### 2D LIST AND NESTED LOOPS #########

number_grid = [[1, 2, 3], [7, 8, 9], [11, 22, 33], [77, 88, 99]]

# accessing the elements of the 2D list

print("the 2d list->", number_grid)

print("get 3 from list->", number_grid[0][2])
# print-3

print("get 22 from list->", number_grid[2][1])
# print-22

print("get 99 from list->", number_grid[3][2])
# print-99

# traversing all element with the help of nested for loop
for row in number_grid:
    for column in row:
        print(column, end=" ")
    print("\n")

#################### translation of the phrase ##############


def translate(original_phrase):
    translated_phrase = ""
    original_phrase.lower()
    for letter in original_phrase:
        if(letter in "AEIOUaeiou"):
            translated_phrase = translated_phrase+"$"
        else:
            translated_phrase = translated_phrase+letter

        return translated_phrase


translate("cool boy daniel")
#############################################################

################## Exception Handling in Python #############

# one of the main reason to do exception handling is because python is the loosly typed language.
# to make it strongly types we use tryand expect

# there are two type of expect in the python we have

# broad except:-> which will catch all the run time error inspect of type of the error
# broad except error example:->
try:
    print("exception handling of broad exception ")
    value = int(input("give a number input-: "))
    print("input provided->"+str(value))
except:
    print("Error!!! you didn't enter the number")


# specific except error- will catch only the specific error
# specific except error example
try:
    print("exception handling of specific exception ")
    value = float(input("enter a decimal number"))
    print("input provided->"+str(value))

except ValueError:
    print("Error!! the input is not a decimal float")
    print("Value Error")
try:
    print("exception handling of when a number is divided by zero")
    value = int(input("eneter a non zero integer"))
    divide_result = 100/value
    print("input provided->"+str(value))
    print("divided result is->"+str(divide_result))
except ZeroDivisionError:
    print("Error!!! you divided the number by zero which is not expected")
    print("ZeroDivisionError")

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
file_pointer.close()  # it is really important that you

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

################ Importing Modules and pip ###########################
# so in python you can import one python file inside another python file and can use variables and functions defined inside that file.

# here we are importing usefool_tools.py file which has some functions and some variables which we will be using in our FCC_python_chaeatsheet1.py

print(" genrating of random number by using the function get_random_number()")
print("which is declared in useful_tools.py file")
print("random number between 1 and 20")
print(int(useful_tools.get_random_number(21)))

print("getting the extention of the file using get_file_extension() ")
print("which is declared in useful_tools.py file")

print("extension of 'file1.txt is->'")
print(useful_tools.get_file_extension("file1.txt"))

print("extension of 'file2.cpp is->'")
print(useful_tools.get_file_extension("file2.cpp"))

print("accessing the variable declared inside another py file")

# useful_tools.meter_in_kilometer
print("i kilometers is->>")
print(str(useful_tools.meter_in_kilometer)+" meters")

# pip is used to install packages and modules in python libraray
# command to install packages
# pip install package_name
######################################################################

##################### Classes and Objects ############################
# Classes are user defined data types..
# Classes are used to represent real word objects..

# Classes represents as a blueprint of the object with the collection of-:
# 1. characterstic of the object(variables)
# 2. methods of the object(functions)


class Student:
    # declaring of constructor which will initialize the objects of the class.
    # constructor are called by themself as soon as the object is created.
    # syntax
    def __init__(self, name, major, cgp, has_loan):  # constructor
        self.name = name
        self.major = major
        self.cgp = cgp
        self.has_loan = has_loan
        # self refers to the object call the constructor at that time

################# Methods Of the Class ####################################

    # class method can be used to define the functionality of the object
    # functions declared inside the class can be accessed by the object of the class

    def print_report(self):
        print("student name is->", self.name)
        print("he has done major in->", self.major)
        print("his cgp is ->", self.cgp)
        print("does he has loan \n->", self.has_loan)

    def on_honor_roll(self):
        if(self.cgp > 40):
            print("yes {0} is on payroll".format(self.name))
        else:
            print("no {0} is not on payroll".format(self.name))


# object act as the instance of the class
# object represent a real world entity
# calling of the constructor
alex_student = Student("alex", "vocals", 95.6, True)
print("creating the object of class", type(alex_student))
alex_student.print_report()  # call to print_report() function
alex_student.on_honor_roll()  # call to the on_honor_roll() function

matt_student = Student("matt", "precursions", 35.6, False)
print("creating the object of class", type(matt_student))
print(matt_student.name)  # accesssing only perticular variable from the class
print(matt_student.has_loan)

################### Inheritance of the class #############
# in inheritance we can inherit the property of the parent class inside the child class.

# also the object of the child class has access to the properties and methods of the parent class.


class GenericChef:
    #parent class
    def make_chicken(self):
        print("the chef can prepare chicken")

    def make_soup(self):
        print("the chef is making soup")

    def special_dish(self):
        print("the chef is making american baked apple pie")


class SuChef(GenericChef):
    # Suchef is the child class.
    # Which inherit the GenericChef class

    def make_hakka_noodles(self):
        print("the chef is making noodles")

    def special_dish(self):
        print("the chef is making the pan fried pork chop ramen")

my_chef=GenericChef()# object of parent class
my_chef.make_chicken() # call to its class method
my_chef.special_dish() # call to parent class method

chief_chef=SuChef() # object of child class

chief_chef.make_chicken() # call to the parent class method as chief chef is the object of child class which inherit the parent class

chief_chef.special_dish()
# since special dish method is present in both parent class and child class.
# the method will be called according to the depends which class object is calling it
######################################################################

############## MCQ Quiz Program ##############################
# program to implement the multiple choice question test

# making the list of questions with available options
question_prompt=["Q-1.What is the color of the apple?\na.>red/green\nb.>yellow\nc.>purple\nd.>blue\n","Q-2.What is the color of the banana?\na.>red/green\nb.>yellow\nc.>purple\nd.>blue\n","Q-3.What is the color of the guavavas?\na.>green\nb>pink\nc.>purple\nd.>blue\n","Q-4.What is the color of the ladyfinger?\na.>yellow\nb.>green\nc.>purple\nd.>blue\n"]

# making the class to store each question as the object with its correct answer key
class QuestionBooklet:
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer

# creating the list objects of the class Question booklet.
# each object contain question from the question prompt list and answer to the question.
question_key=[QuestionBooklet(question_prompt[0],"a"),QuestionBooklet(question_prompt[1],"b"),QuestionBooklet(question_prompt[2],"a"),QuestionBooklet(question_prompt[3],"b")]

def run_test():
    score=0
    for problem in question_key:
        # traversing question_key(list of object of class QuestionBooklet)
        ans=str(input(problem.question+"\n enter your choice--> "))
        # taking input from the user and matching it with stored answer
        if (ans.lower()==problem.answer):
            print("correct answer")
            score+=1
        else:
            print("Wrong answer")
    return score

print("your score from the test is-->",run_test())
###############################################################
# The Documentation in over Thankyou for reading
# if found any mistakes or want to improve notes feel to open an issue


# REGARDS MONKS_MOJO 
###############################################################