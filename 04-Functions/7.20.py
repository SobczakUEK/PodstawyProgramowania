import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def f(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num


print(f(1))
print(f(5))
print(f(5000))