# Credit card payment
account_balance = 500
try:
    total_payment = float(input('Enter total payment: '))
except ValueError:
    print('Invalid amount')
else:
    if total_payment <= account_balance:
        print('Payment completed')
    else:
        print('No funds')
