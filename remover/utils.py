import cv2
import numpy as np
from PIL import Image

def clean_mask(img: Image.Image) -> Image.Image:
    rgba = np.array(img)
    alpha = rgba[:, :, 3]
    alpha = cv2.medianBlur(alpha, 5)
    alpha = cv2.GaussianBlur(alpha, (5, 5), 0)
    rgba[:, :, 3] = alpha
    return Image.fromarray(rgba)