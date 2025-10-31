# Print 1 to 30 with THREE/FIVE/BINGO
for i in range(1,31):
    out = ''
    if i % 3 == 0 and i % 5 == 0:
        out = 'BINGO'
    elif i % 3 == 0:
        out = 'THREE'
    elif i % 5 == 0:
        out = 'FIVE'
    else:
        out = str(i)
    print(out)
