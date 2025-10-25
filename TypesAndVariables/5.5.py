price = input("Enter price: ").replace(",", ".")
if "." not in price:
    price = int(price)
else:
    price = float(price)

discount = int(input("Enter discount: "))

reduction = round((price * discount)/100, 2)
after_discount = round(price - reduction, 2)

print(f'Price with discount: {after_discount}')
print(f'Reduction: {reduction}')