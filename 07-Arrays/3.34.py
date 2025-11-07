def identity_matrix(n):
    matrix = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        matrix[i][i] = 1
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()

print("3x3 Identity Matrix:")
print_matrix(identity_matrix(3))
print("5x5 Identity Matrix:")
print_matrix(identity_matrix(5))
print("8x8 Identity Matrix:")
print_matrix(identity_matrix(8))
