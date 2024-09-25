
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
# The borrow_book method is defined to check if the book is available. If it is, then it is borrowed and the book is no longer available.
    def borrow_book(self):
        if self.available:
            self.available = False
            return True
        else:
            return False
# If the book is not available, then it must be borrowed and it is able to be returned.
    def return_book(self):
        if not self.available:
            self.available = True
            return True
        else:
            return False
