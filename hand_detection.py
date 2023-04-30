import cv2
import mediapipe as mp
import time


class HandDetector:
    def __init__(
            self,
            static_image_mode = False,
            max_num_hands = 2,
            min_detection_confidence = 0.5,
            min_tracking_confidence = 0.5,
        ):

        ### init attributes

        # from parameters 
        self.mode = static_image_mode
        self.max_hands = max_num_hands,
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        
        # default
        self.hands = mp.solutions.hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils
    
    def convert_to_rgb(img):
        return cv2.Color(img, cv2.COLOR_BGR2RGB)
    

    def find_hands(self, img):
        # convert to RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        # show landmarks
        if self.results.multi_hand_landmarks:
            for i, handLms in enumerate(self.results.multi_hand_landmarks): # hand ...
                self.mp_draw.draw_landmarks(img, handLms, mp.solutions.hands.HAND_CONNECTIONS)


    def find_landmark_coords(self, hand_index=0):
        lm_list = []

        if (self.results.multi_hand_landmarks and 
            hand_index < len(self.results.multi_hand_landmarks)):
            hand = self.results.multi_hand_landmarks[hand_index]
            
            for id, lm in enumerate(hand.landmark):
                h, w, c = img.shape

                cx, cy = int(lm.x * w), int(lm.y * w)
                lm_list.append([id, cx, cy])

        return lm_list
    

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