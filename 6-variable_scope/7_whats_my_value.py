# What will the following code do and why? 
# Don't run it until you have tried to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)


# the code prints 2
# function is defined with a global variable assigned to the value of 2 inside 
# since the global variable is called inside the function it changes the a
# variable defined outside of function, and not only local a inside the function