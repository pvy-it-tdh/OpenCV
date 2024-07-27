import cv2
import imutils

#đọc ảnh
img = cv2.imread("troi.jpg")
#xoay ảnh 45 độ
img_rotate = imutils.rotate(img,45)

cv2.imshow("Rotated Image", img_rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
