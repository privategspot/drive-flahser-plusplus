import mounter


if __name__ == "__main__":
    mount_root = "/tmp/flashdrives/"
    mnt = mounter.Mounter(mount_root)
    mnt.mount()
    print(f"USB флешки были примонтированы в {mount_root}")
    input("Нажмите любую клавишу, чтобы размонитровать подключенные USB устройства")
    mnt.umount()