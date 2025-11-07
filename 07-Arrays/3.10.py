array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

print("Numbers in first array that don't appear in second array:")
for num in array1:
    if num not in array2:
        print(num, end=" ")
print()
