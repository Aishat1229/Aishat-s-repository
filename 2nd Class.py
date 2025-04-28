# THURSDAY, 3RD APRIL
print("Hello, World!")
#Python Comments: Documentation, debugging, readability
print("hello world!") #This line of code says hello
print(1 + 2)  #This line of code output sum 1 and 2

"""
"This is "
"a multiline comments in "
"python programming"
"""
import random
# Python Variables
##Python Variables(Numbers):
# If u should declare variables after calling it, it would bring "Name Error" cos interpreter interpretes line by line 
firstNum = 1
secNum = 2
thirdNum = 5
print(firstNum + thirdNum)

# Concatination is the act of joining two strings with the + sign
# Anything in qoutation marks is called a STRING


## Python Variables(Strings):
Name = "Aishat"
print("My name is " + Name)

# Indentation Error means there is supposed to be a space somewhere but the space isnt there

## Python Variables(Boolean):
check = True

if check:
    # print(Name)
    pass     

# if check:
#     print(Name) This wont print the name


## Casting    U cant add variables of different types together unless u use casting
# print(2 + "3") This will bring typeError

# num1 = 2
# num2 = "3"
# print(num1 + int(num2))
# print(type(num2))

# num3 = 4
# print(float(num3))
# print(type(num1))
# print(type(str(num1)))

Name1 = "Tomi"
Name2 = 'Aishat'

print(Name1, Name2)

## Case Sensitivity of Variables
# name = "John"
# name = "Akim"
# This will print the new or updated one
# print(name)

name = "John"
NAME = "Akim"
print(NAME)

## Naming Python Variables
# Rules for descriptive cariable names:
# 1. Must start with a letter ir underscore 
# 2. Cant start with a number"
# 3. Can only contain alpha-numeric(A-z, 0-9, and _)
# 4. Are case sensitive
# 5.   Cant be any python keywords


## Multi-Word Variable Naming
"""
1. Camel case
2. Snake case
3. Pascal case
"""
# Camel Casing
mySchool = "Babcock"
myFirstName = "Aishat"

# Snake- casing
my_school = "Babcock"
my_first_name = "Aishat"

# Pascal- casing
MySchool = "Babcock"
MyFirstName = "Aishat"

"""
Assignment
1. Write a python statement that will output "Tomi will pay $550 at a discount of $50 when he buys a pack of milk
at a grocery store". Use the   following variables:
             Name =  "Tomi"
             Price = "600"
             Discount = 50
2. Write a simple python statement that processes the output in Question 1 only if the vaariable ,
                  is Available = True
"""


#Number One
Name = "Tomi"
#Price = "600"
Price = int("600")  #Converting the string "600" to an integer
Discount = 50

print(Name + " will pay $" + str(Price - Discount) + " at a discount of $" + str(Discount) + " when he buys a pack of milk at a grocery store.")


#Number Two
Price = int("600")  #Converting the string "600" to an integer
Discount = 50
isAvailable = True

if isAvailable:
  print(Name + " will pay $" + str(Price - Discount) + " at a discount of $" + str(Discount) + " when he buys a pack of milk at a grocery store.")

## Assigning Many Values to Variables Friday(4/4)
fruit1, fruit2, fruit3 = "orange", "mango", "pineapple"  #(Assigning many values to many variables)
print(fruit1)
print(fruit2)
print(fruit3)



#Friday 4th April
## Assigning one value to many variables
# fruit4 = fruit5 = fruit6 = "Cherry"
# print(fruit4)
# print(fruit5)
# print(fruit6)

# Array is called List in Python
## Unpacking a Collection
fruits = ["orange", "apple", "mango", "guava"]
print(fruits)
fruit1, fruit2, fruit3, fruit4 = fruits
print(fruit2)

## Global & Local Variables

def myName():
   print("My name is Aishat")
myName()

def myName():
   global Name #Thiw will make it work in diferent functions even though it is in a function
   Name = "Aishat"
   print("My name is " + Name)
myName()

def myName():
   print("My name is " + Name)
myName()

## Python Numbers
# We have three types of python number which are: 1. Int, 2. Float, 3. Complex

# Int(which can be positive or negative)
num1 = 4
print(type(num1))

#Float
num2 = 2.5
print(type(num2))

#Complex numbers
num3 = 2j
print(type(num3))

num4 = 2 + 5j
print(type(num4))

## Converting Numbers 
num1_compl = complex(num1)
print(num1_compl)
print(type(num1_compl))

#When converting from decimal number to int, it wont round up cos the interpreteer would truncates the decimal places
num1_float = float(num1)
print(num1_float)

num2_int = int(num2)
print(num2_int)
# U cant convert complex numbers to anything in python

### Random Numbers
print(random.randrange(1, 10))

## Python Strings

greeting = "HELLO"
print(type(greeting))

print("It's a girl") #If u must use a quote in your words in strings, just make sure they do not match 
# with the one for the string 

bio = """I am Aishat and ..."""
print(bio)

## Strings are Arrays(In programming, u start counting from 0 )

name = "John"
print(name)
print(name[2]) #This will print the 2nd letter

for letters in name:
   print(letters)#This will print the letters one by one

print(len("hippopotamus"))# This will check the length

text = "We are students of Python Programming at Tedprime"
print("Tedprime" in text)

text = "We are students of Python Programming at Tedprime"
print("food" in text)

text = "We are students of Python Programming at Tedprime"
print("Tedprime" not in text)


if "Tedprime" in text:
   print("They are the best")
else:
   print("They are also good")



