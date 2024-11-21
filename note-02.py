# ==============================================================================================
# Run your first python program. With this piece of code, you can print your name on the screen.
# ==============================================================================================

print("wisdom python")

# ====================
# How to draw a dog
# ===================

print("0----")
print(" ||||")

# Description: What we have understand in the codes above is that python codes get executed line by line from the top.
# ...we saw python enterpreter, that is the program that knows how to translate or interpret a python code into....
# ...instructions that a computer can understand. 

# ======================================
# How to multiply a string by any number
# ======================================
 
print("*" * 10)

# Description: Aywhere we have quotations "" or '', we are defining a string. A string is a programming term which means...
# ...which means a series of characters. So, "Wisdom python", "0----",  " ||||", "*", are all strings.
# ("*" * 10), means we are multiplying the string "*" by number, 10. The asterek is the multiplication operator just like the ...
# ...operator we have in math.  With this piece of code, ("*" * 10), we call draw 10 astereks on the terminal.
# What we have <"*" * 10>, on the the piece of code, print("*" * 10) is called an expression. An expression is a piece of code that ...
# ... produces a value. So, when python interpreter wants to print a code, it evaluates the code we put in the parenthesis. 
#  Here, ten astereks will be printed on the terminal..

# =================
#    Variables 
# =================

price = 10 
print(price)

# Description: Variables in python are one of the most fondamental concepts in programming, specifically to python.
# We use variables to temporary store data in a computer's memory in binaries (a serie of 1s, and 0s).
# when python interpreter executes this code, it will allocate some memory that will store a number, 10 in that memory.
# Finally, it will attach the label "price" in that memory location. Imagine we have a box numbered 10, and "price" is the label we put..
#.. in the box. We can use the labe everywhere in the program to access the value that we have in that box.
# To print the value of the variable, we type <print(price)> without quotation in the parenthesis. This because we want to print a variable, "price".
# This will print the number, 10 on our terminal.

# ===================================
#   Update the value of Variable
# ===================================

price = 10 
price = 20
print(price)

# Description: If we reset it to a new value like 20. When we run the program, we should see 20.
# Remember, python interpreter execute a code line by line from the top.

# ====================================================
#  Variables With Integers and Floating Point Numbers
# ===================================================

price  = 10 
rating = 4.9
print(price)

# Description: The numbers 10 in the piece of code above is called integer. It is a number without a decimal point. we can also use number...
# with decimal point such as 4.9, 2.5, etc, they are called floating point numbers.

# ===================================================
#  Variable With String, And Variable With Boolean
# ====================================================

name = "Wisdom"
is_published = True 
is_in_school = False
print(name)
print(is_published)
print(is_in_school)

# Description: We can also define a variable and set it to a string. For instance name ="Wisdom"
# A boolean can be <True>, or <False> but not like "Yes" and "No" in English Language. We use underscore(_) to separate
#..multiple words in a variable's name. For instance "is_published". The False and True are called boolean values.

# NB: Python is case-sensitive language which is sensitive to lowercase and uppercase letters. So, we use lowercase letters when defining variables.
# But the boolean True, and False are special key words in python language. So, Python will not understand it when spell "true" istead of "True", or "false" instead of "False"
# Summary: This exercise we are storing simple values in a computer's memory. Simple values can be numers (such as integers, floats), string, and booleans.

# In python we can also store complex values like <lists>, and <objects>.

# ******************
# Proof of Concept 
# ******************

# Imagine we want to write a program for a hospital. So, we check in a patient named Wisdom Faith. He's 20 years old and is a new patient

# Work Required
# Define:
# - three variables for his name, his age and another variable to tell if it's a new and existing patient.

#          Solution
name = "Wisdom Faith"
age = 20
is_new =True

# ===================================
# How to Receive input from the user
# ===================================

name = input("What is your name? ") # The space after the "?" means the cursor should be seperated from the question mark. Otherwise will be so closed. 
print("Hi " + name)            


# NB:Without the space, the output is < What is your name?|> but with the space, the output is < What is your name? |>

# Description: We going to write a small program that asks the username and then will print a greeting message customized for that user.
# So, instead of <print>, we will use <input>. Both these <input>, and <print> are functions that built into python. As a matter of fact, think of the remote control..
#...of your TV. On this device, we have a bunch of bottons. These bottons are function built into your TV. You can turn it on, turn it of, change channel, reduce the volume, etc.
# In python we also have a bunch of functions for common task such printing message, receiving inputs, and so on. We are going to use the <input> function and whenever we have..
# ...parenthesis, it's like recalling what executes that function. It's like princing a botton on a remote control. 
# Let's call an <input> and in between parenthesis we are going add a string, enabling it to print something on the terminal. ie input("What is your name? ").
# This contains a question mark (?), followed by a space. That is, input("What is your name? ")
# Ths <input> function will print the message < What is your name? > on the terminal and will wait for the user to enter a value. Whatever the user enters, the <input> function will return.
# We can get that value and store it in a memory using a variable. So get the result and store it in variable called name.

# On the second line of our code we want to print a message like "Hi Wisdom Faith!". To do this we type print("Hi ") with a space and after the quotation, we...
#... want to dynamically print what we have in the < name variable >. That is print("Hi " + name). W are concatinating or combining the string...
#..another string (ie is what we have in the name variable.) SO, the <"Hi " + name> is another example of expression (it is a piece of code that produces a value). 

# The output of the piece of code above --
#    < What is your name? > and if put my name, say "Wisdom Faith", it will print "Hi Wisdom Faith" 

# ******************
# Proof of Concept 
# ******************

