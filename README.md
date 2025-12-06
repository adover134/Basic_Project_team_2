# 이미지 전처리
1. 배경 제거
   - 배경을 지울 이미지들이 있는 폴더가 input_path, 배경을 지운 결과 이미지들을 저장할 폴더가 output_path입니다.
   - 사용 시 해당 파일을 여시고, 아래에서 input_path 및 output_path를 처리할 이미지가 있는 폴더 및 저장할 폴더로 변경해주세요.
   - 그 후, 터미널에서 `python background_removal.py`를 입력하시면 자동으로 처리됩니다.

# 데이터 로드
data_load.ipynb 파일을 사용하면 됩니다. 코드 셀들은 다음의 기능들을 수행하는 데에 사용할 수 있습니다.
1. 이미지 단위의 annotation 결합
2. 이미지에 대해 온전한 annotation 집합을 만들 수 있는 이미지 이름 목록 획득
2.1. 이미지에 대해 annotation이 없는 이미지는 제외
2.2. annotation에 대해 이미지가 없는 annotation도 제외
2.3. 이미지에 포함된 모든 알약에 대해 일부 알약의 annotation은 없는 경우도 제외
3. annotation 파일들을 COCO 객체로 사용할 수 있는 형태로 결합
4. COCO 객체로 변환
5. YOLO 학습에 활용 가능한 형태로 변환
