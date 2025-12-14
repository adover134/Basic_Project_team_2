import streamlit as st
import os

# 이미지가 들어 있는 상위 디렉토리 경로
BASE_DIR = "./pill_image"

# 상위 디렉토리 내의 모든 폴더 탐색
folders = [f for f in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, f))]

num_cols = 4  

# 폴더들을 num_cols 단위로 나눠서 출력
for i in range(0, len(folders), num_cols):
    cols = st.columns(num_cols)
    for j, folder in enumerate(folders[i:i+num_cols]):
        folder_path = os.path.join(BASE_DIR, folder)
        images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        if images:
            first_image = os.path.join(folder_path, sorted(images)[0])
            with cols[j]:
                # 폴더 이름 출력
                st.write(f"**K-{str(int(folder)+1)}**")
                st.image(first_image, caption=folder, width=100)