import mounter


if __name__ == "__main__":
    mount_root = "/tmp/flashdrives/"
    mnt = mounter.Mounter(mount_root)
    mnt.mount()
    input("Нажмите любую клавишу, чтобы размонитровать подключенные USB устройства")
    mnt.umount()