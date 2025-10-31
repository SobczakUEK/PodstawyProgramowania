# Lottery coupon 1..49 layout
for row in range(7):
    line = []
    for col in range(7):
        num = 1 + col*7 + row
        line.append(str(num))
    print(' '.join(line))
