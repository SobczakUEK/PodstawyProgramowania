array = [2, 3, 2, 5, 8, 1, 9, 8]
print("Array:", end=" ")
for num in array:
    print(num, end=" ")
print()

print("Unique elements:", end=" ")
for i in range(len(array)):
    is_unique = True
    for j in range(len(array)):
        if i != j and array[i] == array[j]:
            is_unique = False
            break
    if is_unique:
        print(array[i], end=" ")
print()
