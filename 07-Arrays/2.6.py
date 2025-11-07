                            
matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# Replace diagonal elements with 1
for i in range(len(matrix)):
    matrix[i][i] = 1

# Print the matrix
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
