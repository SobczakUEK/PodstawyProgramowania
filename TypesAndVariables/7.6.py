# The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. 
# Write a program that checks whether the vehicle speed entered from the keyboard is correct.

v = int(input("Enter vehicle speed: "))
print(f'Speed is valid: {v>40 and v<140}')