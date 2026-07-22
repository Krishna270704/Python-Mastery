print("===================ATM MACHINE==================\n")

Balance = int(input("Enter your balance:"))
Withdrawal = int(input("Enter withdrawal amount:"))

if Withdrawal > 0 and Withdrawal <= Balance:
    print("Transaction successful")

    print("Remaining balance:", Balance - Withdrawal)

else:
    print("Insufficient balance")
