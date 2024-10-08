from main import *

def main_menu():
    clear_screen()
    print(" ---------------------------------")
    print("| Library Administrator Main Menu |")
    print(" ---------------------------------")
    print("Select a category to configure:")
    print("1. Books")
    print("2. Users")
    print("3. Library")
    print("4. Exit Program")
    while True:
        try:
            selected_option = int(input("Choose 1, 2, 3, or 4: "))
            if selected_option in [1, 2, 3, 4]:
                clear_screen()
                break
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid selection. Please choose a valid option.")
    if selected_option == 1:
        books_menu()
    elif selected_option == 2:
        users_menu()
    elif selected_option == 3:
        library_menu()
    elif selected_option == 4:
        exit()

def books_menu():
    clear_screen()
    print(" ------------")
    print("| Books Menu |")
    print(" ------------")
    print("\033[1mBooks currently available in the library:\033[0m")
    library.list_available_books()
    print()
    print("\033[1mBooks currently borrowed from the library:\033[0m")
    library.list_unavailable_books()
    print()
    print("What would you like to do?")
    print("1. Add a new book to the library")
    print("2. Manually mark a book as borrowed or returned")
    print("3. Return to admin main menu")
    while True:
        try:
            selected_option = int(input("Choose 1, 2, or 3: "))
            clear_screen()
            if selected_option in [1, 2, 3]:
                if selected_option == 1:
                    create_book_menu()
                elif selected_option == 2:
                    borrow_return_menu()
                elif selected_option == 3:
                    main_menu()
                break
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid selection. Please choose a valid option.")

def create_book_menu():
    print("Please enter the details for the book being added: ")
    title = str(input("Title: "))
    author = str(input("Author: "))
    isbn = str(input("ISBN: "))
    new_book = Book(title, author, isbn, True)
    library.add_book(new_book)
    print(new_book.__str__() + " added successfully!")
    input("Press Enter to return to the books menu...")
    books_menu()

def borrow_return_menu():
    print("Would you like to mark a book as borrowed or returned?")
    print("1. Borrowed")
    print("2. Returned")
    list_available_books = []
    for i, book in enumerate(library.books):
        if book.available:
            list_available_books.append(book)
    list_unavailable_books = []
    for i, book in enumerate(library.books):
        if not book.available:
            list_unavailable_books.append(book)
    while True:
        try:
            return_or_borrow = int(input("Choose 1 or 2: "))
            clear_screen()
            if return_or_borrow == 1:
                if len(list_available_books) > 0:
                    print("Please choose the number of the book you would like to mark as borrowed:")
                    for i, book in enumerate(list_available_books):
                        print(str(i + 1) + ". " + book.__str__())
                    book_index = int(input("Choose a book: ")) - 1
                    library.borrow_book(library.users[0], list_available_books[book_index])
                    print("Book borrowed successfully!")
                    input("Press Enter to return to the book testing menu...")
                    books_menu()
                else:
                    print("There are no available books to borrow.")
                    input("Press Enter to return to the book testing menu...")
                    books_menu()
            elif return_or_borrow == 2:
                if len(list_unavailable_books) > 0:
                    clear_screen()
                    print("Please choose the number of the book you would like to mark as returned:")
                    for i, book in enumerate(list_unavailable_books):
                            print(str(i + 1) + ". " + book.__str__())
                    book_index = int(input("Choose a book: ")) - 1
                    library.return_book(library.users[0], list_unavailable_books[book_index])
                    print("Book returned successfully!")
                    input("Press Enter to return to the book testing menu...")
                    books_menu()
                else:
                    print("There are no borrowed books to return.")
                    input("Press Enter to return to the book testing menu...")
                    books_menu()
            else:
                print("Invalid selection. Please choose a valid option.")
            input("Press Enter to return to the book testing menu...")
            books_menu()
        except ValueError:
            print("Invalid selection. Please choose a valid option.")

def users_menu():
    clear_screen()
    print(" ------------")
    print("| Users Menu |")
    print(" ------------")
    print("\033[1mRegistered library members:\033[0m")
    library.list_users()
    print()
    print("What would you like to do?")
    print("1. Test the borrowing functionality (whether the user can borrow available books)")
    print("2. Test the return functionality (whether the user can return books)")
    print("3. View borrowed books")
    print("4. Return to admin main menu")
    while True:
        try:
            selected_option = int(input("Choose 1, 2, 3, or 4: "))
            clear_screen()
            if selected_option in [1, 2, 3, 4]:
                if selected_option == 1:
                    user_borrow_book()
                elif selected_option == 2:
                    user_return_book()
                elif selected_option == 3:
                    view_borrowed_books()
                elif selected_option == 4:
                    main_menu()
                break
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid selection. Please choose a valid option.")

def user_borrow_book():
    print("Please choose the number of the user you would like to test borrowing functionality for:")
    available_book_count = library.available_books_count()
    while available_book_count > 0:
        try:
            for i, user in enumerate(library.users):
                print(str(i + 1) + ". " + user.name)
            user_index = int(input("Choose a user: ")) - 1
            if user_index in range(len(library.users)):
                user_borrow_book_screen_2(user_index)
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid selection. Please choose a valid option.")
    clear_screen()
    print("There are no available books to borrow.")
    input("Press Enter to return to the users menu...")
    users_menu()

