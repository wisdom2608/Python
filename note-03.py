name = "John Peter"
print(name.upper()) # This print name all in uppercase

name = "John Peter"
print(name.lower()) # This print name all in lowercase

name = "John Peter"
print(name.replace("John Peter", "John Paul"))  # This replaces John Peter with Jphn Paul

phrase = "John Peter"
print(phrase.isupper()) # This asks if the str in the phrase container variable is in CAPS. The return is a "False". This because all the letters in the str are not in upercase.

phrase = "John Peter"
print(phrase.islower()) # This asks if the str in the phrase container variable is in CAPS. The return is a "False". This because all the letters in the str are not in lowercase.

phrase = "John Peter"
print(phrase.upper().isupper()) # This coverts the str in the phrase container variable to CAPS, and then asks if it's upper. the return is "True".

phrase = "John Peter"
print(phrase.lower().islower()) # This coverts the str in the phrase container variable to lowercase, and then asks if it's in lowercase. the return is "True".

num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ")
result = num_1 + num_2
print(result)   # The result here will not be true for whatever number a user enters. For instance 1+2= 12, which is not true'.
# This is because we didn't convert str to int.


num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ")
result = int(num_1) + int(num_2)
print(result) # The resut is correct foer whatever ints a user enters. This is because we converted str variables to ints.


# Basic MAthematic Functions
print(3 + 4)
print(3 * 4 + 5)
print(3 * (4 + 5))
print(10 % 3) # "10 % 3" is read "10 mod 3". % is a modular sign. This will preturn the remainder of 10 divided by 3, which is 1.

number = 5
print(number)

# Convert a number in to a string.
# This happens when you wanna print a number alongside str
number = 5
print(str(number) + " is my favourite number")

# =============
# Math Function
# =============

# There are bunch of different math functions that we can use on our numbers. A function is say a collection of code that does something.
# A function could perform operation like a mathematical operation, it can also give us information about a number.
# Below are some of the most common functions used in python.

number = -5
print(abs(number)) # Absolute value of -5
print(pow(4, 2))   # This prints 4 raised to the power of 2
print(max(8, 3))   # This will return the lager of the two numbers passed in the function, which is 8
print(min(8, 3))   # This will return the smallest of the two numbers passed in the function, which is 3
print(round(3.2))  # This will round the number down to 3
print(round(3.7))  # This will round the number down to 4


# ========================
# Importing Math Functions
# ========================

# There are few other functions but in order to get access to them, we have to do what is called importing.
# In Python, we actually import external codes into our files. So if we want to import this code, we use "from math import *". 
# This will graop a bonch of different math function that we can use

from math import * # This will graps a kind of math's different functions that we can use. The "math" is called a Math Module.
print(ceil(3.6)) # Round the number up

print(floor(3.6)) # Round the number down
print(sqrt(36)) # Return the squared root of 36