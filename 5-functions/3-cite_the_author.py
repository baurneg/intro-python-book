# Let's generalize the function from the previous exercise.
# Implement a function named cite that takes two string 
# arguments: the author of the quote and what they said. 
# It then prints the quote, as shown below.

# Copy Code
# cite('Bruce Eckel', 'Python is executable pseudocode.')
# # Bruce Eckel said: "Python is executable pseudocode."


def cite(str1, str2):
  print(f'{str1} said: "{str2}".')
cite('Bruce Eckel', 'Python is executable pseudocode')