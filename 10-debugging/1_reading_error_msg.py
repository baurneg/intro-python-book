# You come across the following code. What errors does it raise for the given 
# examples and what exactly do the error messages mean?

# Copy Code
def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)
#TypeError: find_first_nonzero_among() takes 1 positional argument but 6 were given
# 1 list is expected to go with for loop but 6 arguments given

find_first_nonzero_among(1) # integer is not iterable error


