# What will the following code do and why? 
# Don't run it until you have tried to answer.

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# since the lists are mutable and b variable is accessible outside of 
# the defined function, b[0] mutates b at index 0. 
# the output then is [10, 2, 3]