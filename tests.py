import unittest
from main import Book, User, Library  # Import the classes from main.py

class TestBook(unittest.TestCase):
    # Set up any initial data or objects needed for the tests
    def setUp(self):
        self.books = [
            Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", True),
            Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", True)
        ]
        self.users = [
            User("Alice", 1, []),
            User("Bob", 2, [])
        ]
        self.library = Library(self.books, self.users)
    # Test that a new book can be created
    def test_create_book(self):
        print("----------------------------------------------------------------------")
        print()
        print("Testing book creation")
        print()
        print("Current list of books:")
        self.library.list_books()
        print()
        index = len(self.books)
        new_book = Book("1984", "George Orwell", "9780451524935", True)
        self.library.add_book(new_book)
        self.assertEqual(self.library.books[index].title, "1984", "The title of the book is incorrect")
        self.assertEqual(self.library.books[index].author, "George Orwell", "The author of the book is incorrect")
        self.assertEqual(self.library.books[index].isbn, "9780451524935", "The ISBN of the book is incorrect")
        self.assertEqual(self.library.books[index].available, True, "The availability of the book is incorrect")
        print("Updated list of books:")
        self.library.list_books()
    # Test that a book can be borrowed and then returned
    def test_borrow_and_return_book(self):
        print("----------------------------------------------------------------------")
        print()
        print("Testing borrowing and returning a book")
        print()
        print("Current list of borrowed books:")
        self.library.list_unavailable_books()
        print()
        self.library.borrow_book(self.library.users[0], self.library.books[0])
        self.assertEqual(len(self.library.users[0].borrowed_books), 1, "The number of borrowed books is incorrect")
        self.assertEqual(self.library.books[0].available, False, "The availability of the book is incorrect")
        print("Updated list of borrowed books:")
        self.library.list_unavailable_books()
        print()
        print("Current list of available books:")
        self.library.list_available_books()
        print()
        self.library.return_book(self.library.users[0], self.library.books[0])
        self.assertEqual(len(self.library.users[0].borrowed_books), 0, "The number of borrowed books is incorrect")
        self.assertEqual(self.library.books[0].available, True, "The availability of the book is incorrect")
        print("Updated list of available books:")
        self.library.list_available_books()
        print()
if __name__ == '__main__':
    unittest.main()