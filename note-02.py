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

# Output: Python for Biginners.

# ******************
# Proof of Concept 
# ******************

# Define a variable called "name" and set it to "Wisdom"
name = 'Century'
print(name[1:-1]) # What do you think will be the output? 

# Output: entur

# ==================================================
#  Formatted Strings in Python Programming Language
# ==================================================

# Description: Formatted string are useful in situations where you want to dynamically generate some texts with your variables. 
# Let's set two variables for first_name and lsat_name name. We want to obtain an output which is like "Wisdom Faith is a coder" What do we do?
first_name = 'Wisdom'
last_name = 'Faith'
message = first_name + ' ['+ last_name + '] is a coder'
print(message)

# Output: Wisdom [Faith] is a coder

# While the approach above perfectly works, it's not ideal because as our text gets more complicated, it becomes harder to visualize the output.
# So, someone reading the code < first_name + ' ['+ last_name + '] is a coder' >, they have to visualize all these strings concatinations in the head. 
# ... This is where we use formatted strings. There make it easier for us to visualize the output. Example 

first_name = 'Wisdom'
last_name = 'Faith'
message = first_name + ' ['+ last_name + '] is a coder'
msg = f'{first_name} [{last_name}]  is a coder' # Let's define another variable and set it to a formatted string. formatted string is one which is prefixed with an "f"
print(msg)

# Output: Wisdom [Faith] is a coder

# To define formatted string, prefix your string with an 'f' and use curly braces to dynamically insert values into your strings.

# ===================================
#             String Method
# ===================================

# Description: There are some cool things we can do with Python strings. To calculate the number of xters in a str, we can use a build-in function called "length (len)". 

course = 'Python for Beginners.'
print(len(course)) # the len function prints the number of xter in the variable "course"

# Output: 20 

# NB: This useful when we receive input from the user. For example, You have noticed that when you fill out a form online, each input filled will often has a limit.
# For example, you may have 50 xters for your name. Using this len function, we can enforce a limit on the number of xters in an input filled. 
# If the user types in more xters than we allow, we can display an error. This len function <(len(course))> is another function built into Python. 
# It is a general purpose function. So, it is not limited to counting the number of xters in a str. When we use this function to count the number of item in the list.

# -------------------------------
#  Functions Specific To Strings
# -------------------------------
#--------Converting a str into uppercase:

# Description: These are functions that can convert xters in a str into Uppercase or Lowercase xtersc. To access these functions, we use the "dot operator"
# In More accurate term we refere to these functions as methods. This is a term in object granted programming. When a function blongs to something else or is specific to ...
# ...some kind of object, we refere to that function as a method. Example that ends with "dotupper" <.upper> converts a string to uppercase as well as a function that ends
# with "dotlowerr" <.lower> converts a string to lowercase. In contrast print and len < print(len()) >, are general purpose functions cos they don't belong to str or numbers or a particular oject.

course = 'Python for Beginners.'
print(len(course))
print((course.upper)) # This will display all the xters in variable in uppercase.

# Output: PYTHON FOR BEGINNERS.

# This method does not change or modify the original str. It creates a new str and returns it.

#----------Convertin a str into lowercase
# Description: Here, we change the < dotupper > to < dotlower >
course = 'Python for Beginners.'
print(course)  
print((course.lower)) # This will display all the xters in variable in lowercase.

# Output: python for beginners.

# Try this and see the output!!!!!!!!
course = 'Python for Beginners.'
print(len(course))
print((course.lower))
print(course)
print((course.upper))
# Output: "20", "python for beginners.", "Python for Beginners.", "PYTHON FOR BEGINNERS." in this order.

# ========================================== 
# Find a xter or a sequence of xter in a str 
# ==========================================

# Description: There are times you want to find a xter or a sequence of xter in a str. In those situations you can just define “method“.

course = 'Python for Beginners.'
print(course.find('P')) # This will return the index of the first occurrence of that xter. 

# Output: 0

# This because the index of the first capital letter “P” is zero. If you pass the index of “o”, we’ll get 4 as an output. If we pass “O”, we’ll get “-1” as the output because we don’t have an uppercase, O anywhere in the str.

# We can also pass a sequence of xters say, “Beginners”. We will get “11” as output because the word Beginners” starts at index 11.

course = 'Python for Beginners.'
print(course.find('Beginners'))

# Output: 11

# ------------------------------------------------
# A Method to replace a xter or a sequence of xter
# ------------------------------------------------

# Description: We can also have a method to replace a xter, or a sequence of xters, and that is called “replace”. 

course = 'Python for Beginners.'
print(course.replace('Beginners', 'Absolute Beginners.')) # This will replace Biginners with Absolute Biginners

