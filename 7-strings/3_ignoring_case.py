# Using the following code, compare the value of name with 
# the string 'RoGeR' while ignoring the case of both strings. 
# Print true if the values are the same; print false if they aren't. 
# Next, perform a case-insensitive comparison between the value of 
# name and the string 'DAVE'.

name = 'Roger'

if name.casefold() == 'RoGeR'.casefold():
  print('true')
elif name.casefold() == 'DAVE'.casefold():
  print('false')
