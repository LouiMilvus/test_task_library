from enum import Enum

class BookStatus(Enum):
    """Перечисление для статуса книги."""
    AVAILABLE = "в наличии"
    CHECKED_OUT = "выдана"


class Book:
    def __init__(self, book_id, title, author, year, status=BookStatus.AVAILABLE):
        """Конструктор книги, принимает id, название, автора, год и статус книги."""
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        """Возвращает словарь с данными книги для сохранения в файл."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status.value,  # Преобразуем статус в строку для хранения
        }

    @staticmethod
    def from_dict(data):
        """Создает экземпляр Book из словаря, полученного из файла."""
        return Book(
            book_id=data["id"],  # Используем "id" для создания book_id
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=BookStatus(data["status"]),  # Преобразуем строку обратно в BookStatus
        )
