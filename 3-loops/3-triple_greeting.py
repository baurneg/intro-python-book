# Write a loop that prints the value of the greeting variable three times.

# Copy Code
# greeting = 'Aloha!'
count = 1
while count <= 3:
  print("Aloha!")
  count += 1

print('Another way: ')

for _ in range(3):
  print('Aloha!')

# _ is a common convention when no variable is used