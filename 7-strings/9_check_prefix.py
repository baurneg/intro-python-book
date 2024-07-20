# Write a function that checks whether a string starts 
# with a specific prefix.

# ExamplesCopy Code
# print(starts_with("launch", "la"))   # True
# print(starts_with("school", "sah"))  # False
# print(starts_with("school", "sch"))  # True

def starts_with(string, substring):
  return string.startswith(substring)
print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True