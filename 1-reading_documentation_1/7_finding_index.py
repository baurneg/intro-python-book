# Python lists come with a variety of built-in methods that 
# allow for common list manipulations. One such operation 
# is determining the index of an item in the list.

# Given a list:

# Copy Code
# fruits = ["apple", "banana", "cherry", "peach", "watermelon"]
# How would you determine the index of the fruit "cherry" in 
# this list?

# s.index(x[, i[, j]])

# index of the first occurrence of x in s (at or after index i 
# and before index j)

# index raises ValueError when x is not found in s. Not all 
# implementations support passing the additional arguments i and j. 
# These arguments allow efficient searching of subsections of the 
# sequence. Passing the extra arguments is roughly equivalent to 
# using s[i:j].index(x), only without copying any data and with 
# the returned index being relative to the start of the sequence 
# rather than the start of the slice.

fruits = ["apple", "banana", "cherry", "peach", "watermelon"]
print(fruits[2:5].index('cherry')) # 0