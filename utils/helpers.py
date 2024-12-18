import os


def clear_screen():
    """
    Очищает экран консоли.
    Работает для Windows и Unix-систем.
    """
    os.system("cls" if os.name == "nt" else "clear")


def print_separator(length=40, symbol="-"):
    """
    Печатает разделитель для улучшения читаемости интерфейса.

    :param length: Длина разделителя.
    :param symbol: Символ, из которого состоит разделитель.
    """
    print(symbol * length)


def pause(message="\nНажмите Enter, чтобы продолжить..."):
    """
    Ждёт нажатия Enter от пользователя.

    :param message: Сообщение перед ожиданием.
    """
    input(message)



