# Given the following variables:

# Copy Code
# name = "Victor"
# profession = "programmer"
# How can you print the string < Hello, Victor. You are a programmer.> 
# using the str.format method? You should fill in the name and profession 
# in a string literal that contains the rest of the text.
# How can you achieve the same result using an f-string?
# Refer to the Python documentation on Format String Syntax and Formatted 
# string literals for guidance.

name = "Victor"
profession = "programmer"
message_format = "Hello, {}. You are a {}."
formatted_message = message_format.format(name, profession)
print(formatted_message)