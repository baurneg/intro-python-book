# What will the following code do and why? Don't run it until 
# you have tried to answer.

# if True:
#     my_value = 20

# print(my_value)

# variable initialized inside the if block are accessible outside
# of that block

if True:
    my_value = 20

print(my_value)

#this code will raise an Error, my_new value is not defined since there 
# is no falsy condition to execute if False block. Thus my_new_value remains
# undefined.

if False:
    my_new_value = 42

print(my_new_value)