# We wanted to create a matrix 3x3 so we could use it to build a Tic-Tac-Toe game.
# However, we encountered an issue, as whenever we change a value in one nested 
# list, all nested lists are affected. Can you fix the code?

# Copy Code
sub_list = ["-", "-", "-"]
matrix = []

for element in range(3):
    matrix.append(sub_list.copy())
print(matrix)
print()
print()
print()
matrix[0][0] = "X"
print(matrix)

