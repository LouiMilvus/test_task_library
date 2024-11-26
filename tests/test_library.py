import unittest
from unittest.mock import patch
import os
from library import Library
from book import BookStatus


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Инициализация тестовой библиотеки."""
        self.test_file = "test_storage.json"
        self.library = Library(storage_file=self.test_file)

    def tearDown(self):
        """Удаление тестового файла после тестов."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):
        """Тест на добавление книги в библиотеку."""
        self.library.add_book("Название", "Автор", 2023)
        books = self.library.list_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Название")
        self.assertEqual(books[0].status, BookStatus.AVAILABLE)

    @patch("builtins.print")  # Патчим функцию print, чтобы перехватить вывод
    def test_add_invalid_year(self, mock_print):
        """Тест на добавление книги с некорректным годом."""
        self.library.add_book("Некорректная книга", "Автор", 3000)
        mock_print.assert_called_with(
            "Ошибка: Некорректный год: 3000. Год должен быть между 1000 и 2024.")  # Проверяем, что правильное сообщение было выведено

    def test_year_validation(self):
        """Тест проверки корректности года книги."""
        self.assertTrue(self.library.is_valid_year(2020))  # Текущий год
        self.assertTrue(self.library.is_valid_year(1000))  # Минимальный год
        self.assertFalse(self.library.is_valid_year(999))  # Год ниже минимального
        self.assertFalse(self.library.is_valid_year(2100))  # Год в будущем

    def test_remove_book(self):
        """Тест на удаление книги из библиотеки по ID."""
        self.library.add_book("Название", "Автор", 2023)
        self.library.remove_book(1)
        self.assertEqual(len(self.library.list_books()), 0)

    def test_remove_nonexistent_book(self):
        """Тест на попытку удалить несуществующую книгу."""
        with self.assertRaises(ValueError):
            self.library.remove_book(999)

    def test_find_books(self):
        """Тест на поиск книг по названию, автору или году."""
        self.library.add_book("Название 1", "Автор 1", 2020)
        self.library.add_book("Название 2", "Автор 2", 2021)
        results = self.library.find_books("Автор 1")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, "Автор 1")

    def test_update_status(self):
        """Тест на обновление статуса книги."""
        self.library.add_book("Название", "Автор", 2023)
        self.library.update_status(1, "выдана")
        book = self.library.list_books()[0]
        self.assertEqual(book.status, BookStatus.CHECKED_OUT)

    def test_update_status_invalid(self):
        """Тест на попытку обновить статус книги на недопустимый."""
        self.library.add_book("Название", "Автор", 2023)
        with self.assertRaises(ValueError):
            self.library.update_status(1, "неизвестный статус")

    def test_persistence(self):
        """Тест на сохранение и загрузку данных из файла."""
        self.library.add_book("Название", "Автор", 2023)
        del self.library

        # Перезагрузка библиотеки из файла
        library = Library(storage_file=self.test_file)
        books = library.list_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Название")


if __name__ == "__main__":
    unittest.main()
