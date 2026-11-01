balance = 5000

print("1. Check Balance")
print("2. Withdraw Money")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Available Balance:", balance)

elif choice == 2:
    amount = int(input("Enter withdrawal amount: "))

    if amount > 0 and amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance or Invalid Amount")

else:
    print("Invalid Choice")
