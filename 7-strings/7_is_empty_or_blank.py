# Write an is_empty_or_blank function to determine whether 
# a string is either empty or consists entirely of spaces. For example:

# Copy Code

def is_empty_or_blank(my_str):
    return len(my_str.strip()) == 0
        

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True


