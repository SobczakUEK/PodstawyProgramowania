def f(productCode):
    if len(productCode) != 4:
        return False
    
    firstThree = productCode[:3]
    control = int(productCode[3])
    
    digitSum = sum(int(d) for d in firstThree)
    
    return digitSum % 7 == control

print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))
