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
        return (self.title + " by " + self.author)
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
    # The list_available_books method is defined to show all books currently borrowed by a user.
    def list_available_books(self):
        for book in self.books:
            if book.available:
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
clear_screen()
print(" -----------------------------")
print("| Library Test Mode Main Menu |")
print(" -----------------------------")
print("Which class would you like to test:")
print("1. Book")
print("2. User")
print("3. Library")

while True:
    try:
        selected_class_for_testing = int(input("Choose 1, 2, or 3: "))
        clear_screen()
        if selected_class_for_testing in [1, 2, 3]:
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")
    except ValueError:
        print("Invalid selection. Please choose 1, 2, or 3.")

if selected_class_for_testing == 1:
    print(" --------------")
    print("| Book Testing |")
    print(" --------------")
    print("Which method of the Book class would you like to test:")
    print("1. Test the creation of a book object")
    print("2. Test borrowing and returning functionality (whether the availability status changes)")
    print("3. Return to Test Mode main menu")
    while True:
        try:
            selected_class_for_testing = int(input("Choose 1, 2, or 3: "))
            clear_screen()
            if selected_class_for_testing in [1, 2, 3]:
                break
            else:
                print("Invalid selection. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid selection. Please choose 1, 2, or 3.")
elif selected_class_for_testing == 2:
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
                break
            else:
                print("Invalid selection. Please choose 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")
elif selected_class_for_testing == 3:
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
                break
            else:
                print("Invalid selection. Please choose 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")