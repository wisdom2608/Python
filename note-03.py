print("Hello\nHow are you doing?") # This prints the str in two lines because we use a "\n" in the str

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

phrase = "John Peter"
print(len(phrase)) # Prints the number of letters in the str "len" means length

phrase = "John Peter"
print(phrase[0]) # Prints J

phrase = "John Peter"
print(phrase[-1]) # Prints r

phrase = "John Peter"
print(phrase[3]) # Prints n, etc.


phrase = "John Peter"
print(phrase.index("P")) # This prints 5

phrase = "John Peter"
print(phrase.index("J")) # This prints 0


# =====================
# Working With Numbers
# =====================
# Basic Mathematic Functions
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

# ===================================
#  Get Input From A Users
# ===================================
# Description: Here we will demonstrate how to get input from a user.
# We are basically going to allow a user to input informamation into our program.
# We are actually going to take the information the user input and store it inside a variable ...
# ... and we are going to do something with that variable.
# Getting input from a user is a great way to make your program more interactive.

name = input("Enter your name: ")
print("Hello " + name +"!")

# We can promt a user to enter more than one piece of information. 

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello " + name +"! You are " + age)

# ============================
#  Building a Basic Calculator
# ============================
# Description: In this session we will be building a very basic calculator in python.
# We will build a calculator where we will get two numbers from a user and we'll add those numbers and print our result in the screen.
# So, we will practice to get both inputs and numbers from a user.

num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ")
result = num_1 + num_2
print(result)   # The result here will not be true for whatever number a user enters. For instance 1+2= 12, which is not true'.
# This is because we didn't convert str to int.


num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ")
result = int(num_1) + int(num_2)
print(result) # The resut is correct for whatever ints a user enters. This is because we converted str variables to ints.

# We can also convert a str to a float i.e
num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ")
result = float(num_1) + float(num_2)
print(result) # The resut is correct for whatever float a user enters. This is because we converted a str variables to a float.
 
# Round up or down, the result.
num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ")
result = float(num_1) + float(num_2)
print(round(result)) 


# ==============
# Mad Libs Games
# ==============
# Description: Here we'll learn hoe to build a Mad Lib Game in puthon. 
# A Mad Lib Game is basically just a game where you can enter a bunch of random words, such as verbs nouns like name, colors,...
# ...and you take all those words and put them to a story randomly.

# To do this, we will create a varible called "color", "plural noun", and "celebrity".
color =input("Enter a color: ")
plural_noun =input("Enter a pural nown: ")
celebrity =input("Enter a celebrity: ")

print("Roses are "+ color)
print(plural_noun + " are blue")
print("I love " + celebrity)

#  -----------------------------
# Create your own Mad Libs Game
# ------------------------------


# ======
#  Lists
# ======
# Description: We'll learn how to work with lists in python. At times, when we program in python, we'll be dealing with large amt of data.
# And when you're dealing with complext data, you want to make sure that you can manage and organize it properly.
# So, list is essentially just a structure that we can use inside of python to store a list of information.
# So, we can take a bunch of data valuesWe can put them inside a list and it allows us to orgainse them and keep track of them. 
# So, generally we'll create a python list, we will put a bunch of related value inside of that list, and then we can use them to run a program.

# NB: # The name of the variable "friends" is descriptive. It describes what is in the list. We use sqr brackets "[]"to create a list
# Generally we're creating a normal variable in python, we just give it a one value. 
# So we are creating a list, we are able to store multple values inside of that list, and we can access these individual items inside of our program
# So, inside the variable container-"friends", we're storing values "Kevin", "Karen", "Jim".
# We can change one of them to a number, boolean, etc. "Kevin", 10, False. So, a list can be mixed with str, int, floats, and boolean.

# So when create a list, how do we access individual items in that list?????

# - a) We can access all the items as shown below.
friends = ["Kevin", "Karen", "Jim",] 
print(friends) # This will print all the items in the list.

# - b) We can access specific item(s) or element(s) in the list. To do this, we refere to the required element(s) by their index position.

#   - i) Index position from front of the list:

friends = ["Kevin", "Karen", "Jim",] 
print(friends[0]) # This will return Kevin because Kevin has an index position 0 from front of the list.

friends = ["Kevin", "Karen", "Jim",] 
print(friends[1]) # This will return Karen because Karen has an index position 1 from front of the list.

friends = ["Kevin", "Karen", "Jim",] 
print(friends[2]) # This will return Jim because Jim has an index position 2 from front of the list.

#   - i) Index position from back of the list:

friends = ["Kevin", "Karen", "Jim",] 
print(friends[-1]) # This will return Jim because Kevin has an index position -1 from back of the list.

friends = ["Kevin", "Karen", "Jim",] 
print(friends[-2]) # This will return Karen because Karen has an index position -2 from back of the list.

friends = ["Kevin", "Karen", "Jim",] 
print(friends[-3]) # This will return Kevin because kavin has an index position -3 from back of the list.

