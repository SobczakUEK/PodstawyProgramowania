###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#

a = input("Input phone number:")
print(f'{a[0:3]}-{a[3:6]}-{a[6:9]}')
