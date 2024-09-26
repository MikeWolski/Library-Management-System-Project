import unittest
from main import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book(1, 2, 3, 4)

    def test_borrow_book(self):
        self.assertEqual(self.book.borrow_book())

if __name__ == '__main__':
    unittest.main()