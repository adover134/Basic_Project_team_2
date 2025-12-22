# 이미지 전처리
## 1. 배경 제거
  ### 1.1. 가상환경 설정
    1.1.1. carvekit 버전: background_removal.py 파일을 참고하여 관련 라이브러리들을 설치합니다.
    1.1.2. rembg 버전: [rembg 라이브러리](https://github.com/danielgatis/rembg) 및 관련 라이브러리들을 설치합니다.
  ### 1.2. 배경 제거하기
    1.2.1. carvekit 버전
      배경을 지울 이미지들이 있는 폴더가 input_path, 배경을 지운 결과 이미지들을 저장할 폴더가 output_path입니다.
      사용 시 해당 파일을 여시고, 아래에서 input_path 및 output_path를 처리할 이미지가 있는 폴더 및 저장할 폴더로 변경해주세요.
      그 후, 터미널에서 `python background_removal.py <input folder> <output folder>`를 입력하시면 자동으로 처리됩니다.
      input folder는 배경을 지울 이미지들이 있는 폴더 경로를, output folder는 지운 이미지들을 저장할 폴더 경로를 적어주시면 됩니다.
      폴더를 안 만들고 쓰셔도 자동으로 저장할 폴더를 생성해줍니다.</br>
      예를 들면 다음과 같이 사용합니다; `python background_removal.py train_image train_clean`
      
    1.2.2. rembg 버전
      rembg는 기본적으로 U-Net을 사용하기에 객체를 정교하게 자르기에는 적합하지 않습니다.
      하지만, rembg에서 적용 가능한 여러 모델 중 birefnet-general 모델을 활용하면 속도가 매우 느린 대신 아주 정교하게 배경만 지워줍니다.
## 2. 이미지 전처리 및 라벨링
   ### 2.1. image_cut_and_classify
     2.1.1. bbox 검출
       bbox 검출을 위해, 미리 배경을 지운 이미지들을 준비합니다.
       각 이미지에 대해 OpenCV를 활용하여, 경계선 기반 마스크를 만든 뒤 bbox를 추출합니다.
     2.1.2. 객체 단위 이미지 생성
       각 알약 객체에 대해, 640 x 640 크기의 투명 이미지를 생성한 뒤 그 위에 합성하여 객체 단위 이미지를 만듭니다.
     2.1.3. 이미지 분류
       기본 데이터의 경우, 그 수가 충분치 않아 수작업으로 분류하였습니다.
       하지만, 추가 데이터의 경우 Dino v2를 활용하여 반자동으로 검출 후 검수하였습니다.
     2.1.4. 분류 파일 생성
       기본 데이터의 경우 분류 파일을 먼저 작성하고, 이에 기반하여 폴더 단위로 분류하는 것을 자동화하였습니다.
       반면, 추가 데이터의 경우 검출 과정에서 폴더 단위로 분류하고, 이에 기반하여 분류 파일을 생성하였습니다.
# 분류기 학습
## 1. classifier
### 1.1. 데이터셋 준비
  각 알약 종류 별로 폴더 단위로 준비한 개별 객체 이미지를 torchvision의 ImageFolder 기능을 활용하여 불러왔습니다.
### 1.2. 분류기 학습
  분류기는 torchvision의 사전학습 모델 중 EfficientNet을 활용하였습니다.
### 1.3. 예측
  테스트 데이터에 대해서도 전처리 과정에서와 동일한 과정을 거처 개별 객체 이미지를 만들었고, 학습한 분류기로는 알약 종류만 구한 뒤 전처리 과정에서 얻은 bbox 정보와 결합하여 출력합니다.

# YOLO 학습
## 1. YOLO_train
### 1.1. 데이터셋 준비
  전처리 과정에서 구한 bbox 정보를 활용하여 COCO Dataset 형식의 JSON 파일들을 만듭니다.
  이후, JSON 파일들을 합쳐 하나의 COCO 객체를 만든 뒤 YOLO Dataset으로 변환합니다.
### 1.2. YOLO 모델 학습
  회전, 기울임 등 다양한 증강을 추가하여 학습시켰습니다.
  원본 데이터가 3~4개의 객체들로 구성되어 있어 mosaic 증강을 0으로 두어 동작하지 않도록 하였습니다.

# 업데이트 내역
2025/12/09
추가 데이터의 라벨링 데이터 업로드</br>
[추가 데이터의 배경 지운 이미지 링크](https://drive.google.com/drive/folders/1USyioMVhVSsnp1XBnuTKZPm0DulvMpuZ?usp=sharing)

2025/12/21
최종 버전 파일들 업로드</br>
Readme 파일을 최종 버전에 맞춰 업데이트

# 팀원 별 일지 링크
## [김경태 링크](https://www.notion.so/2d18dd9ffeba806caa9aedec166c98a8?v=2d18dd9ffeba804e9344000c06a759cc&source=copy_link)
