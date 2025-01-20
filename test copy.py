import easyocr
import cv2
from matplotlib import pyplot as plt

# EasyOCR Reader 객체 생성
reader = easyocr.Reader(['en'], gpu=False)  # GPU 사용 가능하면 gpu=True로 설정

def process_image_with_easyocr(image_path):
    # 이미지 로드
    image = cv2.imread(image_path)

    # EasyOCR로 텍스트 인식
    results = reader.readtext(image, detail=0)

    # 숫자만 필터링
    numbers = ''.join(filter(str.isdigit, ''.join(results)))
    
    # 중간 결과 출력 (Optional)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(f"Detected Numbers: {numbers}")
    plt.axis('off')
    plt.show()

    return numbers

# Paths to uploaded images
uploaded_image_paths = []
for i in range(1,7):
    uploaded_image_paths.append(fr"C:\Users\Public\test\{i}.jpg")

# 이미지별 숫자 추출
for i, img_path in enumerate(uploaded_image_paths):
    result = process_image_with_easyocr(img_path)
    print(f"Image {i+1}: Detected Numbers: {result}")