def user_borrow_book_screen_2(user_index):
    clear_screen()
    print("Now select one of the following available books for the user to borrow:")
    available_books = []
    while True:
        try:
            for i, book in enumerate(library.books):
                if book.available:
                    available_books.append(book)
            for i, book in enumerate(available_books):
                print(str(i + 1) + ". " + book.__str__())
            book_index = int(input("Choose a book: ")) - 1
            if book_index in range(len(available_books)):
                clear_screen()
                library.users[user_index].borrow_book(available_books[book_index])
                users_menu()
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid selection. Please choose a valid option.")

def user_return_book():
    print("Please choose the number of the user you would like to test returning functionality for:")
    list_users_with_borrowed_books = []
    for i, user in enumerate(library.users):
        if len(user.borrowed_books) > 0:
            list_users_with_borrowed_books.append(user)
    unavailable_book_count = library.unavailable_books_count()
    while unavailable_book_count > 0:
        try:
            for i, user in enumerate(list_users_with_borrowed_books):
                print(str(i + 1) + ". " + user.name)
            user_index = int(input("Choose a user: ")) - 1
            if user_index in range(len(list_users_with_borrowed_books)):
                user_return_book_screen_2(list_users_with_borrowed_books, user_index)
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid selection. Please choose a valid option.")
    clear_screen()
    print("There are no available books to return.")
    input("Press Enter to return to the users menu...")
    users_menu()

def user_return_book_screen_2(list_users_with_borrowed_books, user_index):
    clear_screen()
    print("Now select one of the following borrowed books for the user to return:")
    while True:
        try:
            for i, book in enumerate(list_users_with_borrowed_books[user_index].borrowed_books):
                print(str(i + 1) + ". " + book.__str__())
            book_index = int(input("Choose a book: ")) - 1
            if book_index in range(len(list_users_with_borrowed_books[user_index].borrowed_books)):
                clear_screen()
                list_users_with_borrowed_books[user_index].return_book(list_users_with_borrowed_books[user_index].borrowed_books[book_index])
                users_menu()
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid selection. Please choose a valid option.")

def view_borrowed_books():
    list_users_with_borrowed_books = []
    for i, user in enumerate(library.users):
        if len(user.borrowed_books) > 0:
            list_users_with_borrowed_books.append(user)
    if len(list_users_with_borrowed_books) > 0:
        library.view_all_borrowed_books()
        input("Press Enter to return to the users menu...")
        users_menu()
    else:
        clear_screen()
        print("There are currently no users with borrowed books.")
        input("Press Enter to return to the users menu...")
        users_menu()

def library_menu():
    clear_screen()
    print(" --------------")
    print("| Library Menu |")
    print(" --------------")
    print("What would you like to do?")
    print("1. Test adding and removing books from the library")
    print("2. Test adding and removing users")
    print("3. Test the borrow and return processes to ensure the logic works between Library, User, and Book")
    print("4. Return to admin main menu")
    while True:
        try:
            selected_option = int(input("Choose 1, 2, 3, or 4: "))
            clear_screen()
            if selected_option in [1, 2, 3, 4]:
                if selected_option == 1:
                    add_remove_books()
                elif selected_option == 2:
                    add_remove_users()
                elif selected_option == 3:
                    main_menu()
                elif selected_option == 4:
                    main_menu()
                break
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid selection. Please choose a valid option.")

def add_remove_users():
    print("Would you like to add or remove a user?")
    print("1. Add")
    print("2. Remove")
    while True:
        try:
            add_or_remove = int(input("Choose 1 or 2: "))
            clear_screen()
            if add_or_remove == 1:
                add_user_menu()
            elif add_or_remove == 2:
                remove_user_menu()
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid selection. Please choose a valid option.")

def add_user_menu():
    print("Please enter the details for the user being added: ")
    name = str(input("Name: "))
    id = int(input("ID: "))
    new_user = User(name, id, [])
    library.add_user(new_user)
    print(new_user.name + " added successfully!")
    input("Press Enter to return to the library testing menu...")
    library_menu()

def remove_user_menu():
    if len(library.users) > 0:
        clear_screen()
        print("Please choose the number of the user you would like to remove:")
        for i, user in enumerate(library.users):
                print(str(i + 1) + ". " + user.name)
        user_index = int(input("Choose a user: ")) - 1
        library.remove_user(library.users[user_index])
        print("User removed successfully!")
        input("Press Enter to return to the library testing menu...")
        library_menu()
    else:
        print("There are no more users in the system.")
        input("Press Enter to return to the library testing menu...")
        library_menu()

def add_remove_books():
    print("Would you like to add or remove a book?")
    print("1. Add")
    print("2. Remove")
    while True:
        try:
            add_or_remove = int(input("Choose 1 or 2: "))
            clear_screen()
            if add_or_remove == 1:
                add_books_menu()
            elif add_or_remove == 2:
                remove_books_menu()
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid selection. Please choose a valid option.")

def add_books_menu():
    print("Please enter the details for the book being added: ")
    title = str(input("Title: "))
    author = str(input("Author: "))
    isbn = str(input("ISBN: "))
    new_book = Book(title, author, isbn, True)
    library.add_book(new_book)
    print(new_book.title + " added successfully!")
    input("Press Enter to return to the library testing menu...")
    library_menu()

def remove_books_menu():
    if len(library.books) > 0:
        clear_screen()
        print("Please choose the number of the book you would like to remove:")
        for i, book in enumerate(library.books):
                print(str(i + 1) + ". " + book.title)
        book_index = int(input("Choose a book: ")) - 1
        library.remove_book(library.books[book_index])
        print("Book removed successfully!")
        input("Press Enter to return to the library testing menu...")
        library_menu()
    else:
        print("There are no more books in the system.")
        input("Press Enter to return to the library testing menu...")
        library_menu()


main_menu()
