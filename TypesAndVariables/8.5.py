###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = input('SWIFT code: ')
print(f'Bank Code: {swift[0:4]}')
print('Country Code: ' + swift[4:6])
