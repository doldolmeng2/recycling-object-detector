# 학습 명령어
python3 train.py --img 640 --batch 4 --epochs 50 --data dataset.yaml --cfg models/yolov5s.yaml --weights yolov5s.pt --name recycle_detector --device 0

# 테스트 명령어
모델 경로 확인
python3 detect.py --weights runs/train/recycle_detector16/weights/best.pt --img 640 --conf 0.25 --source ../dataset/test/images

# 문제 해결
- 모델 학습시 dataset.yaml 파일의 경로를 잘 찾지 못함 -> 절대 경로로 설정해주어야함
# URL
https://github.com/doldolmeng2/recycling-object-detector

# 데이터 형식
![image](https://github.com/doldolmeng2/recycling-object-detector/assets/150113294/fe508fd1-6fbc-4254-86b3-ba0dd5e4e3ae)


# class ID
 0 : bottle
 1 : cup
 2 : disposable 
# 라벨 파일 형식

 (class_id) (x_center) (y_center) (width) (height)

# yaml 파일 형식

- dataset.yaml

train: ./dataset/images/train
val: ./dataset/images/val

nc: 3  # 클래스 수 (예: 3개의 재활용 쓰레기 종류)
names: ['plastic', 'glass', 'metal']  # 클래스 이름
