print("===================SAFE CALCULATOR==================\n")

while True:
    try:
        # Take input
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        operator = input("Enter Operator (+, -, *, /): ")

        # Perform calculation
        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            result = num1 / num2   # May raise ZeroDivisionError

        else:
            print("❌ Invalid Operator!")
            continue

    except ValueError:
        print("❌ Invalid Input! Please enter numbers only.")
        continue

    except ZeroDivisionError:
        print("❌ Cannot divide by zero.")
        continue

    else:
        print(f"✅ Result = {result}")

    finally:
        print("----------------------------")

    # Ask user if they want to continue
    choice = input("Do you want to calculate again? (y/n): ").lower()

    if choice != "y":
        print("👋 Thank you for using Safe Calculator!")
        break