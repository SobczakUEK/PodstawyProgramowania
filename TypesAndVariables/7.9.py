import random as r

dice = r.randint(1,6)
print(f'Dice rolled: {dice}')
print(f'Special number (1 or 6): {dice == 1 or dice == 6}')
