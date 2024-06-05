import cv2
import torch

# 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

# 카메라 스트림 열기
cap = cv2.VideoCapture(0)  # 0은 기본 카메라 장치를 의미합니다.

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 객체 탐지 수행
    results = model(frame)

    # 결과 시각화
    labels, cords = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
    n = len(labels)
    x_shape, y_shape = frame.shape[1], frame.shape[0]

    for i in range(n):
        row = cords[i]
        if row[4] >= 0.2:  # 신뢰도 20% 이상일 때만 표시
            x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
            bgr = (0, 255, 0)  # bounding box 색상
            cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
            cv2.putText(frame, model.names[int(labels[i])], (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)

    # 프레임 출력
    cv2.imshow('YOLOv5 Real-Time Object Detection', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
