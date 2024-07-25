import cv2

#Đọc ảnh từ webcam thì 0 còn video thì tên file video
camera_id =0;
# Mở camera
cap=cv2.VideoCapture(camera_id)
# Đọc ảnh từ camera
while True:
    # Đọc ảnh
    ret, frame=cap.read()
    # Hiện ảnh
    cv2.imshow("CAM",frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv2.destroyWindow()