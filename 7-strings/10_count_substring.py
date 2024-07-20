# Write a function that counts the number of occurrences of a substring in a string.

# Copy Code
# print(count_substrings("lemon lemon lemon", "lemon")) # 3
# print(count_substrings("laLAlaLA", "la")) # 2
# print(count_substrings("launch", "uno")) # 0

def count_substrings(my_str, substring):
  return my_str.count(substring)
  
    



print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA ds", "la")) # 2
print(count_substrings("launch", "uno")) # 0
