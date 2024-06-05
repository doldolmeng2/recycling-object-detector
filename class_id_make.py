import os
import glob


# glob 패턴으로 모든 텍스트 파일 목록 얻기
text_files = glob.glob(os.path.join("./dataset_4/train/labels/", "*.txt"))


# # dataset - bottle-0    cup-1
# # dataset2 - bottle -0
# # dataset3 - bottle -0
# # dataset4 - disposable - 2

for file in text_files:       
    with open(file, 'r') as f:
        text = f.read() # 파일 하나를 읽어옴
        if text == "":
            continue
        # 텍스트 처리 또는 출력
        lines = text.split('\n') # 파일을 줄바꿈 기준으로 나눔
        new_line = ""
        for l in lines:
            if l == "" or l == []:
                continue
            line = l.split() # 각 줄을 띄어쓰기 기준으로 나눠서 리스트로 저장
            # print(line)
            if line[0] == '0': # 리스트에 0인덱스 값이 ""이면 ""로 바꿈
                line[0] = '2'
            new_line += " ".join(line)
            new_line += "\n"
            # print(new_line)
            with open(file, 'w') as g:
                g.write(new_line)

    

