import unittest
from main import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book(a, a, a, True)

    def test_init(self):
        self.assertEqual(self.book.title, a)
        self.assertEqual(self.book.author, 2)
        self.assertEqual(self.book.isbn, 3)
        self.assertEqual(self.book.available, 4)

#    def test_borrow_book(self):
#        self.assertEqual(self.book.borrow_book())

if __name__ == '__main__':
    unittest.main()