from Range import isInRange

number = int(input("A number: "))
result = isInRange(number, 2, 15)
print(f"Number {number} in the range <2,15>: {'yes' if result else 'no'}")
