# Point quadrant checker
x = float(input('x = '))
y = float(input('y = '))
if x == 0 and y == 0:
    print(f'Point P({x},{y}) is at the origin')
elif x == 0:
    print(f'Point P({x},{y}) is on the Y axis')
elif y == 0:
    print(f'Point P({x},{y}) is on the X axis')
elif x > 0 and y > 0:
    print(f'Point P({x},{y}) is in the first quadrant of the coordinate system')
elif x < 0 and y > 0:
    print('Point is in the second quadrant')
elif x < 0 and y < 0:
    print('Point is in the third quadrant')
else:
    print('Point is in the fourth quadrant')
