# What will the following code do and why? 
# Don't run it until you have tried to answer.

# Copy Code


# this code 
x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

# x + 5 is being evaluated first (x is being reassigned and 
# x=10 is not available to it) Normally it's available inside the function
# however because it's being modified we need to specify it as a global variable
# global x