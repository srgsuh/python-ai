import cv2
import numpy as np
from create_folders import TRAIN_DIR,VAL_DIR,IMAGE_SUB,LABEL_SUB,join_path
from circle_image import random_circle, CircleImage
import math
import os

WIDTH: int = 256
HEIGHT: int = 256
FNAME_PATTERN = '{ii}_circle_x_{x}_y_{y}_r_{r}'
IMAGE_EXT = '.jpg'
LABEL_EXT = '.txt'

def clear_all_files(root: str):
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            os.remove(os.path.join(dirpath, filename))

def get_img_path(parent_folder: str, f_name: str) -> str:
    return build_path(parent_folder, IMAGE_SUB, f_name, IMAGE_EXT)

def get_lbl_path(parent_folder: str, f_name: str) -> str:
    return build_path(parent_folder, LABEL_SUB, f_name, LABEL_EXT)

def write_test_case(parent_folder: str, f_name: str, img: np.ndarray, label: str) -> None:
    label_path = get_lbl_path(parent_folder, f_name)
    with open(label_path, 'w') as f:
        f.write(label)
    image_path = get_img_path(parent_folder, f_name)
    cv2.imwrite(image_path, img)

def build_path(parent: str, sub: str, name: str, ext: str) -> str:
    folder: str = join_path(parent, sub)
    return join_path(folder, name + ext)

def get_f_name(s_idx: str, c: CircleImage) -> str:
    x, y = c.center
    r = c.radius
    return FNAME_PATTERN.format(ii=s_idx,x=x,y=y,r=r)

def generate_test_circles(parent_folder: str, n_tests: int) -> None:
    prefix_length: int = math.ceil(math.log10(n_tests))
    for idx in range(1, n_tests + 1):
        s_idx = str(idx).zfill(prefix_length)
        c: CircleImage = random_circle(WIDTH, HEIGHT)
        f_name = get_f_name(s_idx, c)
        write_test_case(parent_folder, f_name, c.image(), c.label())

if __name__ == '__main__':
    clear_all_files(TRAIN_DIR)
    clear_all_files(VAL_DIR)
    generate_test_circles(TRAIN_DIR, 50)
    generate_test_circles(VAL_DIR, 5)
        