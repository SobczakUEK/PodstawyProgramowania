arr = [7,9,2,4,5,6]
print("Original array:", arr)

# Separate even and odd numbers
even = []
odd = []
for num in arr:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

# Combine even and odd numbers
arr = even + odd
print("Rearranged array:", arr)
