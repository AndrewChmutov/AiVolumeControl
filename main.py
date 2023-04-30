import cv2
import time
import numpy
import platform
from hand_detection import HandDetector
from subprocess import call


class VolumeChanger:
    def getRange(self):
        pass

    def setVolume(self, volume):
        pass


class LinuxVolumeChanger(VolumeChanger):
    def getRange(self):
        return (0, 100)

    def setVolume(self, volume):
        call(['amixer', '-D', 'pulse', 'sset', 'Master', str(volume) + '%'])


def main():
    volume_changer = LinuxVolumeChanger()

    # video object, webcam
    cap = cv2.VideoCapture(0)

    detector = HandDetector()

    previous_time = current_time = 0


    # webcam picture processing 
    while True:
        # read the image
        _, img = cap.read()

        processed_img = detector.find_hands(img)


        # FPS
        current_time = time.time()
        fps = 1/(current_time - previous_time)
        previous_time = current_time
        cv2.putText(processed_img, 
            str(int(fps)), 
            (10, 70), 
            cv2.FONT_HERSHEY_PLAIN, 
            3,
            (128, 0, 128), 
            3
        )
        cv2.imshow('Image', processed_img)

        # delay
        cv2.waitKey(1)


if __name__ == '__main__':
    main()