# MyArrays.py module
def second_largest(arr):
    if len(arr) < 2:
        return None
    largest = max(arr)
    second = float('-inf')
    for num in arr:
        if num < largest and num > second:
            second = num
    return second

def min_max_diff(arr):
    if not arr:
        return None
    return max(arr) - min(arr)

def median(arr):
    sortedArr = sorted(arr)
    n = len(sortedArr)
    if n % 2 == 0:
        return (sortedArr[n//2-1] + sortedArr[n//2]) / 2
    return sortedArr[n//2]

def min_max_array(arr):
    if not arr:
        return None
    return [min(arr), max(arr)]

def array_to_string(arr):
    return "-".join(map(str, arr))

# Test the functions
numbers = [7,3,8,5,2]
print("Numbers:", ",".join(map(str, numbers)))
print("Second largest number:", second_largest(numbers))
print("Median:", median(numbers))
print("Smallest and largest number:", min_max_array(numbers))
print("Numbers as a string:", array_to_string(numbers))