# Output: Python for Absolute Beginners.

# This function “replace” is case sensitive. If we pass “biginners” instead of “Beginners”, this method is not gonna replace “Beginners” with “Absolute Beginners” because...
# ...it didn’t find the word “beginners” in the str. So the output will remain the same as in the variable.

course = 'Python for Beginners.'
print(course.find('beginners', 'Absolute Beginners')) # We will still get “Python for Beginners.”

# Output: Python for Beginners.

# We can also replace a single xter, say “P” with “J”

course = 'Python for Beginners.'
print(course.find('P', 'J')) # This replace letter P with letter J.

# Output: Jython for Beginners.

# --------------------------------------------------------------------
# How to check the existence of a xter or a sequence of xters in a str
# ---------------------------------------------------------------------

# Explain: There are times we want to check the existence of a xter or a sequence of xters in our str. 
# In those situations, we use the “in” operator. Let’s say if we want to know this str contains the word “Python”, we can an expression as shown below

course =  'Python for Beginners.'
print('Python' in course) # We are checking to see if “Python” is in the course variable.

# Output: True

# We refer to this expression as a Boolean expression because it’s an expression that produces a Boolean value like a “True” or “False“.
# If we change “Python” to “python” we will get False because we don’t have this exact sequence of xter-“python” in our str

course = 'Python for Beginners.'
print('python' in course) # We are checking to see if “python” is in the course variable.

# Output: False

# The difference between the “find” method and the “in” operation is that the “find” method returns the index of a xter or sequence of...
# ...xters in a str while the “in” operator returns (produces) a Boolean value.

# Summarily

# - we can use a function to count the number of xters in a str. It’s a general purpose function built into Python.
# - we also have specific functions for a str which we refer to as “methods”. These include “upper” for converting a str to uppercase, ...
# - “lower” for converting a str to lowercase, and “tittle” method, the “find” method which returns the index of a xter or sentence of xters, ...
# - the “replace” method for replacing xters or words in a str, and finally the “in” operator which says whether there are some xters in str or not.

# ====================
#  Aritmetic Operation
# ====================
# Description: In Python programming language, we have two types of numbers, int and float. 
# Here we will be looking at arithmetic operations supported in Python language. These are the same arithmetic operations that we have  math. we can add numbers, ..
# ... subtract, multiply, divide them, etc. For example:
print(10 + 3) # For addition operator. Output: 13
print(10 - 3) # For subtraction operator. Output: 7
print(10 * 3) # For multiplication. Output: 30
print(10 ** 3) # For exponential. This returns 10 to the power of 3. Output: 1000

# There are two types of division:
# - division with a float
print(10 / 3) # Division operator is a single forward slage. This produces a floating point number. Output: 3.3333333

