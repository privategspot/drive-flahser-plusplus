import typing
import glob
import os
import logging


def default_searcher():
        """
        Стандартная функция поиска подключенных устройств
        Ищет устройства по пути /dev/ устройства соответствующие патерну sd[b-z]3
        """
        default_path = "/dev/sd[b-z]3"
        paths = glob.glob(default_path)
        return paths


class Mounter:

    """
    Класс инкапсулирующий логику по монтированию usb-флешек в Linux
    """

    def __init__(self, mount_root: str, searcher: typing.Callable = None):
        if searcher == None:
            self.searcher = default_searcher
        else:
            self.searcher = searcher
        self._used_ids = set()
        self._next_id = 0
        self._mount_root = mount_root
        self._mounted_paths = []
    
    def _get_next_id(self):
        next_id = self._next_id
        self._used_ids.add(next_id)
        self._next_id += 1
        return next_id

    def _search_devices(self):
        """
        Ищет подключеные устройства при помощи функции поиска
        """
        devices = self.searcher()
        logging.log(logging.INFO, f"Найдены следующие устройства:\n{devices}")
        return devices

    def _create_directory(self, root):
        """
        Создает папку для монтирования usb-флешки
        """
        id = self._get_next_id()
        mount_path = root + f"/{id}"

        try:
            os.makedirs(mount_path)
        except FileExistsError:
            pass
        logging.log(logging.INFO, f"Создана папка для монтирования {mount_path}")
        return mount_path

    def _mount(self, src, dest):
        """
        Монтирует устройства в папки с уникальным идентификатором
        """
        mount_cmd = f"mount {src} {dest}"
        os.system(mount_cmd)
        logging.log(logging.INFO, f"Устройство {src} примонтировано в {dest}")

    def mount(self) -> int:
        """
        Ищет покдлюченые устройства используя функцию поиска searcher
        и монтирует их в папки с уникальным идентификатором
        """
        devices = self._search_devices()
        for dev in devices:
            mount_path = self._create_directory(self._mount_root)
            self._mount(dev, mount_path)
            self._mounted_paths.append(mount_path)

    def _umount(self, mount_path):
        """
        Демонтирует usb флешку по пути mount_path
        """
        umount_cmd = f"umount {mount_path}"
        os.system(umount_cmd)

    def umount(self):
        """
        Демонтирует примонтированные устройства
        """
        for path in self._mounted_paths:
            self._umount(path)