# Ask two quesions: person's name and the favourite colour.
# The print a message like "Wisdom likes pink"

name = input("what's your name? ")
favourite_color = input("what is your favourite color? ")

print(name + ' likes ' + favourite_color)

# ===================================
#  Ask the year you are born 
# ===================================

birth_year = input("Birth year: ")
age = 2019 - birth_year
print(age)

# Description: We are going to ask the year we were born in, it will calculate our age and print it on the terminal.

# With this program <print(age)>, we are going to get an error message. This is because in <age = 2019 - birth_year>, we are subtracting a string (str) from an integer (int)...
# ...and python does not understand it. To do this correctly, we convert the str into int. For example python does not recognize 1982-"1942". This is..
# ... this is because, one is an int (1982) and the other is a str. Python will recognize it if we convert str to int. That is 1982 - int("1942")
# We can convert str to boolean function, boolen(), to int function, int(), and to float function, float(). Let's fix the problem above

birth_year = input("Birth year: ")
age = 2019 - int(birth_year) # Here, we've passed the str into int function so that python interpreter will be able to evaluate the expression.
print(age)

# Python also has a useful function for getting the type of variables. For instance let's print the type of birth year as shown below

birth_year = input("Birth year: ")
print(type(birth_year)) # <type> in this case is a build-in function because it's passed in another function <print>
age = 2019 - int(birth_year)
print(type(age))
print(age) # The output here will be <class 'str'> and <class 'int'>. this means the "birth_year" variable is a str, and the "age" variable is an int.

# Conclusion: This is what you need to take away. Whenever you use the input function, you always get a string. When you are expecting any numerical value,...
# ... you should always convert that str into an int, or a float.

# ******************
# Proof of Concept 
# ******************

# Write a program. Ask a user their weight (in pounds), convert it to kilogram and print on the terminal.

weight_lbs = input("Weight in (lbs): ")
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)


# ===========================
#  More About Python Strings
# ===========================

 # --------------
 # Short String
 # -------------

# Description: We can use single('') or double ("") quotes to define a string.

course = 'Python for Beginners.' # Our string is in single quote.
print(course)

# Output: Python for Beginners.

# Imagine we want to print something like this <Python's Course for Beginners>. Here, We must use double quotes in our string.

course = ("Python's Course for Beginners.")
print(course)

# Output: Python's Course for Beginners.

# We can also use double quote within single quote in a string

course = 'Python for "Beginners".' # Our single-quote string contains double quotes within.
print(course)

# Return: Python's Course for "Beginners".

# ------------------------------------
# Define a string with multiple lines or a message that you can send in an email. In this case, we use tripple quotes
# ------------------------------------
course = ('''
Hi Wisdom,

Here is our first email to you.

Thank you,
The support team
''' )  # Tripple quotes here can be single (''' '''), or double quote (""" """). With this, we can difine a string that spans multiple lines.
print(course)
 
# ============================================
#  Other Characteristics of Strings in Python
# ============================================

# Description: Here we can a square bracket "[]" to get the xter and a given index in the string. To get the first xter, we use square bracket and 0 (zero)
# The index of the first xter is 0, second xter 1, 3r xter, 2 etc. 

course = ('Python for Beginners.') # Letter "P" is the first xter in the course variable
print(course[0])

# Output: P 

# NB: We can also use a negative index here, and this is one of the features that we don't have in other programming languages as far as we know. But with ...
# ... negative index, we will get letter "s".Assuming 0"" is the index of the first xter "P", in the variable, then "-1" will be the index of the last xter, "s".

course = ('Python for Beginners.') # Letter "P" is the first xter in the course variable
print(course[-1]) # If we pass -1 instead of 0, we will get "s".

# Output: s

# You can try indices such as 2, 3, -2, -3 etc, and see what the ouput is gonna be.

# Can also use the square bracket "[]" syntax to extract a few xter instead of just one xter. For example

course = ('Python for Beginners.')
print(course[0:3]) # Here Python interpreter will return all the xters starting from the start index (0) to end index (3), but it does not return the xter at index 3. That is from "P to t".


# Output: Pyt

# We also have default values for the "start" and "end" index. So, if you don't supply the end index, Python will return all the xters to the end of the index, 0
# This will print all the xters in the string.

course = ('Python for Beginners.')
print(course[0:])

#Output: Python for Beginners.

# But if you change the first index to 1, it will  exclude the first xter in the string.

course = ('Python for Beginners.')
print(course[1:]) # letter "P" is excluded (rmoved) from the output. This means the default value for the start index is 1.

# Output: ython for Beginners.

# Now, if we do not supply the start index add an end index, say 5, Python will assume zero as the start index. With this syntax, we can easily copy or clone our string.

course = ('Python for Beginners')
print(course[:5]) # The end index, 5 means Python will count the first 5 xters starting from 0 . That way the xter, "n" is not included  [0(P), 1(y), 2(t), 3(h), 4(o),] These indices make up five (5) xters. [0, 1, 2, 3, 4, 5] This makes up 6 xters

# Output: Pytho 

# What if we leave both the start and end index? In this case zero(0) will be assumed as the start index and the length (len) of the string will be assumed as the end index.
# With this syntax, we can basically copy or clone our string.

course = ('Python for Beginners')
another = course[:] # This expression will all the xters in the course variable. The second variable "another" will be a copy of first variable "course"
print(another) 

# ******************
# Proof of Concept 
# ******************

# Define a variable called "name" and set it to "Wisdom"
name = 'Century'
print(name[1:-1])

# Output: entur



# Output: Python for Biginners.
# ===================================
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
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
# 
# ===================================
# Description:
