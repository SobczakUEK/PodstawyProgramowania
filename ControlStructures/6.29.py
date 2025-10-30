# Print first N prime numbers
N = int(input('Enter N: '))
found = 0
num = 2
primes = []
while found < N:
    is_prime = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        primes.append(str(num))
        found += 1
    num += 1
print('Prime numbers:', ' '.join(primes))
