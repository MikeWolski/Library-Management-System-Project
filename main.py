import os

# Define a function to clear the screen
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

# Define a class called Book which represents a book in the library.
class Book:
    def __init__(self, title, author, isbn, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
    # A string representation of the book object is returned.
    def __str__(self):
        return (self.title + " by " + self.author + " (ISBN: " + self.isbn + ")")
    # The borrow_book method is defined to mark the books as unavailable as they are borrowed.
    def borrow_book(self):
        if self.available:
            self.available = False
            return True
        else:
            return False
    # If the book is not available, then it is able to be returned.
    def return_book(self):
        if not self.available:
            self.available = True
            return True
        else:
            return False

# Define a class called User which represents a user of the library.
class User:
    def __init__(self, name, user_id, borrowed_books):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = borrowed_books
    # A string representation of the user object is returned.
    def __str__(self):
        return (str(self.user_id) + ": " + self.name + " has borrowed " + str(len(self.borrowed_books)) + " books.")
    # The borrowed_book method is defined to allow the user to borrow a book (if available).
    def borrow_book(self, book):
        if book.borrow_book():
            self.borrowed_books.append(book)
            return True
        else:
            return False
    # The return_book method is defined to allow the user to return a borrowed book.
    def return_book(self, book):
        if book.return_book():
            self.borrowed_books.remove(book)
            return True
        else:
            return False
    # The view_borrowed_books method is defined to show all books currently borrowed by the user.
    def view_borrowed_books(self):
        for book in self.borrowed_books:
            print(book)

# Define a class called Library which represents a library, managing books and users.
class Library:
    def __init__(self, books, users):
        self.books = books
        self.users = users
    # The add_book method is defined to add a book to the library.
    def add_book(self, book):
        self.books.append(book)
    # The remove_book method is defined to remove a book from the library.
    def remove_book(self, book):
        self.books.remove(book)
    # The add_user method is defined to add a user to the library.
    def add_user(self, user):
        self.users.append(user)
    # The remove_user method is defined to remove a user from the library.
    def remove_user(self, user):
        self.users.remove(user)
    # The borrow_book method is defined to facilitate borrowing by interacting with User and Book classes.
    def borrow_book(self, user, book):
        return user.borrow_book(book)
    # The return_book method is defined to facilitate returning by interacting with User and Book classes.
    def return_book(self, user, book):
        return user.return_book(book)
    # The list_available_books method is defined to show all books currently available.
    def list_available_books(self):
        for book in self.books:
            if book.available:
                print(book)
    # The list_unavailable_books method is defined to show all books currently borrowed.
    def list_unavailable_books(self):
        for book in self.books:
            if not book.available:
                print(book)
    # The list_users method is defined to show all users currently registered in the library and their borrowed books.
    def list_users(self):
        for user in self.users:
            print(user)

# Create a list of books to be added to the library.
books = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", True),
    Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", True),
    Book("1984", "George Orwell", "9780451524935", True),
    Book("Pride and Prejudice", "Jane Austen", "9780141439518", True),
    Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488", True)
]
# Create a list of users to be added to the library.
users = [
    User("Alice", 1, []),
    User("Bob", 2, []),
    User("Charlie", 3, [])
]
# Create a library object with the books and users lists.
library = Library(books, users)


clear_screen()
print("Welcome to the library!")
input("Press Enter for Admin Panel...")

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
    while True:
        try:
            return_or_borrow = int(input("Choose 1 or 2: "))
            clear_screen()
            if return_or_borrow == 1:
                print("Please choose the number of the book you would like to mark as borrowed:")
                for i, book in enumerate(library.books):
                    if book.available:
                        print(str(i + 1) + ". " + book.__str__())
                book_index = int(input("Choose a book: ")) - 1
                if library.borrow_book(library.users[0], library.books[book_index]):
                    print("Book borrowed successfully!")
                else:
                    print("Book could not be borrowed.")
            elif return_or_borrow == 2:
                clear_screen()
                print("Please choose the number of the book you would like to mark as returned:")
                for i, book in enumerate(library.books):
                    if not book.available:
                        print(str(i + 1) + ". " + book.__str__())
                book_index = int(input("Choose a book: ")) - 1
                if library.return_book(library.users[0], library.books[book_index]):
                    print("Book returned successfully!")
                else:
                    print("Book could not be returned.")
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
                    main_menu()
                elif selected_option == 2:
                    main_menu()
                elif selected_option == 3:
                    view_borrowed_books()
                elif selected_option == 4:
                    main_menu()
                break
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid selection. Please choose a valid option.")

def view_borrowed_books():
    print("Please choose the number of the user you would like to view borrowed books for:")
    for i, user in enumerate(library.users):
        print(str(i + 1) + ". " + user.name)
    user_index = int(input("Choose a user: ")) - 1
    clear_screen()
    print("Books borrowed by " + library.users[user_index].name + ":")
    library.users[user_index].view_borrowed_books()
    input("Press Enter to return to the users menu...")
    users_menu()

def library_menu():
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
                    main_menu()
                elif selected_option == 2:
                    main_menu()
                elif selected_option == 3:
                    main_menu()
                elif selected_option == 4:
                    main_menu()
                break
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid selection. Please choose a valid option.")

main_menu()
