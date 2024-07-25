import cv2

image=cv2.imread("troi.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imwrite("troi_gray.jpg",image)