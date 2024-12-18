from utils.helpers import clear_screen, print_separator, pause
from database.database import get_db_connection
from tabulate import tabulate

def add_book():
    """
    Добавляет книгу в базу данных.
    """
    clear_screen()
    print("Добавление новой книги:")
    print_separator()

    title = input("Введите название книги: ").strip()
    author = input("Введите автора книги: ").strip()
    genre = input("Введите жанр книги: ").strip()
    year = input("Введите год издания книги: ").strip()

    if not title or not author or not genre or not year.isdigit():
        print("Ошибка! Некорректные данные. Попробуйте снова.")
        pause()
        return

    # Вставка данных в базу
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO books (title, author, genre, year) 
        VALUES (?, ?, ?, ?)
    """, (title, author, genre, int(year)))

    conn.commit()
    conn.close()
    print_separator()
    print("Книга успешно добавлена!")
    pause()


def show_books():
    """
    Отображает список всех книг из базы данных.
    """
    clear_screen()
    print("Список книг:")

    # Подключаемся к базе данных и получаем все книги
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, genre, year, status FROM books")
    books = cursor.fetchall()
    conn.close()

    # Проверяем, есть ли книги
    if not books:
        print("В базе данных пока нет книг.")
    else:
        # Выводим список книг
        table_headers = ["ID", "Название", "Автор", "Жанр", "Год", "Статус"]
        print(tabulate(books, headers=table_headers, tablefmt="grid"))

    pause()


def edit_book(book_id):
    """
    Редактирует данные выбранной книги, отображая текущие значения.
    Поля можно оставить без изменений, если они остаются пустыми.
    """
    clear_screen()
    print(f"Редактирование книги (ID: {book_id}):")
    print_separator()

    # Получаем текущие данные книги
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT title, author, genre, year 
        FROM books 
        WHERE id = ?
    """, (book_id,))
    book = cursor.fetchone()

    if not book:
        print("Ошибка! Книга не найдена.")
        pause()
        return

    current_title, current_author, current_genre, current_year = book

    # Показываем текущие значения пользователю
    print("Оставьте поле пустым, если хотите оставить текущее значение.")
    print_separator()
    print(f"Текущее название: {current_title}")
    new_title = input("Новое название: ").strip()
    print(f"Текущий автор: {current_author}")
    new_author = input("Новый автор: ").strip()
    print(f"Текущий жанр: {current_genre}")
    new_genre = input("Новый жанр: ").strip()
    print(f"Текущий год: {current_year}")
    new_year = input("Новый год: ").strip()

    # Используем текущие значения, если ввод пустой
    updated_title = new_title if new_title else current_title
    updated_author = new_author if new_author else current_author
    updated_genre = new_genre if new_genre else current_genre
    updated_year = new_year if new_year.isdigit() else current_year

    # Обновляем данные в базе данных
    cursor.execute("""
        UPDATE books
        SET title = ?, author = ?, genre = ?, year = ?
        WHERE id = ?
    """, (updated_title, updated_author, updated_genre, updated_year, book_id))
    conn.commit()
    conn.close()

    print("\nКнига успешно отредактирована!")


def delete_book(book_id):
    """
    Удаляет выбранную книгу из базы данных.
    """
    clear_screen()
    print(f"Удаление книги (ID: {book_id}):")
    confirm = input("Вы уверены, что хотите удалить эту книгу? (y/n): ").strip().lower()

    if confirm == "y":
        # Удаляем книгу из базы данных
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()
        print("Книга успешно удалена!")
    else:
        print("Удаление отменено.")



def search_books():
    """
    Ищет книги по названию или автору.
    """
    clear_screen()
    print("Поиск книги:")
    print_separator()

    # Запрос строки поиска
    search_query = input("Введите название книги или автора для поиска: ").strip()

    # Проверка на пустой ввод
    if not search_query:
        print("Ошибка! Строка поиска не может быть пустой.")
        pause()
        return

    # Подключаемся к базе данных и выполняем SQL-запрос
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, author, genre, year, status
        FROM books
        WHERE title LIKE ? OR author LIKE ?
    """, (f"%{search_query}%", f"%{search_query}%"))

    books = cursor.fetchall()
    conn.close()

    # Проверка результата поиска
    if not books:
        print("Книги не найдены по вашему запросу.")
    else:
        # Вывод результатов в виде таблицы
        print("\nРезультаты поиска:")
        table_headers = ["ID", "Название", "Автор", "Жанр", "Год", "Статус"]
        print(tabulate(books, headers=table_headers, tablefmt="grid"))

        # Запрос действия над книгой
        try:
            book_id = int(input("\nВведите ID книги для редактирования или удаления (0 - отмена): ").strip())
            if book_id == 0:
                return

            # Проверка, что введённый ID есть в результатах поиска
            book_ids = [book[0] for book in books]
            if book_id not in book_ids:
                print("Ошибка! Введённый ID отсутствует в результатах поиска.")
                pause()
                return

            # Предложение выбрать действие
            print("1. Редактировать книгу")
            print("2. Удалить книгу")
            action = input("Выберите действие: ").strip()

            if action == "1":
                edit_book(book_id)
            elif action == "2":
                delete_book(book_id)
            else:
                print("Некорректный выбор. Возврат в меню поиска.")
                pause()

        except ValueError:
            print("Ошибка! Введите корректный числовой ID.")

    pause()


def books_menu():
    while True:
        clear_screen()
        print("КНИГИ:")
        print_separator()
        print("1. Показать список книг")
        print("2. Добавить книгу")
        print("3. Найти книгу")
        print("0. Назад")
        print_separator()

        choice = input("\nВыберите действие: ").strip()
        if choice == "1":
            show_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            search_books()
        elif choice == "0":
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")
            pause()
