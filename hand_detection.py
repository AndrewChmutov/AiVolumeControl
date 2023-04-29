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

    # convert to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # show landmarks
    if results.multi_hand_landmarks:
        for i, handLms in enumerate(results.multi_hand_landmarks): # hand ...
            mp_draw.draw_landmarks(img, handLms, mp.solutions.hands.HAND_CONNECTIONS)

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