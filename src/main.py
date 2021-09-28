import mounter


if "__name__" == "__main__":
    mnt = mounter.Mounter("/mnt/")
    mnt.mount()
    input("Нажмите любую клавишу, чтобы размонитровать подключенные USB устройства")
    mnt.umount()