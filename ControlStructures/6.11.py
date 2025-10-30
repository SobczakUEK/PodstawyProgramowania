# Price reduction recommendation
current = float(input('Current product price: '))
previous = float(input('Previous product price: '))
if previous > 0:
    reduction = (previous - current) / previous * 100
else:
    reduction = 0
print(f'Current product price: {current:.2f}')
print(f'Previous product price: {previous:.2f}')
if reduction >= 10:
    print('Buy the product!!')
    print(f'Product price reduced by {int(reduction)}%')
