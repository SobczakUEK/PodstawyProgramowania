def f(n):
    return '*' + ("/*" * (n-1)) if n > 0 else ''

print(f(4))
print(f(1))