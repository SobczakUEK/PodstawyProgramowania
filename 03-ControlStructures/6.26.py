# PIN code with up to three attempts
correct = '0805'
attempts = 0
while attempts < 3:
    pin = input('Enter the PIN code: ')
    if pin == correct:
        print('Correct')
        break
    else:
        print('Incorrect...')
    attempts += 1
if attempts == 3 and pin != correct:
    print('Sorry, your payment card has been blocked.')
