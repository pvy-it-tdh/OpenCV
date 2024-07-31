"""
Hand Module

"""

import cv2
import mediapipe as mp
import time
import os


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode,
                                        max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon,
                                        min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    FolderPath = "Fingers"
    lst = os.listdir(FolderPath)
    lst_2 = []
    for i in lst:
        image = cv2.imread(f"{FolderPath}/{i}")
        lst_2.append(image)

    detector = handDetector(detectionCon=0.55)

    while True:
        # Đọc ảnh từ camera
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)

        # Đặt ảnh từ thư mục vào góc trên bên trái
        h, w, c = lst_2[0].shape
        img[0:h, 0:w] = lst_2[0]

        # Tính FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # Hiển thị FPS trên ảnh
        cv2.putText(img, f"FPS: {int(fps)}", (150, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        # Hiển thị ảnh
        cv2.imshow("CAM", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
