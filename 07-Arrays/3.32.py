array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Before swap:")
for row in array:
    print(row)

tmp = array[0]
array[0] = array[-1]
array[-1] = tmp

print("After swap:")
for row in array:
    print(row)
