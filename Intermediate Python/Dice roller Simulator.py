import random


def roll():
    return random.randint(1, 6)


while True:

    print("\n====== DICE ROLLER ======")
    print("1. Roll Dice")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("🎲 You rolled:", roll())

        again = input("Roll again? (y/n): ").lower()

        while again == "y":
            print("🎲 You rolled:", roll())
            again = input("Roll again? (y/n): ").lower()

    elif choice == "2":
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")