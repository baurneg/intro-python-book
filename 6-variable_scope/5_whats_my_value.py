# What will the following code do and why? 
# Don't run it until you have tried to answer.

# Copy Code
a = 1

def my_function():
    print(a)
    a = 2

my_function()


# it raises an error because it finds that a is reassigned inside the function
# however it's been defined after the print(a) is executed
# to print(a) a needs to be defined before print is called. 
