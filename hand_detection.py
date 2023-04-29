import cv2
import mediapipe as mp
import time

# video object, webcam
cap = cv2.VideoCapture(0)

hands = mp.solutions.hands.Hands()
mp_draw = mp.solutions.drawing_utils

previous_time = current_time = 0


# webcam picture processing 
while True:
    # read the image
    _, img = cap.read()


    # FPS
    current_time = time.time()
    fps = 1/(current_time - previous_time)
    previous_time = current_time
    cv2.putText(img, 
        str(int(fps)), 
        (10, 70), 
        cv2.FONT_HERSHEY_PLAIN, 
        3, 
        (128, 0, 128), 
        3
    )
    
    cv2.imshow('Image', img)

    # delay
    cv2.waitKey(1)