# The destinations list contains a list of travel destinations.

# Copy Code
destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']
# Write a function that, without using the built-in in operator, 
# checks whether a specific destination is included within destinations. 
# For example: When checking whether 'Barcelona' is contained in 
# destinations, the expected output is True, whereas the expected 
# output for 'Nashville' is False.

# Copy Code
# contains('Barcelona', destinations)  # True
# contains('Nashville', destinations)  # False

def contains(city, destinations):
  if city in destinations:
    return True
  else: 
    return False
print(contains('Barcelona', destinations))
print(contains('Nashville', destinations))
print(contains('New York City', destinations))

# True
# False
# True
