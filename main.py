from library import Library
from book import BookStatus

def main():
    library = Library()

    while True:
        print("\n--- Меню ---")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = input("Введите год издания книги: ")
                status = library.add_book(title, author, year)
                if status:
                    print("Книга добавлена.")

            elif choice == "2":
                book_id = int(input("Введите ID книги для удаления: "))
                library.remove_book(book_id)
                print("Книга удалена.")

            elif choice == "3":
                search_term = input("Введите название, автора или год издания: ")
                found_books = library.find_books(search_term)
                if found_books:
                    for book in found_books:
                        print(f"{book.id}: {book.title} - {book.author} ({book.year}) [{book.status.value}]")
                else:
                    print("Книги не найдены.")

            elif choice == "4":
                books = library.list_books()
                if books:
                    for book in books:
                        print(f"{book.id}: {book.title} - {book.author} ({book.year}) [{book.status.value}]")
                else:
                    print("Библиотека пуста.")

            elif choice == "5":
                book_id = int(input("Введите ID книги для изменения статуса: "))
                print("Введите новый статус: ")
                print(f"1. {BookStatus.AVAILABLE.value}")
                print(f"2. {BookStatus.CHECKED_OUT.value}")
                status_choice = input("Ваш выбор: ")

                if status_choice == "1":
                    new_status = BookStatus.AVAILABLE.value
                elif status_choice == "2":
                    new_status = BookStatus.CHECKED_OUT.value
                else:
                    raise ValueError("Неверный выбор статуса.")

                library.update_status(book_id, new_status)
                print("Статус обновлен.")

            elif choice == "6":
                print("Выход из программы.")
                break

            else:
                print("Неверный выбор. Попробуйте снова.")

        except ValueError as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
