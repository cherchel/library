import sqlite3

DATABASE_NAME = "library.db"

def init_db():
    """
    Инициализация базы данных и создание таблиц.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Таблица книг
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            genre TEXT,
            year INTEGER,
            status TEXT DEFAULT 'available'
        )
    """)

    # Таблица читателей
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS readers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT
        )
    """)

    # Таблица журнала выдачи
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS borrowing_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            reader_id INTEGER,
            borrow_date TEXT,
            return_date TEXT,
            FOREIGN KEY (book_id) REFERENCES books (id),
            FOREIGN KEY (reader_id) REFERENCES readers (id)
        )
    """)

    conn.commit()
    conn.close()


def get_db_connection():
    """
    Возвращает соединение с базой данных.
    """
    return sqlite3.connect(DATABASE_NAME)
