from ultralytics import YOLO
from esrgan_helper import ESRGAN
import cv2
import pytesseract

# ESRGAN 모델 로드
esrgan = ESRGAN()

# YOLO 모델 로드
yolo_model = YOLO("yolov8n.pt")

# Tesseract OCR 설정
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def detect_and_read_numbers(image_path):
    # 1. 이미지 로드
    image = cv2.imread(image_path)
    original_image = image.copy()

    # 2. YOLO로 숫자 영역 탐지
    results = yolo_model(image)
    detections = results[0].boxes.xyxy  # 바운딩 박스 좌표 가져오기

    recognized_numbers = []
    for box in detections:
        x1, y1, x2, y2 = map(int, box)

        # 3. 탐지된 영역 자르기
        cropped = image[y1:y2, x1:x2]

        # 4. ESRGAN Super Resolution 적용
        high_res = esrgan.upscale(cropped)

        # 5. Tesseract OCR 실행
        config = "--psm 7 digits"
        text = pytesseract.image_to_string(high_res, config=config)
        recognized_numbers.append(text.strip())

        # 탐지 영역 시각화 (선택)
        cv2.rectangle(original_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(original_image, text.strip(), (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 결과 출력
    cv2.imshow("Detected Numbers", original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return recognized_numbers

# Paths to uploaded images
image_paths = []
for i in range(1,7):
    image_paths.append(fr"C:\Users\Public\test\{i}.jpg")

# 처리 실행
for img_path in image_paths:
    print(f"Processing {img_path}...")
    detected_numbers = detect_and_read_numbers(img_path)
    print(f"Detected Numbers: {detected_numbers}")
