from menus import main_menu
from database.database import init_db


if __name__ == "__main__":
    init_db()  # Инициализация базы данных
    main_menu()