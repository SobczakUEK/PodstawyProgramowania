# A tree may be cut down if its diameter is at least 50 cm. Write a program that
# based on the circumference of the tree entered from the keyboard, calculates and prints
# the value True if the tree can be cut down, or print the value False otherwise.

cc = input("Enter tree circumference in cm: ")
cd = round(int(cc)/3.14, 2)

print(f"Tree can be cut down: {cd >= 50}")