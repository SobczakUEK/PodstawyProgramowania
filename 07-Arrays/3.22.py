import random

def rand_elem(array):
    return random.choice(array)

testArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Array:", testArr)
print("Random elements:")
for _ in range(5):  # Print 5 random elements
    print(rand_elem(testArr), end=" ")
print()
