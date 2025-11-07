def occurs(number, array):
    for num in array:
        if num == number:
            return True
    return False

array = [15, 38, 7, 23, 14]
number = int(input("Number: "))

print("Array:", end=" ")
for num in array:
    print(num, end=" ")
print()

if occurs(number, array):
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} does not appear in the array")
