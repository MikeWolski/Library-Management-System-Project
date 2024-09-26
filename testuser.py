import unittest
from main import User

# Variables to be used in the tests

class TestUser(unittest.TestCase):
    # Set up any initial data or objects needed for the tests
    def setUp(self):
        self.users = [
            User("Alice", 1, []),
            User("Bob", 2, [])
        ]
    # Test the borrowing functionality (whether the user can borrow available books)
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
if __name__ == '__main__':
    unittest.main()