# OpenCV 활용 주차 위치 확인 시스템

## opecv >> project >> parking.py 실행

## 번호판 검출 과정
**1️⃣ 번호판 영상 수집** </br>
**2️⃣ 번호판 영상 학습 (SVM-Support Vector Machine 분류 이용) <ins><train_plate_data.py></ins>** </br>
**3️⃣ 번호판 분류** </br>
**3️⃣-1 차량 사진 입력 및 전처리 <ins><header/plate_preprocess.py></ins>**</br>
**- 블러링 > 소벨 마스크 적용 > 수직 방향 에지 검출**</br>
**3️⃣-2 번호판 후보영역 검색 <ins>함수 작성<train_plate_data.py>, 실행 <opencv/project/find_plates.py></ins>**</br>
**-find_candidates()함수를 통해 번호판 후보 영역 검색**</br>
**3️⃣-3 후보영역 영상 생성 <ins><opencv/project/correct_plate.py></ins>**</br>
**<header/plate_candidate.py>에서 생성한 후보 영역을 회전 시켜 기울기를 보정하여 영상을 생성시키고 번호판 사진을 표시**</br>
**3️⃣-4 후보 영상 번호판 판별<ins><opencv/project/classify_plate.py></ins>**</br>
**1️⃣,2️⃣에서 학습한 svm 파일을 로드하여 번호판 영상을 판별**</br>
**K-NN 글자학습을 통해 번호판의 사진의 숫자 및 문자를 인식**</br>
**4️⃣ 번호판 영상 표시<ins><opencv/project/classify_numbers.py></ins>** </br>
**5️⃣ 번호판의 문자 데이터를 <ins><header/plate_classify.py></ins>에서 str데이터로 저장**</br>
**6️⃣ 시뮬레이션**</br>
**-프로그램의 동작을 확인하기 위해 D라는 딕셔너리 생성, 주차 위치를 생성**</br>
![Image](https://github.com/user-attachments/assets/42d1b9cb-1950-42ce-ba3d-6869157a057e)</br>
**7️⃣ 결과**</br>
![Image](https://github.com/user-attachments/assets/c619c62b-7acc-4ef3-846c-8880aedb1efd)
