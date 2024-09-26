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
input("How can we help you today? Press Enter for Test Mode...")

def test_main_menu():
    clear_screen()
    print(" -----------------------------")
    print("| Library Test Mode Main Menu |")
    print(" -----------------------------")
    print("Which class would you like to test:")
    print("1. Book")
    print("2. User")
    print("3. Library")
    print("4. Exit")
    while True:
        try:
            selected_class_for_testing = int(input("Choose 1, 2, 3, or 4: "))
            if selected_class_for_testing in [1, 2, 3, 4]:
                clear_screen()
                break
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid selection. Please choose a valid option.")
    if selected_class_for_testing == 1:
        book_testing_menu()
    elif selected_class_for_testing == 2:
        user_testing_menu()
    elif selected_class_for_testing == 3:
        library_testing_menu()
    elif selected_class_for_testing == 4:
        exit()

def book_testing_menu():
    clear_screen()
    print(" --------------")
    print("| Book Testing |")
    print(" --------------")
    print("\033[1mBooks currently available in the library:\033[0m")
    library.list_available_books()
    print()
    print("\033[1mBooks currently borrowed from the library:\033[0m")
    library.list_unavailable_books()
    print()
    print("Which method of the Book class would you like to test:")
    print("1. Test the creation of a book object")
    print("2. Test borrow and return functionality (whether the availability status changes)")
    print("3. Return to Test Mode main menu")
    while True:
        try:
            selected_class_for_testing = int(input("Choose 1, 2, or 3: "))
            clear_screen()
            if selected_class_for_testing in [1, 2, 3]:
                if selected_class_for_testing == 1:
                    create_book_menu()
                elif selected_class_for_testing == 2:
                    borrow_return_menu()
                elif selected_class_for_testing == 3:
                    test_main_menu()
                break
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid selection. Please choose a valid option.")

def create_book_menu():
    print("Please enter the details for the book object to be created: ")
    title = str(input("Title: "))
    author = str(input("Author: "))
    isbn = str(input("ISBN: "))
    new_book = Book(title, author, isbn, True)
    library.add_book(new_book)
    print(new_book.__str__() + " created successfully!")
    input("Press Enter to return to the book testing menu...")
    book_testing_menu()

def borrow_return_menu():
    print("Would you like to test borrow or return functionality:")
    print("1. Borrow")
    print("2. Return")
    while True:
        try:
            return_or_borrow = int(input("Choose 1 or 2: "))
            clear_screen()
            if return_or_borrow == 1:
                print("Please choose the number of the book you would like to borrow:")
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
                print("Please choose the number of the book you would like to return:")
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
            book_testing_menu()
        except ValueError:
            print("Invalid selection. Please choose a valid option.")

def user_testing_menu():
    print(" --------------")
    print("| User Testing |")
    print(" --------------")
    print("Which method of the User class would you like to test:")
    print("1. Test the borrowing functionality (whether the user can borrow available books)")
    print("2. Test the return functionality (whether the user can return books)")
    print("3. Test viewing borrowed books")
    print("4. Return to Test Mode main menu")
    while True:
        try:
            selected_class_for_testing = int(input("Choose 1, 2, 3, or 4: "))
            clear_screen()
            if selected_class_for_testing in [1, 2, 3, 4]:
                if selected_class_for_testing == 1:
                    print("Testing borrowing functionality...")
                    print("Creating a book object...")
                    new_book = Book("The Hobbit", "J.R.R. Tolkien", "9780345534835", True)
                    print("Book object created successfully!")
                    print("Title: " + new_book.title)
                    print("Author: " + new_book.author)
                    print("ISBN: " + new_book.isbn)
                    print("Available: " + str(new_book.available))
                    print("Creating a user object...")
                    new_user = User("David", 4, [])
                    print("User object created successfully!")
                    print("Name: " + new_user.name)
                    print("ID: " + str(new_user.user_id))
                    print("Borrowing the book...")
                    new_user.borrow_book(new_book)
                    print("Book borrowed successfully!")
                    print("Available: " + str(new_book.available))
                elif selected_class_for_testing == 2:
                    print("Testing return functionality...")
                    print("Creating a book object...")
                    new_book = Book("The Hobbit", "J.R.R. Tolkien", "9780345534835", True)
                    print("Book object created successfully!")
                    print("Title: " + new_book.title)
                    print("Author: " + new_book.author)
                    print("ISBN: " + new_book.isbn)
                    print("Available: " + str(new_book.available))
                    print("Creating a user object...")
                    new_user = User("David", 4, [new_book])
                    print("User object created successfully!")
                    print("Name: " + new_user.name)
                    print("ID: " + str(new_user.user_id))
                    print("Returning the book...")
                    new_user.return_book(new_book)
                    print("Book returned successfully!")
                    print("Available: " + str(new_book.available))
                elif selected_class_for_testing == 3:
                    print("Testing viewing borrowed books...")
                    print("Creating a book object...")
                    new_book = Book("The Hobbit", "J.R.R. Tolkien", "9780345534835", True)
                    print("Book object created successfully!")
                    print("Title: " + new_book.title)
                    print("Author: " + new_book.author)
                    print("ISBN: " + new_book.isbn)
                    print("Available: " + str(new_book.available))
                    print("Creating a user object...")
                    new_user = User("David", 4, [new_book])
                    print("User object created successfully!")
                    print("Name: " + new_user.name)
                    print("ID: " + str(new_user.user_id))
                    print("Viewing borrowed books...")
                    new_user.view_borrowed_books()
                elif selected_class_for_testing == 4:
                    test_main_menu()
                break
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid selection. Please choose a valid option.")

