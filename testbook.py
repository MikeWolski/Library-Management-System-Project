import unittest
from main import Book

# Variables to be used in the tests
book_title = "1985"
book_author = "George Orwell"
book_isbn = "9780451524935"
book_available = False

class TestBook(unittest.TestCase):
    # Set up any initial data or objects needed for the tests
    def setUp(self):
        self.books = [
            Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", True),
            Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", True)
        ]
    # Test that a new book can be created
    def test_create_book(self):
        print("----------------------------------------------------------------------")
        print()
        print("Testing the creation of a book object")
        print()
        index = len(self.books)
        new_book = Book(book_title, book_author, book_isbn, book_available)
        self.books.append(new_book)
        self.assertEqual(self.books[index].title, book_title, "The title of the book is incorrect")
        self.assertEqual(self.books[index].author, book_author, "The author of the book is incorrect")
        self.assertEqual(self.books[index].isbn, book_isbn, "The ISBN of the book is incorrect")
        self.assertEqual(self.books[index].available, book_available, "The availability of the book is incorrect")
    # Test that a book can be marked as borrowed and then returned
    def test_borrow_and_return_book(self):
        print("----------------------------------------------------------------------")
        print()
        print("Testing borrowing and returning a book")
        print()
        self.books[0].borrow_book()
        self.assertFalse(self.books[0].available, "The availability of the book is incorrect")
        self.books[0].return_book()
        self.assertTrue(self.books[0].available, "The availability of the book is incorrect")
if __name__ == '__main__':
    unittest.main()