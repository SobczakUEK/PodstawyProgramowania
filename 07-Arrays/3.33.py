array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Before swap:")
for row in array:
    print(row)

# Swap first and last columns
for i in range(len(array)):
    tmp = array[i][0]
    array[i][0] = array[i][-1]
    array[i][-1] = tmp

print("After swap:")
for row in array:
    print(row)
