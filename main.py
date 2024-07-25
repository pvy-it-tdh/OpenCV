import cv2

path = r'troi.jpg'
#đọc ảnh
img=cv2.imread(path)
#show ảnh
cv2.imshow('Anh', img)
#dừng màn hình
cv2.waitKey()
cv2.destroyWindow()