# - division with int
print(10 // 3) # Division operstor is a double forward slage. This produces an int number. Output: 3


print(10 % 3) # Modular operator which is a percent (%) sign. This returns the remainder of the division. Output: 1

# For these operators, we have an augmented assignment operator which is very useful. For example
X = 10
X = X + 3 # Python interpreter will add 3 to 10 and the result is 13.

# ------------------------------
# Augmented assignment operator
# ------------------------------

# Augmented assignment operator is a way to write the same code but in a short form.

X = 10
X += 3 # What we’ve on this line is the same as what have above ‘X = X + 3’
print(X)

# This is what we call the augmented assignment operator or enhanced assignment operator.

# We can also subtract or multiply a number by a given value. That’s 

X = 10
X -= 3 # Here we’re subtracting 3 from X 
print(X) # Output: 7

X = 10
X  *=  3
print(X) # Output: 30

# --------------------
# Operator Precedence 
# ----------------------

# Description: Let’s say you define X and set it to 10 + 3 * 2. That is X = 10 + 3 * 2. 
# What do you think will be the answer when you run the program? 
# This is a very basic math operation that unfortunately a lot of people fail to answer.
# The answer is 16. This is because in math we have a concept called “Operator Precedence“.  
# Which means that the order of operations . So, the multiplication operation has the higher precedence, ...
# ..so, it’s applied first. Which means 3*2 and the result is added to 10. 

X = 10 + 3*2
print(X) # Output: 16

# =================
#   Math functions
# =================

# Description: Here we’re going to see some build-in functions used for mathematics. 
# To round functions, we can used the build-in round function called “round”.

X = 2.9
print(round(x)) # Output: 3

# We have another useful build-in round function called “abs”, which is short form of “absolute”.
# This is the absolute function that we have in math. 
# We give it a value and it always returns the positive representation of that value even that value is negative.
# For example,

X = 2.9
print(abs(-2.9)) # Output: 2.9

# Technically in Python we have a handful of build-in function for performing mathematical operations. 
# If we want to write a number that involves complex mathematical calculations, we need to import the math module. 
# The module in Python is a separate file with some reusable codes. 
# We use these modules to organize our codes into different files.
# As a matter of fact, think of a supermarket.
# When you go to a supermarket, you see different sections for fruits and vegetables, cleaning products, junk food, etc.
# Each section in the supermarket is like a module in Python.
# In Python we have this math module which contains a bunch of reusable functions for performing mathematical calculations. Example:

# “import math” math is an object like a str. We can access it functions or more accurately its methods using a “dot” operator.

import math
print(math.ceil(2.9)) # Return: 3

# ceil gets the ceiling of a number.

import math
print(math.floor(2.9)) # Return: 2

# To learn more about these functions or methods,search for “Python 3 math module” in google or click on the link
# ( https://docs.python.org/3/library/math.html)


# ==============
# If Statements
# =============

# Description: If statements are extremely important in programming as there allow us to build programs that can make decisions based on some conditions. So, if some conditions is true, we are going to do certain things otherwise we are going to do other things. Let’s consider this text file with a bunch of rules for a program:

#            “ If it’s hot
#                It’s a hot day
#                Drink plenty of water

#            otherwise if it’s cold drink
#                It’s a cold day
#                Wear warm clothes 
#            otherwise 
#                It’s a lovely day ”

# Let’s write a program that simulates these rules. We start by defining a Boolean variable 
is_hot = True
if is_hot:
    print("It's a hot day")
print('Enjoy your day')

# Output: It's a hot day
#         Enjoy your day

# But if we change the "True" boolean value to "False", the out is as such:
is_hot = False
if is_hot:
    print("It's a hot day")
print('Enjoy your day')

# Output: Enjoy your day

# Let's add anothe "print" statement indented with the "if" condition, say "print('Drink plenty of water')"
# Because the second print statement is indented, it will be printed if the condition is true. example,

is_hot = True
if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
print('Enjoy your day') 

# Output: It's a hot day
#         Drink plenty of water
#         Enjoy your day  
     
 # It will print the first two messages, otherwise the condition is False. But if we want a differnt statement even when the condition is false,..
 # ... we use the "else" statement. Example, let's maintain the condition to be true.

is_hot = True
if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
else:
    print("It's a cold day")
    print('Wear warm clothes')    
print('Enjoy your day')  

# Output: It's a hot day
#         Drink plenty of water
#         Enjoy your day

# Now let's change the condition to False, we have the output as shown below.

is_hot = False
if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
else:
    print("It's a cold day")
    print('Wear warm clothes')    
print('Enjoy your day')  

# Output: It's a cold day
#         Wear warm clothes
#         Enjoy your day

# NB: But if it's not hot, it doesn't necessarily mean that it's cold. Maybe it's a lovely day. The abcence of heat doesn't mean it's cold.
# This means we should add another variable. Here, we use use an "elif" statement to define the second condition.

# Output when all variable are set to True.
is_hot = True
is_cold = True
if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
    
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes')  
else:
    print("It's a lovely day")  
print("Enjoy your day")

#  It's a hot day
#  Drink plenty of water
#  Enjoy your day

# Output when the "is_hot" variable is set to True a "is_cold" variable is set to False.
is_hot = True
is_cold = False
if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
    
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes')  
else:
    print("It's a lovely day")  
print("Enjoy your day")

#  It's a hot day
#  Drink plenty of water
#  Enjoy your day

# Output when the "is_hot" variable is set to False a "is_cold" variable is set to True.
is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
    
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes')  
else:
    print("It's a lovely day")  
print("Enjoy your day")

#  It's a cold day
#  Wear warm clothe
#  Enjoy your day

# Output when the "is_hot" variable is set to False a "is_cold" variable is set to True.
is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
    
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes')  
else:
    print("It's a lovely day")  
print("Enjoy your day")

#  It's a cold day
#  Wear warm clothes
#  Enjoy your day

# Output when all variable are set to False.
is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
    
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes')  
else:
    print("It's a lovely day")  
print("Enjoy your day")

#  It's a lovely day
#  Enjoy your day

# It's neith hot or cold, so it's going to be a lovely day.

# ------------------
# Proof of concept:
# ------------------
#          Imagin the price of a house is $1M. 
#          If a buyer has good credit,
#          they need to put down 10% of the price of this property
#          otherwise 
#          they need to put down 20%
# WR: Write your program with these rules and display the down payment required for a buyer with good credit

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price

else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

# ====================
#  Logical Operators
# ====================

# Description: We use logical operators in situations where we’ve multiple conditions. 
# For example, let’s say we’re building an application for processing loans.
#           “If an applicant has higher income AND good credit, then they’re eligible for loan”.
#           In this example we have two conditions one is “high income“, and another is “good credit”.
#           If both of these conditions are true, then the applicant is eligible for loan. 
# This is where we use the logical “AND” operator. We use this operator to combine two conditions.

has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan") # Output: Eligible for loan

# But one of these conditions if False, we are not doing to see the output “Eligible for loan”

has_high_income = False 
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan") # Output: Eligible for loan

# We also have the logical “or” and we use it in situations...
# ...where we wanna to do certain things if at least one of the conditions is true. 
#           “If an applicant has higher income OR good credit, 
#              then they’re eligible for loan”.

has_high_income = False 
has_good_credit = True
if has_high_income or has_good_credit:
    print("Eligible for loan") # Output: Eligible for loan

# If both of these conditions are false, we will not see any output.
# We also have another logical operator called, “NOT” and this basically inverses any boolean value we give it.
# If given a true boolean value, it will inverse it to false.  For example let’s add another rule to our question.

#        “If an applicant has higher income AND good credit, then they’re
#            Eligible for loan.
#        If applicant has good credit AND does not have a criminal record
#           then they are Eligible for loan”.


has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan") # Output: Eligible for loan

# If the applicant has criminal record, it means he’s not eligible. So there will be no message.
has_good_credit = True
has_criminal_record = True
if has_good_credit and not has_criminal_record:
    print("Eligible for loan") # Output: Eligible for loan

# ======================
#  Comparison Operators
# ======================

# Description: We use comparison operators in situations where we wanna compare a variable with a value. For example,

#              “If temperature is greater than 30
#                 it’s a hot day
#              otherwise if it’s less than 10
#                it’s a cold day
#              otherwise it's  neither hot nor cold”. 

# To build these rules into our program, we need to use comparison operators.

temperature = 30
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# Output: It’s not a hot day. This is because 30 is not greater than 30. 

# If we change the variable value to 35, we will see a different message. For instance,

temperature = 35
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# Output: It’s a hot day

#            We have other operators such as
#            != means not “equal to”
#            ==  means “equa to”
#            <= “less than or equal to”
#            => “greater than equal to”
#            so we can use conditions for our conditional statements Example

temperature = 35
if temperature >= 30:
    print("It's  a hot day")
else:
   print("It's not a hot da")

# -------------------
# Proof of concept 
# -------------------
# You must have realized that when you fill a form online, sometimes the input fields have validation messages. 
# For example, let say we have an input field for the user to put in their name. 

name = "W"
if (len(name)) <  3:
    print("Name must be at least 3 characters")
elif (len(name)) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")

# Output: Name must be at least 3 characters
name = "Wounded"
if (len(name)) <  3:
    print("Name must be at least 3 characters")
elif (len(name)) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")

# Output: Name looks good

name = "Woundeujkkkkfdsnbhaiigibnwerhiopdmfnvbh"
if (len(name)) <  3:
    print("Name must be at least 3 characters")
elif (len(name)) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")

# Output: Name must be a maximum of 50 characters

# =============================
#    Project: Weight Converter 
# ============================

# Description: We want to build a program to convert someone’s weight from pound(lbs) to kilogram (kg).
# We want to extend the program and allow users to enter their weights either in kg or lbs and then we...
# ...will convert it to the other units. 

#        If name is less than 3 characters long
#        name must be at least 3 characters 

#        otherwise if it’s more than 50 characters long 
#        name can be a maxim of 50 characters 
#        otherwise 
#        name looks good

weight = int(input('Weight:  '))
unit = input('(L)bs or (K)g:  ')
if unit.upper() == 'L':
    converted = weight *0.45
    print(f"You are {converted} kilos")
else:
  converted  = weight / 0.45
  print(f"You are {converted} pounds")

# =============
#  While Loops
# =============

# Description: Here we are going to learn how to use "while loops" in python.
# We use while loops to execute a block of code multiple times.
# There are often useful in building interactive program and games. We shall learn how to build a simple game using a while loop 

i = 1
while i <= 5:
    print(i)
    i = i + 1
print('Done')

# We can make this program more interestin. With the expreesion below, we can repeat the str. 
# When we multiply a str with a number, that str will be repeated.

i = 1
while i <= 5:
    print( '*' * i ) 
    i = i + 1
print('Done') # The output is a little triangula shape.


# ==============
#  Guessing Game
# ==============
# Description: Here we'll learn how to use a "while loop" to build a guessing gameSo, we have a secrete number which is set to 9. 
# Now the computer is asking to make a guess. We've have only three chances to guess the correct number. 
# If we guess the number wrongly for three times the output will be "Sorry you filed!".
# If we guess the number correctly, the output is "You win!"

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
