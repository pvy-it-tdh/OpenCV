import time
import hand as htm
import cv2
import os
pTime=0
cap = cv2.VideoCapture(0)
FolderPath="Fingers"
lst=os.listdir(FolderPath)
lst_2=[]
songontay = 0  # Khởi tạo songontay với giá trị mặc định

for i in lst:
    image=cv2.imread(f"{FolderPath}/{i}")
    lst_2.append(image)
detector=htm.handDetector(detectionCon=0.55)
fingerid=[4,8,12,16,20]
while True:
  # Đọc ảnh
    ret, frame = cap.read()
    frame=detector.findHands(frame)
    lmList=detector.findPosition(frame,draw=False)
    if len(lmList)!=0:
        fingers= []

        # Viết cho ngón cái
        if lmList[fingerid[0]][1] < lmList[fingerid[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        print(lmList)
        # viết cho 4 ngón dài
        for id in range(1, 5):
            if lmList[fingerid[id]][2] < lmList[fingerid[id] - 2][2]:
                fingers.append(1)
                print(lmList[fingerid[id]][2])
                print(lmList[fingerid[id] - 2][2])
            else:
                fingers.append(0)

        print(fingers)
        songontay=fingers.count(1)
    h, w, c=lst_2[songontay-1].shape
    frame[0:h,0:w]=lst_2[songontay-1]
    # vẽ hình chữ nhật hiển thị số ngón tay
    cv2.rectangle(frame,(0,200),(150,400),(0,255,0),-1)
    cv2.putText(frame,str(songontay),(30,390),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),5)
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

