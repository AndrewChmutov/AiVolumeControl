from volume_changer import VolumeChanger
import main

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class WinVolumeChanger(VolumeChanger):
    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        self.volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    def getRange(self):
        return (self.volume.GetVolumeRange()[0], self.volume.GetVolumeRange()[1])

    def setVolume(self, volume):
        self.volume.SetMasterVolumeLevel(volume, None)
        
        
if __name__ == '__main__':
    main.main(WinVolumeChanger())