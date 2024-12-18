class Book:
    """
    Класс для представления книги.
    """
    def __init__(self, book_id, title, author, genre, year, status="available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.status = status  # Статус: "available" или "borrowed"

    def __str__(self):
        return f"{self.book_id}. {self.title} ({self.author}, {self.year}) - {self.status}"


class Reader:
    """
    Класс для представления читателя.
    """
    def __init__(self, reader_id, first_name, last_name):
        self.reader_id = reader_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.reader_id}. {self.first_name} {self.last_name}"


class BorrowingRecord:
    """
    Класс для представления записи выдачи книги.
    """
    def __init__(self, record_id, book_id, reader_id, borrow_date, return_date=None):
        self.record_id = record_id
        self.book_id = book_id
        self.reader_id = reader_id
        self.borrow_date = borrow_date
        self.return_date = return_date

    def __str__(self):
        return f"Запись {self.record_id}: Книга ID {self.book_id}, Читатель ID {self.reader_id}, Выдана: {self.borrow_date}, Возвращена: {self.return_date}"
