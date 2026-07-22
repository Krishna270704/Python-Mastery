print("===================LIBRARY MANAGEMENT SYSTEM==================\n")
Book = []
def add_book():
    book = input("Enter book name:")
    Book.append(book)
    print("Book added successfully")

def display_books():
    print("\nBooks Available:")
    for book in Book:
        print(book)

def search_book():
    book = input(" Enter book name")
    if book in Book:
        print("Book found")
    else:
        print("Book not found")

def remove_book():
    book = input("Enter book name:")
    if book in Book:
        Book.remove(book)
        print("Book removed successfully")
    else:
        print("Book not found")

def count_books():
    print("Total books:", len(Book))

while True:

    print("========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display Books")
    print("5. Total Books")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        remove_book()

    elif choice == "3":
        search_book()

    elif choice == "4":
        display_books()

    elif choice == "5":
        total_books()

    elif choice == "6":
        print("👋 Thank You for Using Library Management System!")
        break

    else:
        print("❌ Invalid Choice! Please Try Again.\n")    