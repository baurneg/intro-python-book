#Write a function that checks whether a string starts with a specific prefix.

#ExamplesCopy Code

def starts_with(my_str, substring):
    return my_str.startswith(substring)



print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True