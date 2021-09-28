import typing

import util


NEGATIVE_ANSWERS = ["n", "no", "н", "нет"]
POSITIVE_ANSWERS = ["y", "yes", "д", "да"]


class Controller:

    def __init__(self, model, view) -> None:
        self.mounter = model
        self.view = view

    def run(self):
        """
        Точка входа в приложения
        """
        self.view.show_main_menu()

    def stop(self):
        """
        Выход из программы
        """
        exit(0)

    def _with_menu(self, inner: typing.Callable, *args, **kwargs):
        """
        Вызывает главное меню по выполнению оборачиваемой функции
        """
        inner(*args, **kwargs)
        self.ask_menu_item()

    def ask_menu_item(self):
        """
        Опрос пользователя на выбор пункта меню
        """
        message = "Выберите пункт меню: "
        correct_values = range(1, 3)
        item = self.view.ask_for(
            message, lambda answer: answer in correct_values)

        if item == 1:
            self._with_menu(self.mount_flashdrive())
        elif item == 2:
            self._with_menu(self.umount_flashdrive())
        elif item == 3:
            self.stop()

    def ask_delete_option(self):
        """
        Определяет необходимость удаление папок монтирования
        в зависимости от ввода пользователя
        """
        message = "Удалять папки для монтирования после размонтирования? "

        correct_values = NEGATIVE_ANSWERS + POSITIVE_ANSWERS
        answer = self.view.ask_for(
            message, lambda answer: answer in correct_values)
        if answer in NEGATIVE_ANSWERS:
            self.mounter.delete_paths = False
        elif answer in POSITIVE_ANSWERS:
            self.mounter.delete_paths = True

    def _ask_for_mount_path(self):
        """
        Опрос пользователя на путь до папки монтирования
        """
        message = "Введите путь до папки монтирования: "
        mount_root = self.view.ask_for(
            message, lambda path: util.is_path_correct(path))
        return mount_root

    def mount_flashdrive(self):
        """
        Запускает процесс монтирования USB флешки
        и опроса пользователя
        """
        mount_path = self._ask_for_mount_path()
        self.mounter.mount(mount_path)

    def umount_flashdrive(self):
        """
        Запускает процесс размонтирования USB флешки
        и опроса пользователя
        """
        mount_path = self._ask_for_mount_path()
        self.mounter.umount(mount_path)
