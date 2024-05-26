# URL
https://github.com/doldolmeng2/recycling-object-detector

# 데이터 형식
![image](https://github.com/doldolmeng2/recycling-object-detector/assets/150113294/fe508fd1-6fbc-4254-86b3-ba0dd5e4e3ae)


# 라벨 파일 형식

 (class_id) (x_center) (y_center) (width) (height)

# yaml 파일 형식

- dataset.yaml

train: ./dataset/images/train
val: ./dataset/images/val

nc: 3  # 클래스 수 (예: 3개의 재활용 쓰레기 종류)
names: ['plastic', 'glass', 'metal']  # 클래스 이름
