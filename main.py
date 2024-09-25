
# Define a class called book which represents a book in the library.
class book:
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

# Define a class called user which represents a user of the library.
class user:
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

