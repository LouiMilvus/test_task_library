import json
from book import Book, BookStatus
import datetime


class Library:
    def __init__(self, storage_file="./storage.json"):
        self.storage_file = storage_file
        self.books = []
        self.load_books()

    def load_books(self):
        """Загружает книги из файла."""
        try:
            with open(self.storage_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.books = [Book.from_dict(book) for book in data]
        except FileNotFoundError:
            self.books = []

    def save_books(self):
        """Сохраняет книги в файл."""
        with open(self.storage_file, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        """Добавить книгу с проверкой корректности года."""
        # Попытка преобразовать год в целое число
        try:
            year = int(year)  # Преобразуем год в целое число
        except ValueError:
            print(f"Ошибка: Год '{year}' не является числом.")
            return False

        if not self.is_valid_year(year):
            print(f"Ошибка: Некорректный год: {year}. Год должен быть между 1000 и {datetime.datetime.now().year}.")
            return False
        # book_id будет автоматически увеличиваться, так как книги хранятся в списке
        book_id = len(self.books) + 1  # Увеличиваем ID для новой книги
        book = Book(book_id=book_id, title=title, author=author, year=year)
        self.books.append(book)
        self.save_books()
        print(f"Книга '{title}' успешно добавлена.")
        return True

    def is_valid_year(self, year):
        """Проверка корректности года (должен быть между 1000 и текущим годом)."""
        current_year = datetime.datetime.now().year
        return 1000 <= year <= current_year

    def remove_book(self, book_id):
        """Удаляет книгу по ID."""
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                return
        raise ValueError("Книга с указанным ID не найдена.")

    def find_books(self, search_term):
        """Ищет книги по названию, автору или году."""
        return [
            book for book in self.books
            if search_term.lower() in book.title.lower() or
            search_term.lower() in book.author.lower() or
            search_term == str(book.year)
        ]

    def list_books(self):
        """Возвращает список всех книг."""
        return self.books

    def update_status(self, book_id, new_status):
        """Обновляет статус книги."""
        for book in self.books:
            if book.id == book_id:
                try:
                    book.status = BookStatus(new_status)
                    self.save_books()
                    return
                except ValueError:
                    raise ValueError("Недопустимый статус. Выберите 'в наличии' или 'выдана'.")
        raise ValueError("Книга с указанным ID не найдена.")
