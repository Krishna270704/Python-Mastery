def Add_note():
    note = input("Enter your note:")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")

def View_notes():
    with open("notes.txt", "r") as file:
        print(file.read())

def Exit():
    print("Thank you for using the Student Notes Manager!")
    exit()

print("===================STUDENT NOTES MANAGER==================\n")
print("1. Add Note")
print("2. View Notes")
print("3. Exit")

while True:
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        Add_note()
    elif choice == "2":
        View_notes()
    elif choice == "3":
        Exit()
    else:
        print("Invalid choice. Please try again.")