import os
from PIL import Image
from carvekit.api.high import HiInterface
import torch
import cv2
import numpy as np


def background_removal(input_path, output_path):
    image_names=os.listdir(input_path)
    for image_name in image_names:
        # 배경제거를 위한 인터페이스 로딩
        interface = HiInterface(batch_size_seg=5, batch_size_matting=1,
                                    device='cuda' if torch.cuda.is_available() else 'cpu',
                                    seg_mask_size=1280, matting_mask_size=2048)

        # 원본 이미지 로드
        img_org = Image.open(os.path.join(input_path,image_name))

        alpha = 1.05  # 1보다 크면 대비 증가
        beta = 10    # 양수면 밝기 증가, 음수면 감소

        i=np.array(img_org)
        adjusted = cv2.convertScaleAbs(i, alpha=alpha, beta=beta)

        # 배경 제거
        img_bgrm = interface([Image.fromarray(adjusted)])[0]

        # 배경 제거된 후의 이미지의 밝기를 되돌린 후에 진행
        img_bgrm_np = np.array(img_bgrm.convert('RGBA'))
        mask = img_bgrm_np[:, :, 3] > 0  # 알파 채널 기준 객체 마스크

        restored_rgb = img_bgrm_np[:, :, :3].astype(np.float32)
        restored_rgb[mask] = ((restored_rgb[mask] - beta) / alpha).clip(0, 255)
        restored_rgb = restored_rgb.astype(np.uint8)

        alpha_channel = img_bgrm_np[:, :, 3]  # 원래 알파 채널 복원
        rgba_combined = np.dstack((restored_rgb, alpha_channel))
        img_bgrm_restored = Image.fromarray(rgba_combined, mode='RGBA')

        # 밝기 복원한 이미지를 저장
        img_bgrm_restored.save(os.path.join(output_path,image_name))


if __name__ == "__main__":
    # 배경을 지울 이미지들이 있는 경로
    input_path = "../ai06-level1-project/train_images/"
    # 배경을 지운 이미지들을 저장할 경로
    output_path = "../ai06-level1-project/train_output/"
    result = background_removal(input_path, output_path)