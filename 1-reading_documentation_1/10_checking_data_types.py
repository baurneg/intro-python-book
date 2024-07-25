
# Referring to the official Python documentation, how would you identify 
# the data type of the following values?

# Copy Code
# 23.5
# 'Call me Ishmael.'
# False
# 0
# None


# The type() function returns an object’s type (which is an object itself). 
# Like its identity, an object’s type is also unchangeable.


print(type(23.5)) # <class 'float'>
print(type('Call me Ishmael.')) # <class 'str'>
print(type(False)) # <class 'bool'>
print(type(0)) # <class 'int'>
print(type(None)) # <class 'Nonetype'>