def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr

test_arrays = [
    [64, 34, 25, 12, 22, 11, 90],
    [5, 2, 8, 1, 9, 3],
    [38, 27, 43, 3, 9, 82, 10]
]

for arr in test_arrays:
    print("Original array:", arr)
    sorted_arr = bubblesort(arr.copy())
    print("Sorted array:", sorted_arr)
    print()
