# What will the following code do and why? 
# Don't run it until you have tried to answer.

a = 1

def my_function():
    a = 2

(my_function())
print(a)

# the code prints 1
# function is defined with a variable assigned to the value of 2 inside 
# the function however it does not return or print any value when called
# print a only prints a = 1 global variable