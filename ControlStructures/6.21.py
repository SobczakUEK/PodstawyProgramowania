# Coin change with 5,2,1 PLN coins
amount = int(input('Enter the amount in PLN: '))
coins5 = amount // 5
amount = amount % 5
coins2 = amount // 2
amount = amount % 2
coins1 = amount
print('The amount of PLN in coins:')
print(f'5 PLN coins: {coins5}')
print(f'2 PLN coins: {coins2}')
print(f'1 PLN coins: {coins1}')
