import typing


class ConsoleView:

    def __init__(self, menu_items: typing.Iterable = None):
        if menu_items is None:
            self.menu_items = [
                "Примонтировать USB флешки",
                "Размонтировать USB флешки",
                "Параметры удаления папок монтирования",
                "Выход"
            ]
        else:
            menu_items = menu_items
        self.menu_items_count = len(self.menu_items)

    def _generate_menu(self):
        """
        Создаёт меню из элементов menu_item
        """
        return "\n" + "".join([str(index + 1) + ". " + item + "\n" for index, item in enumerate(self.menu_items)])

    def show_message(self, message):
        print(message)

    def ask_for(self, message, is_correct):
        """
        Просит ввести пользователя значение выводя приглашение message
        """
        answer = input(message)
        while not is_correct(answer):
            print("Неверный ввод. Повторите попытку")
            answer = input(message)
        return answer

    def show_main_menu(self):
        menu = self._generate_menu()
        print(menu)
