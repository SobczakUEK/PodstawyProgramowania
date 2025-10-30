# Decimal to binary converter
n = int(input('Enter decimal number: '))
if n == 0:
    print('0(10) = 0(2)')
else:
    original = n
    bits = ''
    while n > 0:
        bits = str(n % 2) + bits
        n = n // 2
    print(f'{original}(10) = {bits}(2)')
