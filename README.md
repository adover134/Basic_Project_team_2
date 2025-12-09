# 이미지 전처리
0. 가상환경 설정
0.1. carvekit을 중심으로 패키지들을 설치해야 합니다.
0.2. 추후 별도의 폴더에 해당 가상환경에서 필요한 패키지들을 requirements.txt로 만들겠습니다.
1. 배경 제거
  배경을 지울 이미지들이 있는 폴더가 input_path, 배경을 지운 결과 이미지들을 저장할 폴더가 output_path입니다.</br>
  사용 시 해당 파일을 여시고, 아래에서 input_path 및 output_path를 처리할 이미지가 있는 폴더 및 저장할 폴더로 변경해주세요.</br>
  그 후, 터미널에서 `python background_removal.py <input folder> <output folder>`를 입력하시면 자동으로 처리됩니다.</br>
   input folder는 배경을 지울 이미지들이 있는 폴더 경로를, output folder는 지운 이미지들을 저장할 폴더 경로를 적어주시면 됩니다.</br>
   폴더를 안 만들고 쓰셔도 자동으로 저장할 폴더를 생성해줍니다.</br>
   예를 들면 다음과 같이 사용합니다; `python background_removal.py train_image train_clean`

# 데이터 로드
data_load.ipynb 파일을 사용하면 됩니다. 코드 셀들은 다음의 기능들을 수행하는 데에 사용할 수 있습니다.
1. 이미지 단위의 annotation 결합
2. 이미지에 대해 온전한 annotation 집합을 만들 수 있는 이미지 이름 목록 획득</br>
  2.1. 이미지에 대해 annotation이 없는 이미지는 제외</br>
  2.2. annotation에 대해 이미지가 없는 annotation도 제외</br>
  2.3. 이미지에 포함된 모든 알약에 대해 일부 알약의 annotation은 없는 경우도 제외
3. annotation 파일들을 COCO 객체로 사용할 수 있는 형태로 결합
4. COCO 객체로 변환
5. YOLO 학습에 활용 가능한 형태로 변환

# 업데이트 내역
2025/12/09
추가 데이터의 라벨링 데이터 업로드</br>
[추가 데이터의 배경 지운 이미지 링크](https://drive.google.com/drive/folders/1D-aRz5nsbGubS3pPAP_DnG4oK4K3Kbx5?usp=drive_link)