def library_testing_menu():
    print(" -----------------")
    print("| Library Testing |")
    print(" -----------------")
    print("Which method of the Library class would you like to test:")
    print("1. Test adding and removing books from the library")
    print("2. Test adding and removing users")
    print("3. Test the borrow and return processes to ensure the logic works between Library, User, and Book")
    print("4. Return to Test Mode main menu")
    while True:
        try:
            selected_class_for_testing = int(input("Choose 1, 2, 3, or 4: "))
            clear_screen()
            if selected_class_for_testing in [1, 2, 3, 4]:
                if selected_class_for_testing == 1:
                    print("Testing adding and removing books from the library...")
                    print("Current books in the library:")
                    for book in library.books:
                        print(book)
                    print("Creating a book object...")
                    new_book = Book("The Hobbit", "J.R.R. Tolkien", "9780345534835", True)
                    print("Book object created successfully!")
                    print("Title: " + new_book.title)
                    print("Author: " + new_book.author)
                    print("ISBN: " + new_book.isbn)
                    print("Adding the book to the library...")
                    library.add_book(new_book)
                    print("Book added successfully!")
                    print("Current books in the library:")
                    for book in library.books:
                        print(book)
                    print("Removing the book from the library...")
                    library.remove_book(new_book)
                    print("Book removed successfully!")
                    print("Current books in the library:")
                    for book in library.books:
                        print(book)
                elif selected_class_for_testing == 2:
                    print("Testing adding and removing users from the library...")
                    print("Current users in the library:")
                    for user in library.users:
                        print(user.name)
                    print("Creating a user object...")
                    new_user = User("David", 4, [])
                    print("User object created successfully!")
                    print("Name: " + new_user.name)
                    print("ID: " + str(new_user.user_id))
                    print("Adding the user to the library...")
                    library.add_user(new_user)
                    print("User added successfully!")
                    print("Current users in the library:")
                    for user in library.users:
                        print(user.name)
                    print("Removing the user from the library...")
                    library.remove_user(new_user)
                    print("User removed successfully!")
                    print("Current users in the library:")
                    for user in library.users:
                        print(user.name)
                elif selected_class_for_testing == 3:
                    print("Testing borrowing and returning books from the library...")
                    print("Current books in the library:")
                    for book in library.books:
                        print(book)
                    print("Creating a book object...")
                    new_book = Book("The Hobbit", "J.R.R. Tolkien", "9780345534835", True)
                    print("Book object created successfully!")
                    print("Title: " + new_book.title)
                    print("Author: " + new_book.author)
                    print("ISBN: " + new_book.isbn)
                    print("Creating a user object...")
                    new_user = User("David", 4, [])
                    print("User object created successfully!")
                    print("Name: " + new_user.name)
                    print("ID: " + str(new_user.user_id))
                    print("Adding the book to the library...")
                    library.add_book(new_book)
                    print("Book added successfully!")
                    print("Borrowing the book...")
                    library.borrow_book(new_user, new_book)
                    print("Book borrowed successfully!")
                    print("Available: " + str(new_book.available))
                    print("Returning the book...")
                    library.return_book(new_user, new_book)
                    print("Book returned successfully!")
                    print("Available: " + str(new_book.available))
                elif selected_class_for_testing == 4:
                    test_main_menu()
                break
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Invalid selection. Please choose a valid option.")

test_main_menu()
