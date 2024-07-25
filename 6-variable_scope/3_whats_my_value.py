# What will the following code do and why? 
# Don't run it until you have tried to answer.

def my_function():
    global a

    a = 1
    if True:
        print(a)

my_function()

# prints 1, my function is invoked and variable a = 1 is defined
# inside the function, then its evaluated as truthy(True) and 
# print a is executed