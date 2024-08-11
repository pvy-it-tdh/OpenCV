import cv2
import mediapipe as mp

# Khởi tạo đối tượng Mediapipe cho nhận diện khuôn mặt
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Khởi tạo đối tượng Face Detection với độ chính xác mặc định
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.2)

# Mở webcam
cap = cv2.VideoCapture(0)

while True:
    # Đọc từng frame từ webcam
    success, img = cap.read()

    # Chuyển đổi ảnh sang RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Phát hiện khuôn mặt
    results = face_detection.process(img_rgb)

    # Kiểm tra xem có khuôn mặt nào được phát hiện không
    if results.detections:
        for detection in results.detections:
            # Vẽ hộp xung quanh khuôn mặt
            mp_drawing.draw_detection(img, detection)

    # Hiển thị ảnh
    cv2.imshow("Face Detection", img)

    # Thoát khỏi vòng lặp khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng camera và đóng cửa sổ
cap.release()
cv2.destroyAllWindows()
