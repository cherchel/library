from menus.books_menu import books_menu
from menus.readers_menu import readers_menu
from menus.journal_menu import journal_menu

from utils.helpers import clear_screen, print_separator

def main_menu():
    while True:
        clear_screen()
        print("Главное меню:")
        print_separator()
        print("1. Книги")
        print("2. Читатели")
        print("3. Журнал")
        print("0. Выход")
        print_separator()

        choice = input("\nВыберите действие: ")
        if choice == "1":
            books_menu()
        elif choice == "2":
            readers_menu()
        elif choice == "3":
            journal_menu()
        elif choice == "0":
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")