"""
Assignment
1. Create a little game where your players will guess a specific random numbers, if it matches your number,output
"You won!" else output "You lose!"
Hint: Use the variables:
randomNumber=random.randrange(1,20)
yourGuess = input("Guess the number:)
if xxxxx: xxxx

2. Refine the code below to work appropiately:
text = "We are students of Python Programming at TedPrime"

hub = input("Enter a name of a hub to search from the text: ")

if hub in text: 
   print("They are the best!")
else:
  print(:They are also good)

  

"""

import random

# Generate a random number between 1 and 20
randomNumber = random.randrange(1, 10)

# Ask the player to guess the number
yourGuess = int(input("Guess the number: "))

# Check if the guess matches the random number
if yourGuess == randomNumber:
    print("You won!")
else:
    print("You lose! The correct number was", randomNumber)


text = "We are students of Python Programming at TedPrime"

hub = input("Enter a name of a hub to search from the text: ")

# Convert both to lowercase for case-insensitive comparison
if hub.lower() in text.lower(): 
    print("They are the best!")
else:
    print("They are also good!")


#TUESDAY 8th April
## Slicing Strings in Python
name = "Aishat"
print(name[2:5])
name = "my name is Aishat"
print(name[11:])
name = "my name is Aishat"
print(name[:11])
name = "my name is Aishat"
print(name[8:11])
name = "my name is Aisha"
print(name[-8:-6])

## Modifying Strings
hub = "tedprime"
print(hub.upper())
hub = "tedprime"
print(hub.lower())
hub2 = " tedprime"
print(hub2.strip())  # To remove extra spaces in strings , you use name = " tedprime" print(name.strip())
print(hub2.replace("t", "T"))
hub3 ="ted prime"
print(hub3.split(" "))

text = "I have mangoes, bananas, guava"
print(text.split(","))
text = "I am a girl. I love sleeping"
print(text.split("."))

text = "I am up."
text2 = "Up I go"
print(text + text2)

## String Format
age = 10
bio = "I am ten years old"

print(f"My age is {age}")
print(f"I am {age} years old")

price_of_milk = 50

print(f"A tin of milk cost {price_of_milk} Naira")

price_of_milk = 50.666666

print(f"A tin of milk cost {price_of_milk:.3f} Naira")

price_of_milk = 50.666666
item = "milk"
print(f"A tin of {item.upper()} cost {price_of_milk:.3f} Naira")

price_of_milk = 50
discount = 10
print(f"A tin of milk cost {price_of_milk - discount} Naira")

print("He's in China")
print("He's in \nChina")  #This mark "\" s used for escaping

print("We are the \"vikings\"")

text = "Tedprime is in Abeokuta. I love Tedprime"
print(text.count("Tedprime")) #This is to count the number of times a word appears in a string
 

## Python Booleans
num1 = 6
num2 = 12

if num1 < num2:
    print(f"{num1} is lower than {num2}")


if num1 < num2:
    print(f"{num1} is lower than {num2}")
else: 
    print(f"{num2} is higher than {num1}")

print(bool("hello"))

print(bool(0))
print(bool(7))

## Python Operators
#*Arithmetic 
#*Assignment
#*Comparison 
#*Membership 
#*Logical
#* Identity

#Arithmetic Operators: 
    #** Addition ,Subtarction, Division, Floor division, Multiplication, Modulus, Exponentiation
print(10 + 5) #Addition
print(10 - 5) #Subtraction
print(10 / 3)  # Division
print(10 // 3) # Floor division
print(10 % 3)  #Modulus
print(2 ** 3)  #Exponentiation
print(2 * 3) #Multiplication

#Assignment Operartors:
num  = 5 
print(num)
num+=2 
print(num) # num = num + 2
num-=3
print(num)
num/=2
print(num)
#Comparison operators
num = 2
print(num==5)
print(num!=3)
print(num > 5)
print(num < 2)
print(num>=2)
print(num<=7)

#Logical Operators:
## and, or , not
num = 5
# And Operators
print(num<10 and num>2)
print(num<10 and num>6)
 
 # Or: For or operators, one must be true for the print to be true, one can be true and the other should be false
num = 5
print(num<5 or num>4)
print(num<1 or num>9)

#Identity Operators
## is, is not
num1 = [2,3]
num2 = [4,5]
num3 = [2,3]

print(num1[0] is num3[0])

num1 = [2,3]
num2 = [4,5]
num3 = [2,3]

print(num1[0] is not num3[0])


#Membership Operators
## in, not in 
num1 = [2,3]
num2 = [4,5]
num3 = [2,3]

print(2 in num3)
print(2 not in num1)

"""
Assignment
1. Use the python input statement to ask for user ages and compare with age=18. If the user is less than 18, output
"You are not an adult", else if the user's age is more than 18, output "You are an adult.
2. Use python input statement to ask for user's best fruits from the collection:
fruits["mango", "orange", "apple", "banana"]
If the user's best fruit is present in the fruit collection, output "We have your fruit in stock". But if the fruit
is not in collection output "We don't have your fruit in stock"
Hint:Use input statement, membership operator,string modify methods, etc
"""

# Number One
age = int(input("Please enter your age: "))

if age < 18:
    print("You are not an adult.")
else:
    print("You are an adult.")

# Number Two
fruits = ["mango", "orange", "apple", "banana"]

best_fruit = input("Please enter your best fruit: ").strip().lower()

if best_fruit in (fruit.lower() for fruit in fruits):
    print("We have your fruit in stock.")
else:
    print("We don't have your fruit in stock.")

""" Python Sets are represented with curly brackets. They are unordered, unchangeable and do not allow duplicate values.
Duplicate values are ignored. The values and 0 are considered the same values in sets and are tre"""


"""


"""

# CHANGING VALUES IN STRINGS
thislist = ["apple", "banana", "cherry"]
thislist[2] = "orange"
print(thislist)