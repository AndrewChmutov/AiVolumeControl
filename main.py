import cv2
import time
import numpy as np
from hand_detection import HandDetector
from volume_changer import VolumeChanger
import math



def main(volume_ch: VolumeChanger):
    # video object, webcam
    cap = cv2.VideoCapture(0)
    draw = True
    detector = HandDetector()

    previous_time = current_time = 0


    # webcam picture processing 
    while True:
        # read the image
        _, img = cap.read()

        processed_img = detector.find_hands(img, draw)
        coords = detector.find_landmark_coords(img.shape)
        coords = [(i[1], i[2]) for i in coords]

        if coords:
            p1 = coords[4]
            p2 = coords[8]

            dist = math.hypot(p1[0] - p2[0], p1[1] - p2[1])
            vol = np.interp(dist, [35, 200], volume_ch.getRange())
            volume_ch.setVolume(vol)
            
            if draw:
                cv2.circle(processed_img, p1, 15, (255, 255, 255), cv2.FILLED)
                cv2.circle(processed_img, p2, 15, (255, 255, 255), cv2.FILLED)

                cv2.line(processed_img, p1, p2, (255, 255, 255), 3)

                center = (
                    p1[0] // 2 + p2[0] // 2,
                    p1[1] // 2 + p2[1] // 2
                )
                print(center)
                if dist < 35:
                    cv2.circle(processed_img, center, 15, (0, 255, 0), cv2.FILLED)
                else:
                    cv2.circle(processed_img, center, 15, (0, 0, 255), cv2.FILLED)
                    
        

        # FPS
        if draw:
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