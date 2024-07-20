# Magdalena has just adopted a new pet! She wants to add her new dog, Bowser, 
# to the pets dictionary. After doing so, she realizes that her dogs Sparky 
# and Fido have been mistakenly removed. Help Magdalena fix her code so that 
# all three of her dogs' names will be associated with the key 'dog' in the 
# pets dictionary.

# Copy Code
pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

dogs = pets['dog'] + ['bowser']
pets['dog'] = dogs

print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}