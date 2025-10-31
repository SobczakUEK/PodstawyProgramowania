# Simple survey of three yes-no questions
print('SURVEY')
a = input('Are you interested in computer science? (y/n): ')
b = input('Do you like playing computer games? (y/n): ')
c = input('Do you have an Instagram account? (y/n): ')

print('\nSURVEY RESULTS')
print(f'Interested in computer science: {"Yes" if a=="y" else "No"}')
print(f'Playing computer games: {"Yes" if b=="y" else "No"}')
print(f'Has an Instagram account: {"Yes" if c=="y" else "No"}')
