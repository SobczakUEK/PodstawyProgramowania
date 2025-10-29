###
# A program to print numerical representations of characters.
#

charArr = ['a', 'b', 'z', 'A', 'B', 'Z', '1', '=', '+', '€']

for char in charArr:
    print(f'{char}: {ord(char)}')