def f(number):
    digits = str(number)
    total = 0
    for digit in set(digits):
        count = digits.count(digit)
        if count > 1:
            total += int(digit) * count
    return total

print(f(1027))
print(f(230335))
print(f(513553007))