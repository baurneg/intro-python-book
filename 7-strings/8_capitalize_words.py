# Write code that capitalizes the words in the string 
# 'launch school tech & talk', so that you get the string 
# 'Launch School Tech & Talk'.

string = 'launch school tech & talk'
str_list = string.split(' ')
print(str_list)
index = 0
cap_words = []
while index <= len(str_list) - 1:
  new_string = str_list[index].capitalize()
  cap_words.append(new_string)
  index += 1
new_string =' '.join(cap_words)
print(new_string)


# def capitalize_words(string):
#     return string.title()

# string = 'launch school tech & talk'
# result = capitalize_words(string)
# print(result)  # Launch School Tech & Talk

# title method capitalizes every word in the string