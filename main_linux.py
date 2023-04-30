from volume_changer import VolumeChanger
from subprocess import call
import main


class LinuxVolumeChanger(VolumeChanger):
    def getRange(self):
        return (0, 100)

    def setVolume(self, volume):
        call(['amixer', '-D', 'pulse', 'sset', 'Master', str(volume) + '%'])


if __name__ == '__main__':
    main.main(LinuxVolumeChanger())