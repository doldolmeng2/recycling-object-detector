# URL
https://github.com/doldolmeng2/recycling-object-detector

# 데이터 형식
dataset/
    images/
        train/
            image1.jpg
            image2.jpg
            ...
        val/
            image1.jpg
            image2.jpg
            ...
    labels/
        train/
            image1.txt
            image2.txt
            ...
        val/
            image1.txt
            image2.txt
            ...

# 라벨 파일 형식
<class_id> <x_center> <y_center> <width> <height>

# yaml 파일 형식

- dataset.yaml

train: ./dataset/images/train
val: ./dataset/images/val

nc: 3  # 클래스 수 (예: 3개의 재활용 쓰레기 종류)
names: ['plastic', 'glass', 'metal']  # 클래스 이름