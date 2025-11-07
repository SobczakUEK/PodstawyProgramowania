def create_2d_arr(x, y):
    return [[0 for j in range(y)] for i in range(x)]

array = create_2d_arr(3, 5)
for row in array:
    for num in row:
        print(num, end=" ")
    print()
