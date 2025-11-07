numbers = [3.14, 2.5, 9.7, 1.8, 4.2, 6.1]
threshold = float(input("Enter a value: "))

count = 0
for num in numbers:
    if num > threshold:
        count += 1

print(f"Number of elements greater than {threshold}: {count}")
