class ConsoleView:

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
        menu = """
        1. Примонтировать USB флешки
        2. Размонтировать USB флешки
        3. Выход
        """
        print(menu)
