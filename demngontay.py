import time

import cv2
import os
pTime=0
cap = cv2.VideoCapture(0)
FolderPath="Fingers"
lst=os.listdir(FolderPath)
lst_2=[]
for i in lst:
    image=cv2.imread(f"{FolderPath}/{i}")
    lst_2.append(image)
while True:
  # Đọc ảnh
    ret, frame = cap.read()
    h, w, c=lst_2[0].shape
    frame[0:h,0:w]=lst_2[0]

    # viết FPS
    Ctime =time.time()
    fps=1/(Ctime-pTime)
    pTime=Ctime
    cv2.putText(frame,f"FPS: {int(fps)}",(150,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0 ,0),3)
    # Hiện ảnh
    cv2.imshow("CAM", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyWindow()