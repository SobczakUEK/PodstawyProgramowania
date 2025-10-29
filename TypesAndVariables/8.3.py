###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# Register user's input in 'c' variable, representing temperature in degrees Celsius.
c = int(input('Enter temperature in degrees Celsius: '))
# Calculate temperature in degrees Fahrenheit using the formula F = (C * 9/5) + 32.
f = (c * 9/5) + 32
# Print the temperature in degrees Fahrenheit.
print(f'Temperature in degrees Fahrenheit: {f}')