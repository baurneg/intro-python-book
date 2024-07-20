# We have a grocery list. As we check off items on that list, 
# we want to remove them from the list.

# Write code that removes the items from grocery_list,
# one by one, until it is empty. If you print the elements 
# you remove, the expected behavior would look as follows.

# Copy Code
grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa', 'carrots', 'broccoli', 'hummus']

# Your code.

for item in grocery_list:
  print(item)
grocery_list.clear()
print(grocery_list)