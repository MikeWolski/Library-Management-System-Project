import unittest
from main import Book, User, Library  # Import the classes from main.py

# Variables to be used in the tests
book_title = "1985"
book_author = "George Orwell"
book_isbn = "9780451524935"
book_available = False
user_name = "Alice"

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
        new_book = Book(book_title, book_author, book_isbn, book_available)
        self.library.add_book(new_book)
        self.assertEqual(self.books[index].title, book_title, "The title of the book is incorrect")
        self.assertEqual(self.books[index].author, book_author, "The author of the book is incorrect")
        self.assertEqual(self.books[index].isbn, book_isbn, "The ISBN of the book is incorrect")
        self.assertEqual(self.books[index].available, book_available, "The availability of the book is incorrect")
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
        self.assertFalse(self.library.books[0].available, "The availability of the book is incorrect")
        print("Updated list of borrowed books:")
        self.library.list_unavailable_books()
        print()
        print("Current list of available books:")
        self.library.list_available_books()
        print()
        self.library.return_book(self.library.users[0], self.library.books[0])
        self.assertTrue(self.library.books[0].available, "The availability of the book is incorrect")
        print("Updated list of available books:")
        self.library.list_available_books()
        print()
    def test_borrow_book(self):
        print("----------------------------------------------------------------------")
        print()
        print("Testing borrowing functionality")
        print()
        print("Current list of available books:")
        self.library.list_available_books()
        print()
        self.library.borrow_book(self.library.users[0], self.library.books[0])
        self.assertEqual(len(self.library.users[0].borrowed_books), 1, "The number of borrowed books is incorrect")
        self.assertEqual(self.library.books[0].available, False, "The availability of the book is incorrect")
        print("Updated list of available books:")
        self.library.list_available_books()
        print()
        self.library.view_all_borrowed_books()
        print()
        print("Testing returning functionality")
        print()
        print("Current list of borrowed books:")
        self.library.list_unavailable_books()
        print()
        self.library.return_book(self.library.users[0], self.library.books[0])
        self.assertEqual(len(self.library.users[0].borrowed_books), 0, "The number of borrowed books is incorrect")
        self.assertEqual(self.library.books[0].available, True, "The availability of the book is incorrect")
        print("Updated list of borrowed books:")
        self.library.list_unavailable_books()
        print()
        self.library.view_all_borrowed_books()
        print()
if __name__ == '__main__':
    unittest.main()