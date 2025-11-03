def f(detector):
    count = 0
    max_count = 0
    for action in detector:
        if action == '+':
            count += 1
            if count > max_count:
                max_count = count
        else:
            count -= 1
    return max_count >= 3

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))