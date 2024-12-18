from utils.helpers import clear_screen, print_separator, pause

def readers_menu():
    while True:
        clear_screen()
        print("ЧИТАТЕЛИ:")
        print_separator()
        print("1. Список читателей")
        print("2. Добавить читателя")
        print("3. Найти читателя")
        print("0. Назад")
        print_separator()

        choice = input("\nВыберите действие: ")
        if choice == "1":
            print("Список читателей...")
            pause()
        elif choice == "2":
            print("Добавление читателя...")
            pause()
        elif choice == "3":
            print("Поиск читателя...")
            pause()
        elif choice == "0":
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")
