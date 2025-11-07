def is_subset(arr1, arr2):
    for item in arr1:
        if item not in arr2:
            return False
    return True

array1 = [1, 2, 3]
array2 = [1, 2, 3, 4, 5]

print("Array 1:", array1)
print("Array 2:", array2)
print("Is array1 a subset of array2?", is_subset(array1, array2))
