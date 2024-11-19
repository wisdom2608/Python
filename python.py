print("Buea is the most beautiful town")
#=========================================
# How to use variables
#=========================================
bucket_color ="red" # A variable called "red_bucket"
print(bucket_color)

# If we assign different values to the same variable, the most recent value of the variable is printed.
bucket_color ="red" 
bucket_color ="10" # The integer , 10 will be printed because it's the news variable.

print(bucket_color)

# delete a variable
bucket_color ="red"
del bucket_color  # del means delete
print(bucket_color) # this will not print bucket_color because it's been deleted

#Know the type of variable
bucket_color ="red" 
bucket_color ="10" # The integer , 10 will be printed because it's the news variable.

print(type(bucket_color)) # The output shows that 10 is an integer and red is a string.


papa_age = 7
mama_age = 45
if papa_age < mama_age:
    print("papa should be in a day school")
elif papa_age == mama_age:
    print("another school")
else:
    print( "papa shoud be home" ) 

#=========================================
# Printing the same sentence so many times. It becomes stressful do correct these sentences if they have errors.
#=========================================
print("Max is on the way to schocl")
print("Max is on the way to schocl")
print("Max is on the way to schocl")

#===========================================================================
# Using a function to define a sentence that you want to print somany times. It becomes easy do correct these sentences if they have errors.
#===========================================================================
def njilap_town():  # <def> means <definition> which python recognizes it as a function
    text ="Max is on the way to schocl" # The <text> under the function is called variable
    print(text)
    print(text)
    print(text)
#These lines of code below calls the function above. The "schocl" typo can be corrected only on a single line.
njilap_town () # 1st call prints the fxn 3 times
njilap_town () # 2nd call prints the fxn 6 times
njilap_town () # 3rd call prints the fxn 9 times

#==============================================
# never call the function before defining it 
#===============================================

njilap_town ()

def njilap_town(): 
    text ="Max is on the way to schocl" 
    print(text)
    print(text)
    print(text)
# We don't get any output of a function if we call the function before defining it.
    
njilap_town ()

def njilap_town(): 
    text ="Max is on the way to schocl" 
    print(text)
    print(text)
    print(text)    
# ======================================
# Passing a variable in the function
#=======================================


def njilap_town(text): 
    print(text)
    print(text)
    print(text)
njilap_town("Max is on the way to schocl" )

# ===============================================
# How to put the <if> statement within a function
#================================================

def school_age_calculator(age,name): #Based on the child's age, when should they be in school? we want to get two different values. the child's age, and name.
    if age < 5:
        print("Enjoy the time!" ,name, "is only", age) # Earlier we've been printing out only texts. Now weáre printing texts including variables <name>, <age>.
    elif age == 5:
        print("enjoy kindergaten,", name)
    else:
        print("They grow up so fast")
school_age_calculator(10, "Samuel")

# =====================================================
# How to get a parameter (value) back from a function
#======================================================
# We want to know what will your age be in 10 years

def add_ten_age(age): # Meaning when someone sends you theit age, the function will add 10 to that age
    new_age =age+10
    return new_age
How_Old_Will_I_Be = add_ten_age(3)
print(How_Old_Will_I_Be)

# ==================
# How to use loops
#==================

#What is a loop? A loop allows you to execute a block of code multiple times. Every sing week my wife comes to me and say ...
#... wisdom "can you take out the trash?" and she asks me that every single week. in this sense it's aloop. Let's create the loop
# There are two types of loop in python:
# - a < for loop >
# - a < while loop >

# a < while loop >
x=0
while(x<5):
    print(x)
    x=x+1
# a < while loop >
for x in range(5,10):
    print(x)
    
# Other things we can do with loops
days = ["Mon","Tues","Wed","Thur", "Fri", "Sat", "Sun"] # We've a variable "days" and array asigned to it.
for d in days:
    print(d)

# Let's apply some logic. Here, we want to know all the days before "Thur"
days = ["Mon","Tues","Wed","Thur", "Fri", "Sat", "Sun"] 
for d in days:
    if(d=="Thur"):break # Stops the listing at wednesday
    print(d)
    
# If we want to continue after Thurs
days = ["Mon","Tues","Wed","Thur", "Fri", "Sat", "Sun"] 
for d in days:
    if(d=="Thur"):continue
    print(d)
    
# All the foundation knowledge we've learn has been building our own code. However we can build on top of what others have done
#..using libraries and modules. There are a lot of fantastic labraries that we can use. Let's say we want to print out the value of <Pi>
#... we can turn out to an existing library called "math".
import math
print("pi is", math.pi)