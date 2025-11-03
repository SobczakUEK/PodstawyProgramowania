def f(expression):
    total = 0
    currentNum = ''
    operation = '+'
    
    for char in expression:
        if char.isdigit():
            currentNum = char
        elif char in '+-':
            if operation == '+':
                total += int(currentNum)
            else:
                total -= int(currentNum)
            operation = char
            
    if operation == '+':
        total += int(currentNum)
    else:
        total -= int(currentNum)
        
    return total


print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))
