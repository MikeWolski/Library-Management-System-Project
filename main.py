
# Define a class called Book which represents a book in the library.
class Book:
    def __init__(self, title, author, isbn, available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
    # A string representation of the book object is returned.
    def __str__(self):
        self.__str__ = self.title + " by " + self.author
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