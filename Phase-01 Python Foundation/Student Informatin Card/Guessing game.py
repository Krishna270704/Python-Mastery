print("===================Guessing Game==================\n")
Guess = int(input("Guess a number (1-10):"))
Attempts = 0
while Guess > 0 or Guess < 10:
    print("Invalid input. Please guess a number between 1 and 10.")
    Guess = int(input("Guess a number (1-10):"))
    Attempts += 1
    if Guess == 7:
        print("Congratulations! You guessed the correct number.")
        print("Total attempts:", Attempts)
        break
    