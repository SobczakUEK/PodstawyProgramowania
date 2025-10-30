###
# Simple ATM with PIN check and change PIN (very basic)
#
balance = 1000.0
pin = '1111'

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        entered = input("Enter PIN to check: ")
        if entered == pin:
            print("PIN is correct.")
        else:
            print("PIN incorrect.")
    elif choice == '5':
        entered = input("Enter current PIN: ")
        if entered == pin:
            new_pin = input("Enter new 4-digit PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                pin = new_pin
                print("PIN changed.")
            else:
                print("Invalid PIN format. PIN must be exactly 4 digits.")
        else:
            print("Current PIN incorrect.")
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")