# Access just the portion of the list, for example, the first item.
friends = ["Kevin", "Karen", "Jim",] 
print(friends[1:]) # This will grap element at index position 1 and all other elements after that.

# -d) We can specify a range 
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby",] # Let's add a couple of other elements so we can illustrate it better.
print(friends[1:3]) # This will grap element at index position 1 upto not including 3. So, it will grap Karen, and Jim.

#                         So, this is how we can access elements inside this list.

# NB: We can a modify items in the list as shown below.
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby",] 
friends[1] = "Mike" # We are changing or replacing the element ("Karen") in index postion 1 to (with) another element called "Mike".
print(friends[1])   #  So, when we print value in index position 1, it will be updated to Mike instead of Karen.


# ================
#  List Functions
# ================
# Description: Here we will talk about using a function with lists in python. In python, a list is one of the most important structures when we
# ... store information. A list basically allows you to take a bunch of given values, organise them, and store them inside of theor own "little list" structure.
# So, below we've a list of lucky numbers and list of friends. These two lists are storing a bunch of different values.
# What makes it awesom is, not only can we store only these limited values, we can store hundreds and thousands of millions of values.
# When you are working with a lot of data and a lot of information python, this lists are invaluable. 
# So, because this list is important, there's actually different functions that we can use with list. And these functions allow to do things like ...
# ...modify the list, get information about the list.
 
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby',] 
print(friends) # This will print the elements in the list.

# There are lot of other functions that we can use. This is called the "extend" function. It allows us to take a list append another...
# ...list on to the end of it.

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby',] 
friends.extend(lucky_numbers) # Here we pass the list we want to append to the end of "friends" list inside the extend function
print(friends) 

# We can also just individual elements on to a list.
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby',] 
friends.append('Creed') # This will add "Creed" as a new item to a friends list. The item added is at the end of the list
print(friends) 

# Let's say we want to add an item inside the middle of the list, there's another list function called "insert".

# The insert fxn takes two parameters. The first is the indext where you want to store the value, the second is the new value.
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby',] 
friends.insert(1, 'Cathe') # The index position here is 1, and new element we want to insert is Cathe. All other values will be pushed to the right.
print(friends)

# Let's say we want to remove an element from the list. Here we use a list function called "remove".
# We add the function and pass the element we want to remove without necessarily pricising its index positon. Example,

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby',] 
friends.remove('Jim')    # The will remove Jim from the list.
print(friends)


# Remove all the elements from the list
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby',] 
friends.clear()    # The will empty the list.
print(friends)

# There is also another function called "pop". "pop" function gets rid of the last element inside the lis
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby',] 
friends.pop()    # The last element disappeared. So, it cleared off 'Toby'
print(friends)

# Let's figure out if a certain element exists in this list. Let's say we want to check if our friend 'Kevin' is in the list.
# Here, we use .index and pass the value(the name of the element).

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby',] 
print(friends.index('Kevin')) # This tells us the index of Kevin or tells us if Kevin is in the list.

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby',] 
print(friends.index('Jim')) # This tells us the index of Jim or tells us if Jim is in the list.

# If we put a Name that is not in the list, if print an error message to us. For instance
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby',] 
print(friends.index('Paul')) # We'll receive an error message since the element-Paul is not in the list.

# We can actually count the number of similar items in the list.
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Jim', 'Jim', 'Oscar', 'Toby',] 
print(friends.count('Jim')) # This counts the number of times, the element-Jim shows up inside the list. It will return a 3.


# We can also sort the values in the list.
# This Puts items in the list in alphabetical order.
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby',] 
friends.sort()
print(friends) # This will sort or arrange the list in ascending order. The ouput is ['Jim', 'Karen', 'Kevin', 'Oscar', 'Toby']

# This can also work for lucky numbers
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby',] 
lucky_numbers.sort()
print(lucky_numbers) # This will sort or arrange the list of "lucky_numbers" in ascending order. The ouput is [4, 8, 15, 16, 23, 42]

# We can also reverse a list. This arranges numbers or in descending order(from bigger down to smaller).
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby',] 
lucky_numbers.reverse()
print(lucky_numbers) # This will reverse or arrange the list of "lucky_numbers"  in descending order. The ouput is [42, 23, 16, 15, 8, 4]

# There is another list function called "copy". We can actually create another list and make it as a copy. For example 
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby',] 
friends2 = friends.copy() # "friends2" will have all the same attributes as "friends"
print(friends2) 


# =======
#  Tuples 1:18:59
# =======
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
#  Ask the year you are born 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
#  Ask the year you are born 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
#  Ask the year you are born 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
#  Ask the year you are born 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
#  Ask the year you are born 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
#  Ask the year you are born 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
#  Ask the year you are born 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
#  Ask the year you are born 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
#  Ask the year you are born 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
#  Ask the year you are born 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
#  Ask the year you are born 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description:

# ===================================
#  Ask the year you are born 
# ===================================
# Description:

# ===================================
# 
# ===================================
# Description: