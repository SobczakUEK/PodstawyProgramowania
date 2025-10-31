# First twenty Fibonacci numbers
a = 0
b = 1
count = 0
while count < 20:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
