import unittest
from book import Book, BookStatus


class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book(1, "Название", "Автор", 2023)
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "Название")
        self.assertEqual(book.author, "Автор")
        self.assertEqual(book.year, 2023)
        self.assertEqual(book.status, BookStatus.AVAILABLE)

    def test_to_dict(self):
        book = Book(1, "Название", "Автор", 2023)
        expected = {
            "id": 1,
            "title": "Название",
            "author": "Автор",
            "year": 2023,
            "status": "в наличии",
        }
        self.assertEqual(book.to_dict(), expected)

    def test_from_dict(self):
        data = {
            "id": 1,
            "title": "Название",
            "author": "Автор",
            "year": 2023,
            "status": "в наличии",
        }
        book = Book.from_dict(data)
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "Название")
        self.assertEqual(book.author, "Автор")
        self.assertEqual(book.year, 2023)
        self.assertEqual(book.status, BookStatus.AVAILABLE)


if __name__ == "__main__":
    unittest.main()
