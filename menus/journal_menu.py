from utils.helpers import clear_screen, print_separator, pause

def journal_menu():
    while True:
        clear_screen()
        print("ЖУРНАЛ:")
        print_separator()
        print("1. Выдача книги")
        print("2. Возврат книги")
        print("3. Просмотр истории")
        print("0. Назад")
        print_separator()

        choice = input("\nВыберите действие: ")
        if choice == "1":
            print("Выдаем книгу...")
            pause()
        elif choice == "2":
            print("Возвращаем книгу...")
            pause()
        elif choice == "3":
            print("Смотрим историю...")
            pause()
        elif choice == "0":
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")
