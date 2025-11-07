array = [[0 for j in range(5)] for i in range(5)]

for i in range(5):
    for j in range(5):
        array[i][j] = (i + 1) * (j + 1)

for row in array:
    for num in row:
        print(f"{num:2d}", end=" ")
    print()
